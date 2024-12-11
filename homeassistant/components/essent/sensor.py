"""Sensor to fetch dynamic prices from Essent API."""

from __future__ import annotations

import json
import logging

import requests

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

_LOGGER = logging.getLogger(__name__)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""
    # pass the api url to the class to make api call
    add_entities([EssentDynamicPricing("")])


class EssentDynamicPricing(SensorEntity):
    """Representation of Essent Dynamic Pricing API Section."""

    _LOGGER.info("Essent Dynamic Pricing Entity is being added to the entities")

    def get_dynamic_price(self, api):
        """Set the function on the fire."""
        api_response = requests.get(f"{api}", timeout=5)
        if api_response.status_code == 200:
            self.formatted_print(api_response.json())

    def formatted_print(self, obj):
        """Set the function on the fire."""
        json.dumps(obj, sort_keys=True, indent=4)

    def __init__(self, api):
        """Set the function on the fire."""
        self.get_dynamic_price(api)
