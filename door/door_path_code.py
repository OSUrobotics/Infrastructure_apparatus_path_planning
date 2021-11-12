#! /usr/bin/env python

# Author: Josh Campbell
# Email: campbjos@oregonstate.edu
# Date: 10/21

# different script touch off point to calibrate the arm to the door
# saves the transform matrix to go from the  


# The pivot point is 207.1mm in the x and 113.89mm in the y
#      207.1mm (* == pivot point of door)
# *________________
#                  |
#                  |
#                  |  113.89mm
#                  |
#                  |
#                  H  (H == center of the handle - calibration point)

# pivot point is set with a circle w/raduis 338.6mm is centered on the pivot point.
# starting position is 28.81 deg clockwise from x axis of the 

# Set up a circle centered on the pivot point of door and raduis being the distance from the center of the handle to the pivot point


# Select points along the circle with the axes normal to the palm aligned with the tangent of the circle

# Plan path for the end effect to the pose [x,y,z,r,p,y] should only be changing in the x,y,z and yaw

# connect to Ryans code to record the joint angles at each step, Use the recorded joint angles for future runs.


