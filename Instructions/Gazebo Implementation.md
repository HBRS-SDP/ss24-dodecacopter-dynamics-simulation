
In order to create and run the model of the Dodecacopter in Gazebo Simulation, follow the steps below:

1. Clone the PX4 Autopilot repository https://github.com/PX4/PX4-Autopilot into your local system.
2. Go to the SDP project folder ss24-dodecacopter-dynamics-simulation/PX4_files/ and download all the following files:
-	gps (folder containing .sdf and model.config files)
-	mku25 (folder containing drone’s 3D meshes, .sdf and model.config files)
-	22001_gazebo-classic_mku25
-	CMakeLists.txt
-	my_vehicle.world
-	sitl_targets_gazebo-classic.cmake

These are the files that will be required to set up PX4 SITL Simulation. 

We will now copy each of these files into necessary paths in the PX4 directory:

-	Navigate to the PX4 firmware directory in your local system.
-	Copy both the folders ‘gps’ and ‘mku25’ from above and paste them in the PX4 directory /PX4-Autopilot/Tools/simulation/gazebo-classic/sitl_gazebo-classic/models/.
-	Copy ‘my_vehicle.world’ file and paste it into the directory /PX4-Autopilot/Tools/simulation/gazebo-classic/sitl_gazebo-classic/worlds/.
-	Copy ‘22001_gazebo-classic_mku25’ file and paste it into the directory /PX4-Autopilot/ROMFS/px4fmu_common/init.d-posix/airframe/. Make sure the number assigned to the new airframe file (in this case, 22001) is a unique number in that folder. This airframe file is a default config file which contains the physical configuration of the system (e.g. a plane, wing or multicopter), geometry and airframe-specific parameter settings, including tuning gains and it basically starts the controllers and land detectors, etc.
-	Add the new airframe file name in the file /PX4-Autopilot/ROMFS/px4fmu_common/init.d-posix/airframes/CMakeLists.txt or simply replace the existing ‘CMakeLists.txt’ with the downloaded one from above SDP project folder.
-	Replace the file ‘sitl_targets_gazebo-classic.cmake’ in the directory /PX4-Autopilot/src/modules/simulation/simulator_mavlink/ with the new downloaded one from the SDP Project folder. In this file, we have updated the ‘command set(models ...)’ by adding the two new model names - ‘gps’ and ‘mku25’, and updated ‘command set(worlds ...)’ by adding the new world file name ‘my_vehicle’. This step ensures that our custom models are recognized and included as an available model when running PX4 SITL simulations.
-	Ensure that all the PX4 files from the SDP project folder are successfully added in the required locations in the PX4 firmware directory.
-	Now download and install the QGroundControl software in your system. Follow the installation instructions in its official website https://docs.qgroundcontrol.com/master/en/qgc-user-guide/getting_started/download_and_install.html
-	Ensure the ‘Gazebo simulator’ is installed in your system. If not, follow the installation instructions from the website https://classic.gazebosim.org/tutorials?tut=install_ubuntu
-	Now navigate back to the root directory /PX4-Autopilot/ and open the terminal there.
-	Run the command in the terminal: PX4_NO_FOLLOW_MODE=1 make px4_sitl gazebo-classic_mku25 .

This command will automatically open the Gazebo and the drone model should be automatically imported to the gazebo world.

●	Run the QGroundControl software at the same time and wait for the message “Ready for takeoff!” in the terminal.
●	As it as the message appears, enter the command: commander takeoff
●	Now we can see the drone is armed in the QGC software, i.e., it will soon be in flight mode. In Gazebo, we can see the rotors of the drone start rotating and soon the drone takes off and hovers at an altitude of 7-9 ft.
●	You can fine-tune the PID settings in the QGC to make the drone stable during takeoff and hovering. Follow the documentation to edit the PID settings in the Vehicle Setup: https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter_basic.html
●	We used the following PID values for rate controller, altitude controller, velocity controller and position controller to fine tune our model:
○	MC_ROLLRATE_K: 1.9000
○	MC_ROLLRATE_D: 0.0024
○	MC_ROLLRATE_I: 0.125
○	MC_PITCHRATE_K: 2.1000
○	MC_PITCHRATE_D: 0.0032
○	MC_PITCHRATE_I: 0.150
○	MC_YAWRATE_K: 1.7000
○	MC_YAWRATE_I: 0.060
○	MC_ROLL_P: 9.50
○	MC_PITCH_P: 6.50
○	MC_YAW_P: 2.80
○	MPC_XY_VEL_P_ACC: 1.80
○	MPC_XY_VEL_I_ACC: 0.40
○	MPC_XY_VEL_D_ACC: 0.20
○	MPC_Z_VEL_P_ACC: 4.00
○	MPC_Z_VEL_I_ACC: 2.00
○	MPC_Z_VEL_D_ACC: 0.00
○	MPC_XY_P: 0.95
○	MPC_Z_P: 1.00

●	We can also set a mission in which the drone gets launched and travels a predefined trajectory. There is a detailed tutorial for this in youtube: https://youtu.be/Oj-ZSt0F-q4?si=scpeR2uDBaF_vywU

●	For testing, you can use the mission plan in the Project repository: https://github.com/HBRS-SDP/ss24-dodecacopter-dynamics-simulation/blob/main/test/mission.plan. Upload this file directly in the QGC to set up a mission and travel a straight path.

●	This was all about running the Dodecacopter model using QGC software.
