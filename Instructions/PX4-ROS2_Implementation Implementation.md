
# PX4-ROS2_Implementation

## In order to create and run the model of the Dodecacopter in Gazebo Simulation, follow the steps below:

1. Clone the PX4 Autopilot repository https://github.com/PX4/PX4-Autopilot into your local system.

2. Go to the SDP project folder ss24-dodecacopter-dynamics-simulation/PX4_files/ and download all the following files:
-	gps (folder containing .sdf and model.config files)
-	mku25 (folder containing drone’s 3D meshes, .sdf and model.config files)
-	22001_gazebo-classic_mku25
-	CMakeLists.txt
-	my_vehicle.world
-	sitl_targets_gazebo-classic.cmake

These are the files that will be required to set up PX4 SITL Simulation. 

3. We will now copy each of these files into necessary paths in the PX4 directory:

-	Navigate to the PX4 firmware directory in your local system.
-	Copy both the folders ‘gps’ and ‘mku25’ from above and paste them in the PX4 directory /PX4-Autopilot/Tools/simulation/gazebo-classic/sitl_gazebo-classic/models/.
-	Copy ‘my_vehicle.world’ file and paste it into the directory /PX4-Autopilot/Tools/simulation/gazebo-classic/sitl_gazebo-classic/worlds/.
-	Copy ‘22001_gazebo-classic_mku25’ file and paste it into the directory /PX4-Autopilot/ROMFS/px4fmu_common/init.d-posix/airframe/. Make sure the number assigned to the new airframe file (in this case, 22001) is a unique number in that folder. This airframe file is a default config file which contains the physical configuration of the system (e.g. a plane, wing or multicopter), geometry and airframe-specific parameter settings, including tuning gains and it basically starts the controllers and land detectors, etc.
-	Add the new airframe file name in the file /PX4-Autopilot/ROMFS/px4fmu_common/init.d-posix/airframes/CMakeLists.txt or simply replace the existing ‘CMakeLists.txt’ with the downloaded one from above SDP project folder.
-	Replace the file ‘sitl_targets_gazebo-classic.cmake’ in the directory /PX4-Autopilot/src/modules/simulation/simulator_mavlink/ with the new downloaded one from the SDP Project folder. In this file, we have updated the ‘command set(models ...)’ by adding the two new model names - ‘gps’ and ‘mku25’, and updated ‘command set(worlds ...)’ by adding the new world file name ‘my_vehicle’. This step ensures that our custom models are recognized and included as an available model when running PX4 SITL simulations.
-	Ensure that all the PX4 files from the SDP project folder are successfully added in the required locations in the PX4 firmware directory.

4. Now we mode to the installation part of thq QGroundControl Software:

-	Follow the installation instructions in its official website https://docs.qgroundcontrol.com/master/en/qgc-user-guide/getting_started/download_and_install.html
-	Ensure that the ‘Gazebo simulator’ is installed in your system. If not, follow the installation instructions from the website https://classic.gazebosim.org/tutorials?tut=install_ubuntu
-	Now navigate back to the root directory /PX4-Autopilot/ and open the terminal there.
-	Run the command in the terminal: PX4_NO_FOLLOW_MODE=1 make px4_sitl gazebo-classic_mku25 . This command will automatically open the Gazebo and the drone model should be automatically imported to the gazebo world.
-	Run the QGroundControl software at the same time and wait for the message “Ready for takeoff!” in the terminal.
-	As it as the message appears, enter the command: commander takeoff
-	Now we can see the drone is armed in the QGC software, i.e., it will soon be in flight mode. In Gazebo, we can see the rotors of the drone start rotating and soon the drone takes off and hovers at an altitude of 7-9 ft.

5. To ensure that the drone is stable in the Gazebo simulation environment the following steps need to be done: 

-	You can fine-tune the PID settings in the QGC to make the drone stable during takeoff and hovering. Follow the documentation to edit the PID settings in the Vehicle Setup: https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter_basic.html
- We used the following PID values for rate controller, altitude controller, velocity controller and position controller to fine tune our model:

-	MC_ROLLRATE_K: 1.9000
-	MC_ROLLRATE_D: 0.0024
-	MC_ROLLRATE_I: 0.125
-	MC_PITCHRATE_K: 2.1000
-	MC_PITCHRATE_D: 0.0032
-	MC_PITCHRATE_I: 0.150
-	MC_YAWRATE_K: 1.7000
-	MC_YAWRATE_I: 0.060
-	MC_ROLL_P: 9.50
-	MC_PITCH_P: 6.50
-	MC_YAW_P: 2.80
-	MPC_XY_VEL_P_ACC: 1.80
-	MPC_XY_VEL_I_ACC: 0.40
-	MPC_XY_VEL_D_ACC: 0.20
-	MPC_Z_VEL_P_ACC: 4.00
-	MPC_Z_VEL_I_ACC: 2.00
-	MPC_Z_VEL_D_ACC: 0.00
-	MPC_XY_P: 0.95
-	MPC_Z_P: 1.00

6. In the QGRoundControl software it is possible to also set a mission in which the drone gets launched and travels a predefined trajectory. There is a detailed tutorial for this in youtube: https://youtu.be/Oj-ZSt0F-q4?si=scpeR2uDBaF_vywU


## To integrate ROS 2 with the PX4 to run the model in the Gazebo simulation environment,  you need to do the following:

1. Follow the documentation and user guide to set up ROS 2 for PX4 in https://docs.px4.io/main/en/ros2/
2. Ensure ROS 2 Humble is installed in your system. If you are using Ubuntu version 20, then install ROS 2 Foxy, as Humble is for higher versions like Ubuntu 22.
3. Open a terminal and execute the following commands to install ROS 2 Humble:

- sudo apt update && sudo apt install locales
- sudo locale-gen en_US en_US.UTF-8
- sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
- export LANG=en_US.UTF-8
- sudo apt install software-properties-common
- sudo add-apt-repository universe
- sudo apt update && sudo apt install curl -y
- sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
- echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
- sudo apt update && sudo apt upgrade -y
- sudo apt install ros-humble-desktop
- sudo apt install python3-colcon-common-extensions
- source /opt/ros/humble/setup.bash
- echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

4. Next, we need a Micro XRCE-DDS Agent which facilitates communication between ROS 2 and PX4 using the XRCE-DDS protocol. Install and run the Micro XRCE-DDS Agent:

- git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
- cd Micro-XRCE-DDS-Agent
- mkdir build && cd build
- cmake ..
- make
- sudo make install
- sudo ldconfig /usr/local/lib/
- MicroXRCEAgent udp4 -p 8888

5.The agent is now running, but you won't see much until we start PX4. You can leave the agent running in this terminal! Note that only one agent is allowed per connection channel.

6.Build the ROS 2 Workspace and clone necessary packages:
- mkdir -p ~/ros2_px4_ws/src
- cd ~/ros2_px4_ws/src
- git clone https://github.com/PX4/px4_msgs.git
- git clone https://github.com/PX4/px4_ros_com.git
- cd ..
- source /opt/ros/humble/setup.bash
- colcon build
- chmod +x install/local_setup.bash
- source install/local_setup.bash

7. Once the setup script has been successfully sourced, check to ensure that your ROS 2 environment is configured correctly by using the command ros2 topic list. This command should display a list of available ROS 2 topics if everything is set up properly. If PX4 is connected to the agent, the result will be below list of topic:


$ ros2 topic list
/fmu/in/actuator_motors
/fmu/in/actuator_servos
/fmu/in/arming_check_reply
/fmu/in/aux_global_position
/fmu/in/config_control_setpoints
/fmu/in/config_overrides_request
/fmu/in/differential_drive_setpoint
/fmu/in/goto_setpoint
/fmu/in/manual_control_input
/fmu/in/message_format_request
/fmu/in/mode_completed
/fmu/in/obstacle_distance
/fmu/in/offboard_control_mode
/fmu/in/onboard_computer_status
/fmu/in/register_ext_component_request
/fmu/in/sensor_optical_flow
/fmu/in/telemetry_status
/fmu/in/trajectory_setpoint
/fmu/in/unregister_ext_component
/fmu/in/vehicle_attitude_setpoint
/fmu/in/vehicle_command
/fmu/in/vehicle_command_mode_executor
/fmu/in/vehicle_mocap_odometry
/fmu/in/vehicle_rates_setpoint
/fmu/in/vehicle_thrust_setpoint
/fmu/in/vehicle_torque_setpoint
/fmu/in/vehicle_trajectory_bezier
/fmu/in/vehicle_trajectory_waypoint
/fmu/in/vehicle_visual_odometry
/fmu/out/battery_status
/fmu/out/estimator_status_flags
/fmu/out/failsafe_flags
/fmu/out/manual_control_setpoint
/fmu/out/mode_completed
/fmu/out/position_setpoint_triplet
/fmu/out/sensor_combined
/fmu/out/timesync_status
/fmu/out/vehicle_attitude
/fmu/out/vehicle_command_ack
/fmu/out/vehicle_control_mode
/fmu/out/vehicle_global_position
/fmu/out/vehicle_gps_position
/fmu/out/vehicle_local_position
/fmu/out/vehicle_odometry
/fmu/out/vehicle_status
/parameter_events
/rosout

Note that the workspace does not need to build with px4_msgs for this to succeed; topic type information is part of the message payload.

8.	Use the command ros2 topic echo to show the details of a particular topic. Unlike with ros2 topic list, for this to work you must be in a workspace that has built the px4_msgs and sourced local_setup.bash so that ROS can interpret the messages. For example, the command ros2 topic echo /fmu/out/sensor_combined will echo the following topic details as they update:
---
timestamp: 1726471999775514
gyro_rad:
- -0.009587380103766918
- -0.0023968429304659367
- -0.0005326343234628439
gyro_integral_dt: 4000
accelerometer_timestamp_relative: 0
accelerometer_m_s2:
- -0.18674775958061218
- 0.0742204338312149
- -9.659406661987305
accelerometer_integral_dt: 4000
accelerometer_clipping: 0
gyro_clipping: 0
accel_calibration_count: 0
gyro_calibration_count: 1
---
9.	Launch ROS 2 Nodes that interact with PX4 (make sure the MicroXRCEAgent is running):
- ros2 launch px4_ros_com sensor_combined_listener.launch.py

11.	In a new terminal, ensure the ROS environment variables are sourced and start the PX4 simulation:
- cd ~/PX4-Autopilot
- source ~/ros2_px4_ws/install/local_setup.bash
- make px4_sitl gazebo-classic_mku25
  
11.	To summarize the list of commands to run the model and interact with ros 2 nodes:

- Source ros2 humble/foxy and also source ros2 workspace install/local_setup.bash in all 3 terminals.
- In the 1st terminal, run the command: MicroXRCEAgent udp4 -p 8888
- In the 2nd terminal, run the command : ros2 launch px4_ros_com sensor_combined_listener.launch.py
- In the 3rd terminal, run the command: PX4_NO_FOLLOW_MODE=1 make px4_sitl gazebo-classic_mku25

12.	This setup initiates communication between PX4 and a ROS 2 workspace. ROS 2 nodes can now send commands to PX4 or subscribe to PX4 topics, facilitating complex simulations and controls within the Gazebo environment.

13.	For testing, you can use the mission plan in the Project repository: https://github.com/HBRS-SDP/ss24-dodecacopter-dynamics-simulation/blob/main/test/mission.plan. Upload this file directly in the QGC to set up a mission and travel a straight path.

	This was all about running the Dodecacopter model using QGC software.
