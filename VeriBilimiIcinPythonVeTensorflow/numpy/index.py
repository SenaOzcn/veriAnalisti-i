import numpy as np

myRange = np.arange(0,15)
myRange   ## array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
myRange[5]   ## 5
myRange[3:8]   ## array([3, 4, 5, 6, 7])
myRange[3:8] = -5
myRange   ## array([ 0,  1,  2, -5, -5, -5, -5, -5,  8,  9, 10, 11, 12, 13, 14])

otherRange = np.arange(0,24)
otherRange   ## array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

slicingRange = otherRange[4:9]
slicingRange   ## array([4, 5, 6, 7, 8])
slicingRange[:] = 700
slicingRange   ## array([700, 700, 700, 700, 700])
otherRange   ## array([  0,   1,   2,   3, 700, 700, 700, 700, 700,   9,  10,  11,  12, 13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23])

sampleRange = np.arnage(0,24)
copySampleRange = sampleRange.copy()
copySampleRange   ## array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
sampleRange   ## array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

copySampleSlicing = copySampleRange[3:6]
copySampleSlicing   ## array([3, 4, 5])
copySampleSlicing[:] = 800
copySampleSlicing   ## array([800, 800, 800])
copySampleRange   ## array([  0,   1,   2, 800, 800, 800,   6,   7,   8,   9,  10,  11,  12, 13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23])
sampleRange   ## array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
