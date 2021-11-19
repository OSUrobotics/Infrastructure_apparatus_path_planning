#! /usr/bin/env python

# Author: Josh Campbell
# Email: campbjos@oregonstate.edu
# Date: 10/21

import tf
import numpy as np
from math import pi, sin, cos, tan
from general_path_planner_kinova import MoveRobot
import rospy
import sys
from datetime import datetime

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

# pivot point is set with a circle w/raduis 236.35mm is centered on the pivot point.
# starting position is 28.81 deg clockwise from x axis of the 

# Set up a circle centered on the pivot point of door and raduis being the distance from the center of the handle to the pivot point


# rospy.init_node('door_path_planner', argv=sys.argv)
today = datetime.now()
stamp = today.strftime("%d-%H:%M")
robot_control = MoveRobot("1", "1", "2", "door_path2_{}.csv".format(stamp))

R = 0.2365 # m, raduis of the circle

angle = (180 + 28.81) * pi / 180
angle_of_approach = 28.81 * pi /180
angle_step = 5 * pi / 180

listener = tf.TransformListener()
while True:
        try:
            translation, rotation = listener.lookupTransform('j2s7s300_link_base', 'door_pivot_frame', rospy.Time())
            break  # once the transform is obtained move on
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue  # if it fails try again

robot_base_door_mat = listener.fromTranslationRotation(translation, rotation)
angle_shift = 0
new_pose_mat = np.zeros((4,4))
ee_motion = tf.TransformBroadcaster()
rate = rospy.Rate(10.0)
while angle_shift >= -pi/2:
# while True:
# while not rospy.is_shutdown:
    x_pos = R * cos(angle)
    z_pos = R * sin(angle)
    rot_mat = tf.transformations.euler_matrix(0, angle_shift ,0)
    new_pose_mat = np.dot(robot_base_door_mat, tf.transformations.translation_matrix([x_pos,0,z_pos,1]))
    ee_trans = tf.transformations.translation_from_matrix(new_pose_mat)
    
    ee_rot = tf.transformations.quaternion_from_matrix(np.dot(new_pose_mat, rot_mat))
    
    # ee_rot = tf.transformations.quaternion_from_matrix(new_pose_mat)
    
    # ee_rot = tf.transformations.quaternion_from_euler(0,((90 - angle) * pi / 180),0
    # ee_rot = tf.transformations.quaternion_about_axis( -1*pi, (0,1,0))
    new_pose = [ee_trans[0],ee_trans[1],ee_trans[2],ee_rot[0],ee_rot[1],ee_rot[2],ee_rot[3]]
    # new_pose = [ee_trans[0],ee_trans[1],ee_trans[2],0, 0,0]
    robot_control.go_to_goal(new_pose)
    robot_control.write_joint_pose()
    angle_shift -= angle_step
    angle += angle_step
    print('\n\n\n{}\n\n\n'.format(new_pose))
    # angle_of_approach += angle_step
    
    # ee_motion.sendTransform(tuple(ee_trans), tuple(ee_rot), rospy.Time.now(), 'ee_location', 'j2s7s300_link_base')
    
    # rate.sleep()

# rospy.spin()




# Select points along the circle with the axes normal to the palm aligned with the tangent of the circle

# Plan path for the end effect to the pose [x,y,z,r,p,y] should only be changing in the x,y,z and yaw

# connect to Ryans code to record the joint angles at each step, Use the recorded joint angles for future runs.


