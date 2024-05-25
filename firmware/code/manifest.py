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
