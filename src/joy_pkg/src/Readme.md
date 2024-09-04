# Serial port to ROS Joy node Publisher

This project reads data from a serial port, processes it, and publishes it as a ROS `Joy` message.

## Prerequisites

Ensure you have the following installed:

- Python 3.8
- ROS (Robot Operating System)      
- `pyserial` for serial communication
- `numpy` for numerical processing

## Installation

1. **Install ROS**: Follow the official ROS installation guide for your operating system. You can 
use the following command for one line installation!
    ```bash 
    wget -c https://raw.githubusercontent.com/qboticslabs/ros_install_noetic/master/ros_install_noetic.sh && chmod +x ./ros_install_noetic.sh && ./ros_install_noetic.sh
    ```
2. **Set up a ROS Workspace**:
    ```bash
    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/
    catkin_make
    source devel/setup.bash
    ```
    Sets up the base ROS environment for your system by adding the following
    to your .bashrc or .zshrc
    ```bash
    source /opt/ros/src/setup.bash
    ```
3. **Install Python Dependencies**:
    ```bash
    pip install pyserial numpy
    ```

## Code Overview

- **CRC16 Calculation**: Computes the CRC16 checksum for data validation.
- **Initializer**: Prepares the initializer message for communication.
- **JoyPublisher**: Publishes the joystick data to the ROS topic `/joy`.
- **SerialReader**: Handles reading from the serial port and data processing.

## Running the Code

1. **Start ROS Core**:
    ```bash
    roscore
    ```

2. **Run the ROS Node**:
    `joy_pkg` contains our publisher ROS node. Run the following code on a new terminal to start the publisher:
    ```bash
    rosrun joy_pkg S_R_3_8.py
    ```

3. **Verify Data on Topic**:
    Use the following command on a new terminal to check if data is being published to the `/joy` topic:
    ```bash
    rostopic echo /joy
    ```

## Troubleshooting

- Ensure the serial device path (`/dev/ttyACM0`) is correct and the device has appropriate permissions.
- Use `rostopic list` to see available topics and ensure `/joy` is listed.
- Check terminal logs for any errors or warnings.
