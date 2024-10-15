# Repository for Caleb Messerly's Indoor World
## CS 560

This is of a map of a moderate section of Paty Hall's 3rd floor
The included png file in this directory shows which section this is

I've made a startup_sim.sh script that should build and startup the simulation for you
On a windows computer. Not sure about mac.
Simply run the command ./startup_sim.sh in wsl and it should startup.

If not, this is the ros2 launch command:
ros2 launch caleb_messerly_project_1 caleb_messerly_project_1_launch.py

in paty.png, you can see the section I modeled. It is the cube at the bottom.
I also added some ramps and some stairs to make it more interesting

## Adjusting parameters
To adjust the light and door parameters, see the following instructions:

To open or close all doors, do the following
go to the world file located at caleb_messerly_project_1/worlds/paty_floor.wbt
Locate the doors in the proto file, and either set their positions to 0 (closed)
or set their positions to -.5 (slightly ajar) or -1 (open).

This should open the doors, you must do this for each door.

To adjust the lighting, open up the world file as before.
For each lamp, (called CeilingLight in the world file), change
light intensity to 0 for no light, or 6 for the full light. 6 is the default
for this world file.

