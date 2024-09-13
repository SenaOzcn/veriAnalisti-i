import numpy as np

myList = [[10,20,30],[20,30,40],[40,50,60]]
myMatrix = np.array(newList)
myMatrix   ## array([[10, 20, 30], [20, 30, 40], [40, 50, 60]])
myMatrix[0]   ## array([10,20,30])
myMatrix[1][2]   ## 40
myMatrix[1,2]    ## 40
myMatrix[1:,2]   ## array([40,60])
myMatrix[0:,2]   ## array([30,40,60])
myMatrix[2:,2]   ## array([60])

newList = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
newMatrix = np.array(newList)
newMatrix   ## array([[ 0,  1,  2,  3,  4], [ 5,  6,  7,  8,  9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]])
newMatrix[2]   ## array([10, 11, 12, 13, 14])
newMatrix[[4,0,2]]   ## array([20, 21, 22, 23, 24], [0, 1, 2, 3, 4], [10, 11, 12, 13, 14])
