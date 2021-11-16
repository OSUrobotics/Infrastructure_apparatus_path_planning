#! /usr/bin/env python

# Author: Josh Campbell
# Email: campbjos@oregonstate.edu
# Date: 10/21

import rospy

import tf
import os
import numpy as np
import csv
import glob
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":

    door_translation_mat = np.array([0.2071, 0, 0.11389, 1])

    # n = float(sys.argv[1])
    
    rospy.init_node('door_calibration', argv=sys.argv)


    listener = tf.TransformListener()
    
    while True:
        try:
            translation, rotation = listener.lookupTransform('j2s7s300_link_base', 'j2s7s300_end_effector', rospy.Time())
            break  # once the transform is obtained move on
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue  # if it fails try again

    transform_mat = listener.fromTranslationRotation(translation, rotation)
    
    door_pivot_mat = np.dot(transform_mat, tf.transformations.translation_matrix(door_translation_mat))
    # print(door_pivot_mat)
    # print('\n')
    # print(transform_mat)
    file = open(dir_path + "/data/door_pivot_matrix.csv", "w")
    wr = csv.writer(file, dialect='excel')

    for i in range(len(door_pivot_mat)):
        wr.writerow(door_pivot_mat[i])
    
    file.close()