#!/usr/bin/env python3

import time
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280

print("""all-values.py - Read temperature, pressure, and humidity

Press Ctrl+C to exit!

""")

# Initialise the BME280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

bme280.setup()

print('bme280 unique identifier: {:x}'.format(bme280.unique_id))

while True:
    temperature = bme280.get_temperature()
    fahrenheit = 9.0/5.0 * temperature + 32
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()
    print('{:05.2f}*C {:05.2f}*F {:05.2f}hPa {:05.2f}%'.format(temperature, fahrenheit, pressure, humidity))
    time.sleep(1)
