| Supported Targets | ESP32 | ESP32-C3 | ESP32-C6 | ESP32-H2 | ESP32-P4 | ESP32-S2 | ESP32-S3 |
| ----------------- | ----- | -------- | -------- | -------- | -------- | -------- | -------- |

# Signal Processing with I2C

## Overview

This example demonstrates basic usage of I2C driver by reading and writing from a I2C connected sensor.

## Usage

### Hardware Required:

To run this example, you should have one ESP32, ESP32-S, ESP32-C or ESP32-H based development board as well as a MPU9250. MPU9250 is a inertial measurement unit, which contains a accelerometer, gyroscope as well as a magnetometer, for more information about it, you can read the [datasheet of the MPU9250 sensor](https://invensense.tdk.com/wp-content/uploads/2015/02/PS-MPU-9250A-01-v1.1.pdf).

#### Pin Assignment:

**Note:** The following pin assignments are used by default, you can change these in the `menuconfig` .

|                  | SDA             | SCL           |
| ---------------- | -------------- | -------------- |
| ESP I2C Master   | I2C_MASTER_SDA | I2C_MASTER_SCL |
| MPU9250 Sensor   | SDA            | SCL            |

### Build and Flash

Enter `idf.py -p PORT flash monitor` to build, flash and monitor the project.

(To exit the serial monitor, type ``Ctrl-]``.)

See the [Getting Started Guide](https://docs.espressif.com/projects/esp-idf/en/latest/get-started/index.html) for full steps to configure and use ESP-IDF to build projects.