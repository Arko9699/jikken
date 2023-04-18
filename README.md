# icky66

Handwired Keyboard by yours truly. With inspiration from various other keyboards, I present my own (attempt at) fully 3DP mechanical keyboard.

![Render](https://github.com/Arko9699/trijoy65/blob/main/Resources/Exploded_View.png?raw=true)

## Materials Required

All STL files were printed in PLA at 90% infill. You may also use ABS.

* 1x Waveshare RP2040 Zero (my MCU of choice for this build, you are free to choose your own but you need to edit the Bottom Case)
* 66x MX key switches
* 66x 1N4148 diodes
* Soldering Tools
* 4x M2x5 Screws
* 7x M2x12 Screws
* 7x M2 threaded inserts (you can try screwing into the bare plastic but its not recommended)

## How to make your own

1. Download the contents of the repo for the files.
2. Get your MCU ready for KMK by following ![this](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Getting_Started.md).
3. If your MCU is supported and working, congrats! Now you can copy over the files in the KMK folder to the root of the CIRCUITPY drive.
4. Be sure to test drive your keyboard before solder all the wires to the MCU.
