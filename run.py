import pyupm_grove

import lightbulb

# This is custom user configuration
TEMP_SENSOR_A_PIN = 0
LIGHT_SENSOR_A_PIN = 3
lightbulb.sensors.register(pyupm_grove.GroveTemp(TEMP_SENSOR_A_PIN))
lightbulb.sensors.register(pyupm_grove.GroveLight(LIGHT_SENSOR_A_PIN))

# Launch Flask
lightbulb.app.run(host='0.0.0.0', debug=True)
