#!/usr/bin/env python

# Author: Josh Campbell
# Email: campbjos@oregonstate.edu
# Date: 10/21

import rospy

import tf
import os
import numpy as np
from math import pi
import csv
import glob
import sys


if __name__ == '__main__':

    rospy.init_node('door_pivot_tf')

    directory = os.path.dirname(os.path.realpath(__file__))

    door_pivot_mat = np.zeros((4,4))
    
    with open(directory + '/data/door_pivot_matrix.csv') as f:
        reader = csv.reader(f)
        for j, row in enumerate(reader):
            for i, col in enumerate(row):
                door_pivot_mat[j][i] = float(col)


    translation = tf.transformations.translation_from_matrix(door_pivot_mat)
    rotation = tf.transformations.quaternion_from_matrix(door_pivot_mat)
    door_pivot = tf.TransformBroadcaster()

    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():

        door_pivot.sendTransform(tuple(translation), tuple(rotation), rospy.Time.now(), 'door_pivot_frame', 'j2s7s300_link_base')
        rate.sleep()