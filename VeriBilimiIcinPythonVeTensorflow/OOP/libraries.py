import numpy as np
import matplotlib.pyplot as matplot

salaryList = np.random.normal(4000,500,1000)
np.mean(salaryList)   ### 3990.3877018810063
matplot.hist(salaryList,50)
matplot.show()
## There is a graph...
