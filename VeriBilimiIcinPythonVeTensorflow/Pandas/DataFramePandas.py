import numpy as np
import pandas as pd

data = np.random.randn(4,3)
data
## array([[ 0.46484375,  0.28128691,  0.9473642 ],
##        [ 1.12678968, -0.25719882,  1.15687883],
##        [ 2.04686066,  0.13855855, -0.0891846 ],
##        [ 0.3786098 , -1.38290678,  0.1392032 ]])

dataFrame = pd.DataFrame(data)
## 	     0	            1	          2
## 0	0.464844	0.281287	0.947364
## 1	1.126790	-0.257199	1.156879
## 2	2.046861	0.138559	-0.089185
## 3	0.378610	-1.382907	0.139203

dataFrame[0]
## 0    0.464844
## 1    1.126790
## 2    2.046861
## 3    0.378610
## Name: 0, dtype: float64

newDataFrame = pd.DataFrame(data, index=["Atıl", "Zeynep", "Atlas", "Mehmet"], columns=["Salary", "Age", "Working Hours"] )
newDataFrame
##	         Salary	           Age	    Working Hours
## Atıl	        0.464844	0.281287	0.947364
## Zeynep	1.126790	-0.257199	1.156879
## Atlas	2.046861	0.138559	-0.089185
## Mehmet	0.378610	-1.382907	0.139203

newDataFrame["Age"]
## Atıl      0.281287
## Zeynep   -0.257199
## Atlas     0.138559
## Mehmet   -1.382907
## Name: Age, dtype: float64

newDataFrame["Working Hours"]
## Atıl      0.947364
## Zeynep    1.156879
## Atlas    -0.089185
## Mehmet    0.139203
## Name: Working Hours, dtype: float64

newDataFrame[["Salary", "Age"]]
## 	         Salary	          Age
## Atıl	        0.464844	0.281287
## Zeynep	1.126790	-0.257199
## Atlas	2.046861	0.138559
## Mehmet	0.378610	-1.382907

newDataFrame.loc["Atıl"]
## Salary           0.464844
## Age              0.281287
## Working Hours    0.947364
## Name: Atıl, dtype: float64

newDataFrame.loc["Zeynep"]
## Salary           1.126790
## Age             -0.257199
## Working Hours    1.156879
## Name: Zeynep, dtype: float64

newDataFrame.iloc[1]
## Salary           1.126790
## Age             -0.257199
## Working Hours    1.156879
## Name: Zeynep, dtype: float64

newDataFrame["Retirement Age"] = newDataFrame["Age"] + newDataFrame["Age"]
newDataFrame
##               Salary	           Age	    Working Hours     Retirement Age
## Atıl	        0.464844	 0.281287	0.947364	 0.562574
## Zeynep	1.126790	-0.257199	1.156879	-0.514398
## Atlas	2.046861	0.138559	-0.089185	0.277117
## Mehmet	0.378610	-1.382907	0.139203	-2.765814

newDataFrame.drop("Retirement Age", axis = 1)
##              Salary	           Age	    Working Hours
## Atıl	        0.464844	0.281287	0.947364
## Zeynep	1.126790	-0.257199	1.156879
## Atlas	2.046861	0.138559	-0.089185
## Mehmet	0.378610	-1.382907	0.139203

newDataFrame.drop("Mehmet", axis = 0)
## 	          Salary	  Age	     Working Hours   Retirement Age
## Atıl	        0.464844	0.281287	0.947364	0.562574
## Zeynep	1.126790	-0.257199	1.156879	-0.514398
## Atlas	2.046861	0.138559	-0.089185	0.277117

newDataFrame.drop("Retirement Age", axis = 1, inplace = True)
##              Salary	           Age	    Working Hours
## Atıl	        0.464844	0.281287	0.947364
## Zeynep	1.126790	-0.257199	1.156879
## Atlas	2.046861	0.138559	-0.089185
## Mehmet	0.378610	-1.382907	0.139203

newDataFrame.loc["Atıl"]
## Salary           0.464844
## Age              0.281287
## Working Hours    0.947364
## Name: Atıl, dtype: float64

newDataFrame.loc["Atıl"]["Age"]
## 0.28128691332222155

newDataFrame.loc["Atlas", "Age"]
## 0.13855854676563284

newDataFrame < 0
## 	        Salary	Age	Working Hours
## Atıl	        False	False	False
## Zeynep	False	True	False
## Atlas	False	False	True
## Mehmet	False	True	False

booleanFrame = newDataFrame < 0
booleanFrame
## 	        Salary	Age	Working Hours
## Atıl	        False	False	False
## Zeynep	False	True	False
## Atlas	False	False	True
## Mehmet	False	True	False

newDataFrame[booleanFrame]
## 	        Salary	Age	Working Hours
## Atıl	        NaN	NaN	NaN
## Zeynep	NaN	-0.257199 NaN
## Atlas	NaN	NaN	-0.089185
## Mehmet	NaN	-1.382907 NaN

newDataFrame[newDataFrame < 0]
## 	        Salary	Age	Working Hours
## Atıl	        NaN	NaN	NaN
## Zeynep	NaN	-0.257199 NaN
## Atlas	NaN	NaN	-0.089185
## Mehmet	NaN	-1.382907 NaN
