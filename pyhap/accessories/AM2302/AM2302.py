"""An Accessory for the AM2302 temperature and humidity sensor.
Assumes the DHT22 module is in a package called sensors.

Also, make sure pigpiod is running.
"""
import asyncio

import pigpio

from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_SENSOR

from .sensor import sensor


class AM2302(Accessory):
    """
    Accessory for the AM2302 temperature and humidity sensor.
    """

    category = CATEGORY_SENSOR

    def __init__(self, *args, pin=4, **kwargs):
        super().__init__(*args, **kwargs)
        self.pin = pin

        serv_temp = self.add_preload_service('TemperatureSensor')
        serv_humidity = self.add_preload_service('HumiditySensor')

        self.char_temp = serv_temp.get_characteristic('CurrentTemperature')
        self.char_humidity = serv_humidity \
            .get_characteristic('CurrentRelativeHumidity')

        self.sensor = sensor(pigpio.pi(), pin)

    @Accessory.run_at_interval(60)
    async def run(self):
        await self.driver.loop.run_in_executor(executor=None,
                                               func=self.sensor.trigger)
        await asyncio.sleep(0.2)
        t = self.sensor.temperature()
        h = self.sensor.humidity()
        self.char_temp.set_value(t)
        self.char_humidity.set_value(h)
