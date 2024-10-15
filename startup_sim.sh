#!/bin/bash
source /opt/ros/humble/setup.bash
export WEBOTS_HOME=/mnt/c/Program\ Files/Webots
colcon build
source install/setup.bash
ros2 launch caleb_messerly_project_1 caleb_messerly_project_1_launch.py
