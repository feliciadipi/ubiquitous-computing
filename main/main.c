#include <stdio.h>
#include "esp_system.h"
#include "esp_event.h"
#include "esp_log.h"
#include "nvs_flash.h"
#include "esp_netif.h"
#include "mpu6050.h"

static const char *TAG = "I2C MPU6050";
static const char buf[128];
static mpu6050_handle_t mpu6050 = NULL;

#define I2C_MASTER_SCL_IO CONFIG_I2C_MASTER_SCL         /*!< GPIO number used for I2C master clock */
#define I2C_MASTER_SDA_IO CONFIG_I2C_MASTER_SDA         /*!< GPIO number used for I2C master data  */
#define I2C_MASTER_NUM 0                                /*!< I2C master i2c port number, the number of i2c peripheral interfaces available will depend on the chip */
#define I2C_MASTER_FREQ_HZ 100000                       /*!< I2C master clock frequency */
#define I2C_MASTER_TX_BUF_DISABLE 0                     /*!< I2C master doesn't need buffer */
#define I2C_MASTER_RX_BUF_DISABLE 0                     /*!< I2C master doesn't need buffer */
#define I2C_MASTER_TIMEOUT_MS 1000

#define MPU6050_SENSOR_ADDR 0x68    /*!< I2C address of the MPU6050 sensor */
#define MPU6050_PWR_MGMT_1 0x6B     /*!< Register addresses of the power managment register */
#define MPU9250_WHO_AM_I 0x75       /*!< Register addresses of the "who am I" register */
#define MPU6050_RESET_BIT 7

static esp_err_t i2c_master_init(void) {
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

void app_main(void) {
    mpu6050 = mpu6050_create(I2C_MASTER_NUM, MPU6050_SENSOR_ADDR);
    ESP_ERROR_CHECK(i2c_master_init());
    ESP_LOGI(TAG, "I2C initialized successfully");
    ESP_ERROR_CHECK(mpu6050_config(mpu6050, ACCE_FS_4G, GYRO_FS_500DPS));
    ESP_ERROR_CHECK(mpu6050_wake_up(mpu6050));

    mpu6050_acce_value_t acce;
    mpu6050_gyro_value_t gyro;

    for (int j=0; j<20; ++j) {
        ESP_LOGI(TAG, "----------SAMPLE #%d----------", j);
        ESP_LOGI(TAG, "----------SAMPLE #%d----------", j);
        ESP_LOGI(TAG, "----------SAMPLE #%d----------", j);
        ESP_LOGI(TAG, "----------SAMPLE #%d----------", j);
        ESP_LOGI(TAG, "----------SAMPLE #%d----------", j);
        ESP_LOGI(TAG, "----------SAMPLE #%d----------", j);
        ESP_LOGI(TAG, "----------SAMPLE #%d----------", j);
        ESP_LOGI(TAG, "----------SAMPLE #%d----------", j);
        ESP_LOGI(TAG, "----------SAMPLE #%d----------", j);
        ESP_LOGI(TAG, "----------SAMPLE #%d----------", j);
        for (int i=0; i<400; ++i) {
            ESP_ERROR_CHECK(mpu6050_get_acce(mpu6050, &acce));
            ESP_ERROR_CHECK(mpu6050_get_gyro(mpu6050, &gyro));
            snprintf(buf, 128, "%f,%f,%f,%f,%f,%f", acce.acce_x, acce.acce_y, acce.acce_z, gyro.gyro_x, gyro.gyro_y, gyro.gyro_z);
            puts(buf);
        }
        vTaskDelay(pdMS_TO_TICKS(10));
    }
    mpu6050_delete(mpu6050);
}