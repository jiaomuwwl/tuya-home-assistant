# Tuya Home Assistant Integration

<p align="center">
    <img src="https://images.tuyacn.com/app/hass/ha_tuya.png" width="70%">
</p>

Tuya Home Assistant integration is developed for controlling **Powered by Tuya (PBT)** devices using [Tuya Open API](https://developer.tuya.com/en/docs/cloud/?_source=github), officially maintained by the Tuya Developer Team.

## Supported Tuya Device Types

The following Tuya Device types are currently supported by this integration:

- [Light](https://github.com/tuya/tuya-home-assistant/blob/master/custom_components/tuya/light.py): Supports Tuya Wi-Fi light devices.
- [Switch](https://github.com/tuya/tuya-home-assistant/blob/master/custom_components/tuya/switch.py): Supports Tuya Wi-Fi switch devices, like switch, socket and power strip
- [Cover](https://github.com/tuya/tuya-home-assistant/blob/master/custom_components/tuya/cover.py): Supports Tuya cover devices like smart curtain motor.
- [Climate](https://github.com/tuya/tuya-home-assistant/blob/master/custom_components/tuya/climate.py): Supports Tuya climate devices like air conditioner and heater.
- [Fan](https://github.com/tuya/tuya-home-assistant/blob/master/custom_components/tuya/fan.py): Support Tuya fan devices.

Please check the [Develop Tuya-Compatible Home Assistant Drivers](https://developer.tuya.com/en/demo/devhomeassistantplugin/?_source=github) and [Home Assistant Entity](https://developers.home-assistant.io/docs/core/entity) tutorials to develop more drivers for the Tuya Home Assistant Integration and support more Tuya devices.

## Workflow

<img src="https://images.tuyacn.com/app/hass/hass_diagram1.png" width="60%"/> <img src="https://images.tuyacn.com/app/hass/workflow.png" width="35%" />

## Sequence Diagram

<img src="https://airtake-public-data-1254153901.cos.ap-shanghai.myqcloud.com/content-platform/hestia/16194063817c985ee4c2f.png" width="60%" />

## Installation

### 1. Home Assistant Installation

Please refer to the [Home Assistant Official Installation](https://www.home-assistant.io/installation/) documentation to install **Home Assistant Core**.

You can also get help from [Set up Home Assistant Development Environment on Raspberry Pi](https://developer.tuya.com/en/demo/setuphomeassistantdevenv/?_source=github) in Tuya Developer Demo Center.

### 2. Tuya Home Assistant Integration Installation

There are two methods to install the integration:

1. Home Assistant Custom Components Installation
2. Install by [HACS](https://hacs.xyz/)

#### 2.1 Home Assistant Custom Components Installation

Download this tuya-home-assistant repo, unzip it, and copy the **custom_components/tuya/** folder to the HomeAssistant configuration directory, e.g. ~/.homeassistant

<img src="https://airtake-public-data-1254153901.cos.ap-shanghai.myqcloud.com/content-platform/hestia/1619406706bb7cb5eb66b.png" height="300" />

#### 2.2 Install by HACS

**1.** [HACS Install](https://hacs.xyz/docs/installation/installation/)

**2.** [HACS Initial Configuration](https://hacs.xyz/docs/configuration/basic)

**3.** HACS -> Integrations -> ... -> Custom repositories 

<img src="https://images.tuyacn.com/app/hass/hacs_install_custom.png" width="90%" />

**4.** Input the tuya-home-assistant GitHub URL: **https://github.com/tuya/tuya-home-assistant** and select **Integration** as the Category type,  then click **ADD**.

<img src="https://images.tuyacn.com/app/hass/custom_repos.png" width="70%" />

**5.** Click **INSTALL**

<img src="https://images.tuyacn.com/app/hass/hacs_tuya_install.png" width="90%" />

#### 2.3 Restart Home Assistant

Configuration -> Server Controls -> RESTART

#### 2.4 Activate Tuya Integration

Configuration -> Integrations -> ADD INTEGRATION -> Tuya Integration

<img src="https://images.tuyacn.com/app/hass/hacs_tuya_setup.png" width="90%" />

### 3. Enter your Tuya credential

Please get the Tuya credential info by following the **Configure Cloud Development Project** part in [Tuya IoT Platform Configuration Guide](https://github.com/tuya/tuya-android-iot-app-sdk-sample/blob/activator_tool/Tuya_IoT_Platform_Configuration_Guide.md).

<img src="https://images.tuyacn.com/app/hass/hacs_tuya_credential.png" height="300"/>

## Start Home Assistant

Go to the home assistant installation folder `~/hass` and use the following command to activate it and run the hass service:

~~~
➜  hass source bin/activate
(hass) ➜  hass hass
~~~

<img src="https://images.tuyacn.com/app/hass/command_line.png" width="80%"/>

For more information, please refer to the [Home Assistant Core](https://www.home-assistant.io/installation/) tutorial for the startup process and run **hass**.

## Link Tuya Devices to Home Assistant

Please download and use the Tuya Smart or Tuya Smart Life apps to pair Tuya devices to the Home Assistant for controlling. You can check the following links to download the apps.

- Tuya Smart App: [iOS App](https://apps.apple.com/us/app/tuyasmart/id1034649547) | [Android App](https://play.google.com/store/apps/details?id=com.tuya.smart&hl=en_US&gl=US)
- Tuya Smart Life App: [iOS App](https://apps.apple.com/us/app/smart-life-smart-living/id1115101477) | [Android App](https://play.google.com/store/apps/details?id=com.tuya.smartlife&hl=en_US&gl=US)

## Contributing

Please refer to the [Contributing.md](./contributing.md) for contributing guide.

## Issue feedback
You can give feedback on issues you encounter via **GitHub Issue**.

## LICENSE
For more information, please refer to the [LICENSE](LICENSE) file
