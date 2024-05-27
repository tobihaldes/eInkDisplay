# 1. Main Components
## 1.1 E-Ink Display
- Model: WaveShare 7.5inch E-Paper E-Ink Display Module (B) for Raspberry Pi Pico
### Technical specifications:
- Size: 7.5 inch
- Resolution: 800x480 pixels
- Display colours: Red, black, white
- Grey scale: 2
- Interface: SPI (3-wire and 4-wire)
- Viewing angle: >170°
- Power consumption: Very low
- Special features: Passive reflective display panel, no blue light
- External dimensions: 170.2 x 111.2 mm
- Screen size: 163.2 x 97.92 mm
- Refresh times: Partial N/A, full 16 seconds
- Energy efficiency: Standby current <0.01uA
## 1.2 Microcontroller
- Model: Raspberry Pi RP-PICO-W
### Technical specifications:
- Microcontroller chip: RP2040
- Memory: 2 MB QSPI Flash, 256 KB RAM
- Connectors: Micro-USB, I/O pins, GPIO, PWM, SPI, I2C, UART
- Additional functions: ADC 12-bit, RTC/Timer, Serial Wire Debug (SWD)
- Operating voltage: 5V/DC
# 2. Additional Components
## 2.1 Power supply
- Battery holder: For 2x AA (Mignon) batteries, switchable and water-repellent
- Batteries: TecXus Alkaline Mignon AA
## 2.2 Connecting elements
- Stranded copper wire: 1-core, insulated, 1x0.14mm²
## 2.3 Switching components
- Short-stroke push-button: PCB mounting, vertical mounting, 12x12mm
## 2.4 Resistors
- Metal film resistors: 220.0 kOhm and 10.0 kOhm, 1/4W, ±1%, axial, through-hole mounting

## Circuit diagram
![Schaltung](https://github.com/tobihaldes/eInkDisplay/assets/165897037/0c34166b-3e30-4ae9-bccc-5798e1ae8a13)

Each button is connected to a ground (GND) line and has its own lead.
Each button's lead is connected to an LED and a resistor (330Ω and 680Ω) in series.
The LEDs indicates the state of the buttons.
The transistor controls the current flow through the LEDs. Its collector is connected to the LEDs and resistors, and its emitter is connected to the ground (GND).
The base of the transistor receives a control signal that switches the transistor on and off, allowing current to flow.

# 3. Housing: 
## Dimensions of the Housing

1. **Overall Size of the Housing:**
   - **Width:** 183.20 mm
   - **Height:** 165.00 mm
   - **Depth:** 40.00 mm

2. **Display Area:**
   - **External Dimensions of the Display:** 170.2 x 111.2 mm
   - **Screen Size:** 163.2 x 97.92 mm

3. **Frame Thickness:**
   - **Side Frame:** 2.00 mm
   - **Top Frame:** 10.00 mm

4. **Placement of Buttons:**
   - **Number of Buttons:** 3
   - **Spacing Between Buttons:** 13.00 mm
   - **Button Size:** 12 x 12 mm

5. **Depth of the Housing Wall:**
   - **Front Housing Depth:** 37.00 mm
   - **Rear Housing Depth:** 40.00 mm

6. **Cutout for Electronics (Raspberry Pi Pico W):**
   - **Length:** 165.00 mm
   - **Width:** 111.30 mm
   - **Height:** 24.00 mm
     
## General Shape and Structure of the Housing

The housing for the E-Ink display is rectangular and consists of several main components. It has a deep recess to securely hold the display while also providing space for the Raspberry Pi and associated electronic components. The front of the housing is dominated by the screen area, with a slim frame to maximize the visibility of the screen. Three control buttons are positioned below the display, evenly spaced to allow for easy operation. The housing has sufficient depth to accommodate the electronics, with no additional elements on the sides, ensuring a sleek profile. The back of the housing provides space for the power supply and wiring of the electronics. The rear panel is removable to facilitate access to the internal components. The bottom surface offers ample space for stable placement of the housing and is designed to accommodate the power supply components.

## Integration of the Display

The WaveShare 7.5-inch E-Paper E-Ink Display Module (B) is securely held within the frame of the housing. The precise fit ensures that the display does not shift and remains optimally visible. The frame has an opening that precisely matches the visible screen area of the E-Ink display.

## Modeling with Fusion 

Fusion was used for modeling the housing. Fusion 360 is a cloud-based 3D CAD, CAM, and CAE tool for product design and manufacturing. It combines industrial and mechanical design, simulation, collaboration, and machining.

## File of the technical drawing
**File:** [`E-Ink Display.stl`](/docs/hardware/E-InkDisplay.stl)


## Screenshots of the model from Fusion

### View from the front
![technische  Zeichnung 1](https://github.com/tobihaldes/eInkDisplay/assets/165897037/18eda6b2-b5e9-4e4c-a407-810895db2474)

### View from the side
![technische  Zeichnung 2](https://github.com/tobihaldes/eInkDisplay/assets/165897037/d330d66f-892e-457d-8619-909525831fe6)

### View from the top
![technische  Zeichnung 4](https://github.com/tobihaldes/eInkDisplay/assets/165897037/120c0774-c526-4197-8a61-b667ba4b9fed)

### Complete Model
![technische  Zeichnung 5](https://github.com/tobihaldes/eInkDisplay/assets/165897037/661e2cec-d8a2-4720-9125-cf7d0737470d)



