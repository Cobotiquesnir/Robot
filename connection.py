from pyniryo import *
from os import chdir


robot = NiryoRobot("169.254.200.200")
#NiryoRobot.release_with_tool()

robot.calibrate_auto()


#j1 -3.053 +3.053
#j2 -1.91 +0.64
#j3 -1.39 +1.57
#j4 -3.049 +3.053
#j5 -1.744 +1.919
#j6 -2.529 +2.529


#x -0.455 +0.455 / Avant-Arrière
#y -0.455 +0.455 / Gauche-Droite
#z +0.135  +0.640 / Haut-Bas

robot.joints = [0.926, -0.813, -1.008, 0.921, 1.700, 0.194]
robot.move_joints([1.6, 0.1, 0.3, 0.0, 1.0, 1.0])
robot.open_gripper()
#robot.move_joints([2.0, 0.1, 0.5, 0.0, 1.0, 0.0])
robot.close_gripper()
#robot.move_joints(0.0, 0.5, -1.0, 0.0, 0.0, 0.0)


robot.update_tool()


