import numpy as np

## random

np.random.randn(8)
np.random.randn(4,4)
np.random.randint(1,10)
np.random.randint(1,10,5)
myNumpy = np.arange(30)
myNumpy   ## array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
                     17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
myRandom = np.random.randint(1,100,30)
myRandom   ## array([83, 93, 87,  2, 19, 61,  0, 73, 45, 88, 73, 98, 46, 95, 27, 95, 51,
                     73, 41, 74, 25, 47, 20, 86, 75, 25, 92, 87, 79, 82])

## numpy dizi metodları

myNumpy.reshape(5,6)   ## array([[ 0,  1,  2,  3,  4,  5],
                                 [ 6,  7,  8,  9, 10, 11],
                                 [12, 13, 14, 15, 16, 17],
                                 [18, 19, 20, 21, 22, 23],
                                 [24, 25, 26, 27, 28, 29]])
myNumpy.max()  ## 29
myNumpy.min()   ## 0
myRandom.max()   ## 98
myRandom.min()   ## 0
myRandom.argmax()   ## 11
myRandom.argmin()   ## 6
myNumpt.shape   ## (30,)
