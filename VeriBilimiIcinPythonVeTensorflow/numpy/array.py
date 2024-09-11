import numpy as np

myList = [10, 20, 30, 40]
type(myList)   ## list
np.array(myList)   ## array([10, 20, 30, 40])
type(np.array(myList))   ## numpy.ndarray

matrixList = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]
type(matrixList)   ## list
matrixList[1][0]   ## 20
np.array(matrixList)   ## array([[10, 20, 30],
                       ##       [20, 30, 40],
                       ##       [30, 40, 50]])
