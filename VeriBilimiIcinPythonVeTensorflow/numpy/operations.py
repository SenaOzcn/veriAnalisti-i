import numpy as np

newRange = np.random.randint(1,100,20)
newRange   ## array([72, 15, 43, 94, 52, 44, 23, 36, 77, 59,  4, 89, 73, 87, 59,  3, 54, 27, 27,  3])
newRange > 24    ## array([ True, False,  True,  True,  True,  True, False,  True,  True,  True, False,  True,  True,  True,  True, False,  True,  True,  True, False])
result = newRange > 24
result   ## array([ True, False,  True,  True,  True,  True, False,  True,  True, True, False,  True,  True,  True,  True, False,  True,  True,  True, False])
newRange   ## array([72, 15, 43, 94, 52, 44, 23, 36, 77, 59,  4, 89, 73, 87, 59,  3, 54, 27, 27,  3])
newRange[result]   ## array([72, 43, 94, 52, 44, 36, 77, 59, 89, 73, 87, 59, 54, 27, 27])
newRange[newRange > 24]   ## array([72, 43, 94, 52, 44, 36, 77, 59, 89, 73, 87, 59, 54, 27, 27])

lastRange = np.arange(0,24)
lastRange   ## array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
lastRange + lastRange   ## array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46])
lastRange * lastRange   ## array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529])
lastRange - lastRange   ## array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
np.sqrt(lastRange)   ## array([0.        , 1.        , 1.41421356, 1.73205081, 2.        , 2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.        ,  3.16227766, 3.31662479, 3.46410162, 3.60555128, 3.74165739,  3.87298335, 4.        , 4.12310563, 4.24264069, 4.35889894,  4.47213595, 4.58257569, 4.69041576, 4.79583152])
np.max(lastRange)   ## 23
np.min(lastRange)   ## 0
