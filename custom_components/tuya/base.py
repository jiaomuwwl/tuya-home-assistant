#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from typing import Any, Dict, List, Optional, Tuple, cast

from .const import (
    DOMAIN,
)

from tuya_iot import TuyaDeviceManager, TuyaDevice

class TuyaHaDevice:
    """Tuya base device."""

    tuyaDevice: TuyaDevice
    tuyaDeviceManager: TuyaDeviceManager

    def __init__(self, device: TuyaDevice, deviceManager: TuyaDeviceManager):
        super().__init__()
        self.tuyaDevice = device
        self.tuyaDeviceManager = deviceManager
        self.entity_id = 'tuya.{}'.format(device.id)

    @staticmethod
    def remap(old_value, old_min, old_max, new_min, new_max):
        new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min
        return new_value

    # Entity

    @property
    def should_poll(self) -> bool:
        return False

    @property
    def unique_id(self) -> Optional[str]:
        """Return a unique ID."""
        return self.tuyaDevice.uuid

    @property
    def name(self) -> Optional[str]:
        """Return Tuya device name."""
        return self.tuyaDevice.name

    @property
    def device_info(self):
        """Return a device description for device registry."""
        _device_info = {
            "identifiers": {(DOMAIN, f"{self.unique_id}")},
            "manufacturer": "tuya",
            "name": self.name,
            "model": self.tuyaDevice.product_name,
        }
        return _device_info

    # @property
    # def icon(self) -> Optional[str]:
    #     """Return Tuya device icon."""
    #     cdn_url = 'https://images.tuyacn.com/'
    #     # TODO customize cdn url
    #     return cdn_url + self.tuyaDevice.icon

    @property
    def available(self) -> bool:
        """Return if the device is available."""
        return self.tuyaDevice.online
