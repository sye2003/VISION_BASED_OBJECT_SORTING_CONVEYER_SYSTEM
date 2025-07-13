
# 📦 Project Title: **Color-Based Object Sorting Conveyor System**

## 🧠 Overview

This project is a **real-time object sorting system** that uses **computer vision** to detect the **color of objects** moving on a conveyor and triggers a **servo motor** to divert each object to its respective path. It's designed to mimic the type of automation used in manufacturing, packaging, and recycling industries.

## 🎯 Objective

To build an intelligent conveyor system using:
- A webcam for live object detection
- OpenCV (Python) for color recognition
- Arduino/ESP32 to control servos
- Servo motors to physically sort objects based on their color

## 🔧 Technologies Used

| Component          | Tool/Language            |
|-------------------|--------------------------|
| Color Detection    | Python, OpenCV           |
| Communication      | PySerial (Serial over USB) |
| Control Unit       | Arduino Uno / ESP32      |
| Actuation          | Servo motors (SG90/MG996R etc.) |
| Platform           | Windows (but portable to Linux/Mac) |

## 🖼️ System Architecture

```
           [Webcam]
              ↓
      [Python + OpenCV]
    ┌───────────────────────┐
    │  Detect color (R/G/B/Y)│
    └────────┬──────────────┘
             ↓
    [Send command via Serial]
             ↓
       [Arduino/ESP32]
             ↓
    [Move corresponding servo]
             ↓
[Divert object to right container]
```

## 💻 How It Works

1. A **webcam** continuously captures frames of the conveyor belt.
2. Each object that appears is analyzed in real-time using **OpenCV**.
3. The system detects whether the object is **red**, **green**, **blue**, or **yellow** based on **HSV color masking**.
4. Once detected, a **serial command** ('R', 'G', 'B', or 'Y') is sent to the **Arduino**.
5. The Arduino receives the character and triggers the corresponding **servo motor** to move briefly and push the object into the correct bin.
6. The servo then resets to its default position, ready for the next object.

## 📂 Folder Structure

```
object-sorting-conveyor/
│
├── color_sorter.py           # Python script for color detection + serial communication
├── arduino_code.ino          # Arduino code to control servos
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── media/                    # Images or demo videos (optional)
```

## 🛠️ Hardware Requirements

- Arduino Uno / ESP32
- Webcam (laptop or USB)
- 4x Servo Motors (SG90 or stronger)
- Jumper wires
- External 5V power supply for servos
- Breadboard or custom PCB
- Conveyor belt (can be improvised using motor + rollers)

## 📦 Software Requirements

```bash
pip install opencv-python pyserial numpy
```

## 🧪 Test Steps

1. Upload the Arduino sketch to your board using Arduino IDE.
2. Ensure the correct COM port is selected in Python (`COM3`, `COM4`, etc.).
3. Run the Python script:
```bash
python color_sorter.py
```
4. Place colored objects (e.g., red, blue, green, yellow) in front of the webcam.
5. Observe each object being detected and the corresponding servo activating.

## 📽️ Demo (optional)

> *Insert a GIF or YouTube link showing the system in action.*

## 📈 Future Improvements

- Add object **shape detection** (Phase 2)
- Add **machine learning** to detect logos or printed objects
- Use **YOLO** or **TensorFlow Lite** for real object classification
- Add a GUI for monitoring/logging color counts
- Add **wireless ESP32 communication (WiFi/Bluetooth)**

## 👨‍💻 Made By

> Syed Abudahir  
> B.E. Electronics and Communication Engineering  
> [LinkedIn](https://www.linkedin.com/in/syed-abudahir-a-44b076237/) | [GitHub](https://github.com/sye2003)
