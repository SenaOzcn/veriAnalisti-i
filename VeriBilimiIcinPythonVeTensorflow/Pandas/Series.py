import numpy as np
import pandas as pd

myDict = {
  "Atıl"= 50,
  "Zeynep"= 40,
  "Mehmet" = 30
}

pd.Series(myDict)   ## Atıl      50
                    ## Zeynep    40
                    ## Mehmet    30
                    ## dtype: int64
type(pd.Series(myDict))   ## pandas.core.series.Series

myAges = [50,40,30]
myNames = ["Atıl", "Zeynep", "Mehmet"]

pd.Series(myAges)   ## 0    50
                    ## 1    40
                    ## 2    30
                    ## dtype: int64

pd.Series(myAges, myNames)  ## Atıl      50
                            ## Zeynep    40
                            ## Mehmet    30
                            ## dtype: int64

pd.Series(data=myAges, index=myNames)   ## Atıl      50
                                        ## Zeynep    40
                                        ## Mehmet    30
                                        ## dtype: int64
numRange = ([50,40,30])
numRange   ## array([50, 40, 30])
pd.Series(numRange)   ## 0    50
                      ## 1    40
                      ## 2    30
                      ## dtype: int64

pd.Series(numRange,myNames)   ## Atıl      50
                              ## Zeynep    40
                              ## Mehmet    30
                              ## dtype: int64

comp1 = pd.Series([10, 5, 1] ,["Atıl", "Atlas", "Osman"])
comp1   ## Atıl     10
        ## Atlas     5
        ## Osman     1
        ## dtype: int64

comp2 = pd.Series([20, 10, 8] ,["Atıl", "Atlas", "Osman"])
comp2   ## Atıl     20
        ## Atlas    10
        ## Osman     8
        ## dtype: int64

comp2["Atlas"]   ## 10

result = comp1 + comp2
result  ## Atıl     30
        ## Atlas    15
        ## Osman     9
        ## dtype: int64

difSeries = pd.Series([20, 30, 40, 50], ["a", "b", "c", "d"])
difSeries2 = pd.Series([10, 5, 3, 1], ["a", "c", "f", "g"])

difSeries   ## a    20
            ## b    30
            ## c    40
            ## d    50
            ## dtype: int64

difSeries2  ## a    10
            ## c     5
            ## f     3
            ## g     1
            ## dtype: int64

difSeries + difSeries2    ## a    30.0
                          ## b     NaN
                          ## c    45.0
                          ## d     NaN
                          ## f     NaN
                          ## g     NaN
                          ## dtype: float64

