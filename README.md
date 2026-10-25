# ITU RAKE ROS 2 Project

This repository contains the ROS 2 package for the İTÜ RAKE robotics project, designed for autonomous navigation and coordinate tracking using **ROS 2 Humble** and **TurtleBot3**.

## System Architecture

The project consolidates the navigation stack and custom tracking scripts into a single, streamlined launch file:
- **Navigation2 Stack:** Handles map server, AMCL localization, and path planning using the provided custom map.
- **Coordinate Tracker:** A custom Python node (`coordinate_tracker.py`) designed to monitor and track the robot's coordinates during execution.

## Project Structure

```text
itu_rake_project/
├── config/
│   ├── map.pgm         # Occupancy grid map (image)
│   └── map.yaml        # Map metadata configuration
├── launch/
│   └── rake_system.launch.py  # Unified system launch file
├── scripts/
│   └── coordinate_tracker.py  # Custom coordinate tracking node
├── package.xml
├── setup.py
└── setup.cfg

Prerequisites
Ensure you have the following installed in your workspace (Ubuntu / WSL2 & ROS 2 Humble):

ROS 2 Humble Hawksbill

TurtleBot3 Navigation2 packages:

Bash
sudo apt install ros-humble-turtlebot3-navigation2

Installation & Building
Clone the repository into your ROS 2 workspace src directory:

Bash
cd ~/ros2_ws/src
git clone [https://github.com/ethemozserbetci/itu_rake_project.git](https://github.com/ethemozserbetci/itu_rake_project.git)
Build the package using colcon:

Bash
cd ~/ros2_ws
colcon build --packages-select itu_rake_project
source install/setup.bash
Usage
To launch the complete navigation and coordinate tracking system with a single command:

Bash
ros2 launch itu_rake_project rake_system.launch.py
