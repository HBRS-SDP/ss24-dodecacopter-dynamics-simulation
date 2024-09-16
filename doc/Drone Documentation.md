# Documentation for the Multi-Rotor Drone SDF File
This document provides an in-depth explanation of the elements and parameters used in the SDF (Simulation Description Format) file for a multi-rotor Dodecacopter model named **mku25**. The SDF file is crucial for simulating the drone in Gazebo, and includes definitions for physical properties, geometry, joints, links and sensor plugins.
-  In the SDF file, the <model> element defines the drone's structure, consisting of several important components such as links, joints, collisions, visuals, and plugins.
-  Links represent the physical parts of the drone. Each link has attributes like pose, inertia, mass, collision geometry, and visual representation.
-  <pose>0 0 0 0 0 0</pose> defines the position and orientation (x, y, z, roll, pitch, yaw) of the base link, imu link and rotor links.
-  <mass> specifies mass of the drone (37.8 kg).
-  <inertia> describes resistance to rotational acceleration with parameters like ixx, ixy, ixz, iyy, iyz, and izz.
-  <visual> defines the 3D model for the links.
-  <geometry> refers to a mesh file (mku25.stl) scaled down by a factor of 0.001 in all axes.
-  <collision> describes the physical boundaries for simulation. The entire model has uses a single collision instead of several collisions for individual parts as this slows down import of the model in Gazebo.
-  The imu link has a low mass (0.015 kg) and very small inertia values (1e-05), indicating it has minimal effect on the drone's dynamics.
<gravity> is set to true, meaning it is affected by gravity.
-  The rotors are defined as separate links attached to the base_link via revolute joints. Each rotor has its own mass, collision geometry, visual representation, and motion control. 
Rotors 0, 1, 2, ... 11 represent the rotors of the drone, having a small mass (0.175 kg) and low inertia values to simulate the lightweight nature of the rotor.
-  The 3D model for visualization is defined in mesh files (ccw.stl for counter-clockwise and cw.stl for clockwise turning rotors).
-  The rotors rotate around the z-axis and the rotation limits are set extremely high to allow free spinning.
-  The drone is equipped with several plugins that simulate its behavior, including motors, sensors, and communication interfaces.
-  Each rotor has a motor model plugin that controls its behavior.
-  File ‘libgazebo_motor_model.so’ is a shared object file containing the motor model logic.
-  Below are the parameters used in the motor plugin files:
1. turningDirection: Specifies the rotor's direction, either ccw (counterclockwise) or cw (clockwise).
2.Time Constants: timeConstantUp (0.0125) and timeConstantDown (0.025) define how quickly the motor reaches its target speed.
3. Max Rotational Velocity: Set to 3000 for each rotor.
4. Motor Number: Unique identifier for each rotor.
5. Command Topics: Motor speed is controlled via a ROS topic (/gazebo/command/motor_speed).
-  The drone uses a range of sensor plugins:
1. IMU Plugin (libgazebo_imu_plugin.so): Publishes IMU data (gyroscope and accelerometer) to the /imu topic with noise parameters for realistic simulation.
2. Magnetometer Plugin (libgazebo_magnetometer_plugin.so): Simulates the magnetometer sensor with a noise model, publishing to /mag at 100 Hz.
3. Barometer Plugin (libgazebo_barometer_plugin.so): Simulates atmospheric pressure data, publishing to /baro at 50 Hz.
-  Communication and control plugins:
1. MAVLink Interface (libgazebo_mavlink_interface.so): Interfaces with the MAVLink protocol, controlling motor speeds and receiving sensor data over UDP and TCP ports.
2. Motor Speed Command: Sent through /gazebo/command/motor_speed.
3. Control Channels: Each rotor is assigned a control channel that specifies the scaling and behavior of motor control.

# Links:

-  Details about the motor model **KV120** of the drone can be found in: https://store.tmotor.com/product/mn805-s-kv120-motor-navigator-type.html
-  All the plugin parameters are calculated from the github notes and discussions: https://github.com/mvernacc/gazebo_motor_model_docs/blob/master/notes.pdf and https://github.com/PX4/PX4-SITL_gazebo-classic/issues/110
-  Please note that there are no proper validated documentations or source code for above calculations of parameter values, all the example models in the PX4 use iris model as the base (https://github.com/PX4/PX4-SITL_gazebo-classic/tree/67431d233f0f08de647f0eb11239816f9c8bd6c6/models/iris).
-  The airframe reference is taken from https://docs.px4.io/v1.13/en/airframes/airframe_reference.html
-  Details about the rotor of the drone can be found in https://uav-en.tmotor.com/html/2018/navigato_0402/46.html
-  Details about the propellers of the drone can be found in https://www.mad-motor.com/collections/propellers
-  The 3D model of the drone was created in Inventor. Please check the following link for the STL files and the 3D model of the drone: https://drive.google.com/file/d/1KSn984cVOkgP_WAqGt8mQ50ABie2zR--/view?usp=sharing
