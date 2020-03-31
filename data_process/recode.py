import pandas as pd
import numpy as np
#recode sn
df = pd.read_csv("D:\\大四下\\毕业设计\\data\\order.csv", dtype={"areaCode": object, "sn": object})
lack = df.isnull()
lac_col = lack.any()
df_lack_only = df[df.isnull().values == True]
df_del_lack_row = df.dropna(axis=0)