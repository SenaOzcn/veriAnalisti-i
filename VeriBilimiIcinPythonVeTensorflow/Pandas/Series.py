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
