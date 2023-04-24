# Jikken

An open/free-to-do whatever 65% handwired keyboard project.

## Specs:
* Mount Style : Top Mount
* Typing Angle : 2 Degrees
* Front Type Height : 21.4mm
* Dimensions : 319.5mm x 110.3mm

## Layouts:
![Layouts](https://github.com/Arko9699/trijoy65/blob/main/Resources/Layouts.png?raw=true)

## Render:
![Render](https://github.com/Arko9699/trijoy65/blob/main/Resources/explosion.png?raw=true)
![Fusion](https://github.com/Arko9699/trijoy65/blob/main/Resources/fusion.png?raw=true)

## Materials Required:

All STL files were printed in PLA at 90% infill. You may also use ABS.

*You may choose either Tsangan or Standard for your plate, every other part is the same.*

* 1x Waveshare RP2040 Zero (my MCU of choice for this build, you are free to choose your own but you need to edit the Bottom Case)
* MX key switches (66 for Tsangan, 67 for Standard)
* 1N4148 diodes (66 for Tsangan, 67 for Standard)
* Plate Mount Stabilisers (3 x 2u + 1 x 6.25u for Standard/7u for Tsangan) 
* 4x M2x5 Screws
* 7x M2x12 Screws
* 7x M2 threaded inserts (you can try screwing into the bare plastic but its not recommended)
* Soldering Tools

## Firmware:

1. Download the contents of the repo for the files.
2. Get your MCU ready for KMK by following ![this](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Getting_Started.md).
3. If your MCU is supported and working, congrats! Now you can copy over the files in the KMK folder to the root of the CIRCUITPY drive.
4. Be sure to test drive your keyboard before soldering all the wires to the MCU.
