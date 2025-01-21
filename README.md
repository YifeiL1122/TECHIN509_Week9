
# Catan assistant

## Project Overview

This device enhances tabletop gameplay with a programmed dice point generation system and a dynamic LED display mechanism. Players can use it to generate random dice points, manage the thief's location, and display real-time plot information with corresponding output resources. The system integrates button controls, image recognition, and manual inputs to improve game efficiency and immersion.

### Features:

- Random dice point generation (2-12).
- Real-time updates based on the thief's location and plot distribution.
- Dynamic LED and screen display showing plot numbers and output resources.
- Image recognition to record plot arrangements at the start of the game.
- Powered by mains or lithium battery, with USB charging support.

### Hardwares:

- Microcontroller: ESP32 
- Rotary Encoder: KY-040
- Camera Module: OV7670
- LED Matrix: MAX7219-based 8x8
- TFT LCD Screen: 1.8" ST7735
- Power Supply
- Button

---

## Title Slide

### Description:

- This device streamlines board game interactions by dynamically generating dice points and indicating plot outputs. The centerpiece is a trigger button, complemented by a screen for displaying plot and output information.
- **Sketch:**
  - Central button for dice generation.
  - LED display showing dice points and plot data.
  - Rotatable wheel for manual input of the thief's location.

---

## Sensors and Inputs

### Random Number Generator (Dice Logic)

- **Purpose:** Generates random numbers between 2-12 for dice points.
- **Explanation:** Embedded program ensures equal probability for all outcomes.
- **Implementation:**
  - Microcontroller: ESP32 or Arduino Uno.
  - Logic: Use built-in `random()` or `randomSeed()` functions to ensure uniform distribution.

### Thief Location Wheel

- **Purpose:** Records the thief’s location manually.
- **Explanation:** Players flick the wheel to input the current thief's plot number.
- **Implementation:**
  - Rotary Encoder: KY-040 rotary encoder to capture rotational input.

### Image Recognition System

- **Purpose:** Captures and processes the arrangement of plots at the start of the game.
- **Explanation:** Uses a camera module to upload plot distribution and link it with numbers.
- **Implementation:**
  - Camera Module: OV7670 (low-cost CMOS camera).
  - Processing: Use TensorFlow Lite or OpenCV for image recognition.

---

## Display

### LED and Screen Mechanism

- **Purpose:** Displays dice points, plot numbers, and output resources dynamically.
- **Explanation:** LED indicators highlight affected plots, while the screen shows detailed game information.
- **Implementation:**
  - LED Matrix: MAX7219-based 8x8 LED matrix for plot indication.
  - Screen: 1.8" TFT LCD screen (ST7735) for detailed information.
