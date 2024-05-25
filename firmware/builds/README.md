# Pi Pico Firmware

## Customizing and Compiling the Firmware

To customize the firmware, files from the `Firmware/code` folder need to be compiled in. Use the `manifest.py` file in the same folder for this purpose. The relevant section from `manifest.py` looks like this:

```python
include("$(PORT_DIR)/boards/manifest.py")

#******* Code needed for EInk *******
module("icons.py")
module("driver.py")
module("tiles.py")
package("apis")
package("picozero")
#************************************

require("bundle-networking")

# Bluetooth
require("aioble")
```

Follow the instructions in the [MicroPython GitHub repository](https://github.com/micropython/micropython/tree/master/ports/rp2) to compile the firmware.

## Installing the Firmware

To install the firmware on the Pico, follow these steps:

1. Hold down the `BOOTSEL` button on the Pico while connecting it to your computer.
2. Drag and drop the `firmware.uf2` file into the displayed drive.

## Using Precompiled Builds

If no significant changes have been made to the code, you can use the precompiled builds available in the `Firmware/builds` folder.

