"""Constants for the victron_mqtt integration."""
DOMAIN = "victron_mqtt_ongas"

CONF_INSTALLATION_ID = "installation_id"
CONF_MODEL = "model"
CONF_SERIAL = "serial"
CONF_ROOT_TOPIC_PREFIX = "root_topic_prefix"
CONF_UPDATE_FREQUENCY_SECONDS = "update_frequency"
CONF_OPERATION_MODE = "operation_mode"
CONF_EXCLUDED_DEVICES = "excluded_devices"

DEVICE_MESSAGE = "device"
SENSOR_MESSAGE = "sensor"

DEFAULT_HOST = "venus.local."
DEFAULT_PORT = 1883
DEFAULT_UPDATE_FREQUENCY_SECONDS = 30

# Service names
SERVICE_PUBLISH = "publish"

# Service data attributes
ATTR_METRIC_ID = "metric_id"
ATTR_DEVICE_ID = "device_id"
ATTR_VALUE = "value"

SYSTEM_STATE_MAPPING = {
    "Float": "Float charging",
    "Bulk": "Bulk charging",
    "Absorption": "Absorption charging",
    "Equalize": "Equalize charging",
    "Storage": "Storage mode",
    "Discharged": "Discharged",
    "Fault": "Fault",
    "Inverting": "Inverting",
    "PowerAssist": "PowerAssist",
    "Bypass": "Bypass",
    "Off": "Off",
    "Starting": "Starting",
    "Deactivated": "Deactivated",
    "LowPower": "Low Power",
    "ExternalControl": "External Control",
}

VEBUS_INVERTER_STATE_MAPPING = {
    "Off": "Off",
    "LowPower": "Low Power",
    "Fault": "Fault",
    "Bulk": "Bulk charging",
    "Absorption": "Absorption charging",
    "Float": "Float charging",
    "Storage": "Storage mode",
    "RepeatAbs": "Repeat Absorption",
    "Equalize": "Equalize charging",
    "Passthru": "Passthru",
    "Inverting": "Inverting",
    "PowerAssist": "PowerAssist",
    "Bypass": "Bypass",
    "Charge": "Charge",
    "Discharge": "Discharge",
}
