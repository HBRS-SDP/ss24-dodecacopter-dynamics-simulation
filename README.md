# ss24-dodecacopter-dynamics-simulation


# Dodecacopter Dynamics Simulation Project


## Project Description:

The Dodecacopter Dynamics Simulation project is designed to enable safe testing of new algorithms for a seeding drone within a simulated environment. By using a detailed 3D model of the dodecacopter and importing it into Gazebo, the project aims to evaluate the performance of various control strategies without risking physical damage to the drone.

## Project Goals
-    Develop a comprehensive 3D model of the dodecacopter.
-    Create a configuration file with the drone's physical properties and dynamics for integration into Gazebo.
  -    Enable manual control of the drone in the virtual environment for flight testing.

## Tools and Technologies:

   - ROS (Robot Operating System): For testing and validating the drone's dynamics.
   - Gazebo: A robotics simulation environment for controlling and simulating the dodecacopter.
   - Inventor: For creating the 3D model of the drone.
   - Git & GitHub: For version control and project management.
   - Slack: For team communication and coordination.

## Requirements Specifications:

-    **3D Model Development**
        - Priority: High
        - Role: Mechanical Engineer
        - Goal: Create a realistic 3D model for import into Gazebo.
        - Acceptance Criteria: Accurate representation of physical dimensions and features.
-    **Configuration File Creation**
        - Priority: High
        - Role: Software Developers
        - Goal: Configure the drone model within Gazebo with specific parameters.
        - Acceptance Criteria: Accurate mass, inertia, and other physical parameters.

-    **Manual Control Implementation**
        - Priority: High
        - Role: Software Developers
        - Goal: Control the drone model in simulation using a SIYI MK15 controller.
        - Acceptance Criteria: Accurate flight behavior with thrust, yaw, pitch, and roll commands.

## Project Structure:

 -  **Minimum Viable Product (MVP)**

    -  **Project Organization**:
        -  Organized into a ROS package format.
        -  Focus on integrating the 3D model into Gazebo and proper configuration.

    -  **ROS Nodes**L
        Simulation Nodes: Handle integration with Gazebo.
        Basic Control Node: Manage control commands for demonstrations.

-  **Integration**:

    -  Development Branch: All development work will be conducted on a dedicated branch with frequent commits.
    -  Merge Requests: Review and merge changes into the main branch upon reaching key milestones.

-  **Demonstration**:

    -  Demo Setup: Simulate a dodecacopter's flight in Gazebo with predefined obstacles.
    -  Operator Interaction: Initiate flight via ROS node commands.
    -  System Response: Execute maneuvers using the SIYI MK15 controller and monitor via ROS topics.

-  **Collaboration Plans**:

    -  Scheduling: Regular team meetings.
    -  Communication Tools: Slack, Google Meet, Webex, and GitHub.
    -  Version Control: Managed through GitHub.

## Future Steps:
-  Update the SDF file with correct poses of each part of the dodecacopter.
-  Create and validate test cases and scenarios.
-  Develop a communication interface for control commands.

For detailed technical specifications, reference materials, and configuration data, please refer to the full project documentation and associated files.

## Repository Links:
-  Project Repository
-  [Project Board](https://github.com/orgs/HBRS-SDP/projects/17/views/1)

## Installation
To install the necessary dependencies, run the following commands:

```bash
# Clone the repository
git clone git@github.com:HBRS-SDP/ss24-dodecacopter-dynamics-simulation.git

# Change directory
cd ss24-dodecacopter-dynamics-simulation

# Install dependencies
pip install -r requirements.txt

This is a  an overview of the project, its goals, and the tools and technologies used. For more detailed information, please refer to the project documentation included in this repository.
