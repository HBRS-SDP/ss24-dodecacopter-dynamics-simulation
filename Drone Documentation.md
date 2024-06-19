# Documentation:

# Important Features:

## Pose Coordinates of the Drone:
- IUC: Pose: <pose>0 0 0 0 0 0</pose>
This indicates that the base link is positioned at the origin (0, 0, 0) with no rotation (0, 0, 0).

- Link Pose: <pose>0.415 0 0 0 0 0</pose>
This positions the wing_arm_0 link 0.415 meters along the x-axis from the origin of the base link with no rotation.

- Visual Pose: <pose>-0.415 0 0 0 0 0</pose>
This positions the visual representation of wing_arm_0 -0.415 meters along the x-axis relative to the wing_arm_0 link origin, effectively placing it back at the origin of the base link.

- Collision Pose: <pose>0.228 0 -0.029 0 0 0</pose>
This positions the collision box 0.228 meters along the x-axis and -0.029 meters along the z-axis relative to the wing_arm_0 link origin.

- Link Pose: <pose>-0.415 0 0 0 0 0</pose>
This positions the wing_arm_1 link -0.415 meters along the x-axis from the origin of the base link with no rotation.

- Visual Pose: <pose>0.415 0 0 0 0 0</pose>
This positions the visual representation of wing_arm_1 0.415 meters along the x-axis relative to the wing_arm_1 link origin, effectively placing it back at the origin of the base link.

- Collision Pose: <pose>-0.228 0 -0.029 0 0 0</pose>
This positions the collision box -0.228 meters along the x-axis and -0.029 meters along the z-axis relative to the wing_arm_1 link origin.

-  The link poses position the wing_arm_0 and wing_arm_1 links at 0.415 meters and -0.415 meters along the x-axis, respectively, relative to the base link. The visual poses of the wing arms are positioned back to the base link origin by offsetting them with -0.415 meters and 0.415 meters along the x-axis, respectively. This ensures that the visual meshes are displayed correctly at their intended locations. The collision poses are adjusted to align with the visual parts at 0.228 meters and -0.228 meters along the x-axis, respectively, and -0.029 meters along the z-axis, to accurately cover the wing arm visuals.

## Collision:
When importing the stl file of the drone in gazebo , it is important to import the individual parts of the drone and not the whole drone. The reason for this is because the drone will lack collision. Without collisin, the drone won't stay on the ground and it will pass through objects. This will also affect its center of gravity which will vary. 

# Links:

-  Details about the rotor of the drone can be found in the following link: https://uav-en.tmotor.com/html/2018/navigato_0402/46.html
-  Details about the propellers of the drone can be found in the following link: https://www.mad-motor.com/collections/propellers

-  The 3D model of the drone was created in Inventor. To access the 3D model go to the **Final Update Assembly Drone.iam** file from the following link: https://drive.google.com/drive/folders/1MhGHMvqRIwXFox53sXme-O2n0eSo7QqC?usp=sharing  

- The reference SDF FILE that was used in this project was the **iris.sdf** file from the following link: https://github.com/PX4/PX4-SITL_gazebo-classic/tree/67431d233f0f08de647f0eb11239816f9c8bd6c6/models/iris
