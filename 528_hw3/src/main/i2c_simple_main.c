#include <stdio.h>
#include "esp_log.h"
#include "driver/i2c.h"

static const char *TAG = "i2c-mpu6050";

#define I2C_MASTER_SCL_IO           1                   /*!< GPIO number used for I2C master clock */
#define I2C_MASTER_SDA_IO           0                   /*!< GPIO number used for I2C master data  */
#define I2C_MASTER_NUM              0                   /*!< I2C master i2c port number, the number of i2c peripheral interfaces available will depend on the chip */
#define I2C_MASTER_FREQ_HZ          100000              /*!< I2C master clock frequency */
#define I2C_MASTER_TX_BUF_DISABLE   0                   /*!< I2C master doesn't need buffer */
#define I2C_MASTER_RX_BUF_DISABLE   0                   /*!< I2C master doesn't need buffer */
#define I2C_MASTER_TIMEOUT_MS       1000

#define MPU6050_SENSOR_ADDR         0x68                /*!< I2C address of the MPU6050 sensor */
#define MPU6050_PWR_MGMT_1          0x6B                /*!< Register addresses of the power managment register */
#define MPU6050_RESET_BIT           7       
#define MPU6050_OUT                 0x3B                /*!< Register address of ACCEL_XOUT_H (first accelerometer output register) */

/**
 * @brief Read a sequence of bytes from a MPU6050 sensor registers
 */
static esp_err_t mpu6050_register_read(uint8_t reg_addr, uint8_t *data, size_t len)
{
    return i2c_master_write_read_device(I2C_MASTER_NUM, MPU6050_SENSOR_ADDR, &reg_addr, 1, data, len, I2C_MASTER_TIMEOUT_MS / portTICK_PERIOD_MS);
}

/**
 * @brief Write a byte to a MPU6050 sensor register
 */
static esp_err_t mpu6050_register_write_byte(uint8_t reg_addr, uint8_t data)
{
    int ret;
    uint8_t write_buf[2] = {reg_addr, data};

    ret = i2c_master_write_to_device(I2C_MASTER_NUM, MPU6050_SENSOR_ADDR, write_buf, sizeof(write_buf), I2C_MASTER_TIMEOUT_MS / portTICK_PERIOD_MS);

    return ret;
}

/**
 * @brief i2c master initialization
 */
static esp_err_t i2c_master_init(void)
{
    int i2c_master_port = I2C_MASTER_NUM;

    i2c_config_t conf = {
        .mode = I2C_MODE_MASTER,
        .sda_io_num = I2C_MASTER_SDA_IO,
        .scl_io_num = I2C_MASTER_SCL_IO,
        .sda_pullup_en = GPIO_PULLUP_ENABLE,
        .scl_pullup_en = GPIO_PULLUP_ENABLE,
        .master.clk_speed = I2C_MASTER_FREQ_HZ,
    };

    i2c_param_config(i2c_master_port, &conf);

    return i2c_driver_install(i2c_master_port, conf.mode, I2C_MASTER_RX_BUF_DISABLE, I2C_MASTER_TX_BUF_DISABLE, 0);
}

void app_main(void)
{
    uint8_t data[14];
    ESP_ERROR_CHECK(i2c_master_init());
    ESP_LOGI(TAG, "I2C initialized successfully");

    /* Write 0x00 to PWR_MGMT_1 to wake up MPU6050 */
    ESP_ERROR_CHECK(mpu6050_register_write_byte(MPU6050_PWR_MGMT_1, 0));

    short accel_x;
	short accel_y;
	short accel_z;
    short gyro_x;
	short gyro_y;
	short gyro_z;

    while(true) {

        /* Read 14 bytes from MPU6050 starting at ACCEL_XOUT_H */
        ESP_ERROR_CHECK(mpu6050_register_read(MPU6050_OUT, data, 14));

        /* Get accelerometer data from buffer (big-endian) */
        accel_x = (data[0] << 8) | data[1];
		accel_y = (data[2] << 8) | data[3];
		accel_z = (data[4] << 8) | data[5];

        /* Get gyroscope data from buffer (big-endian) */
        gyro_x = (data[8] << 8) | data[9];
        gyro_y = (data[10] << 8) | data[11];
        gyro_z = (data[12] << 8) | data[13];

        /* Log sensor readings */
        ESP_LOGI(TAG, "%d,%d,%d,%d,%d,%d", accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z);
        
    }
}