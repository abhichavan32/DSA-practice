import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering 
from sklearn.preprocessing import LabelEncoder 



# data={
#     "income":[13,24,23,35,40,45,12]
# }
# df=pd.DataFrame(data)
# model=AgglomerativeClustering(n_clusters=2)
# df['Cluster']=model.fit_predict(df)
# print(df)

data={
    "age":[12,34,35,33,23,13],
    'diseas':["Normal","Critical","Normal","Critical","danger","Normal"]
}
df=pd.DataFrame(data)

le = LabelEncoder()
df["diseas_encode"] = le.fit_transform(df["diseas"])

model=AgglomerativeClustering(n_clusters=3)
df["cluster"]=model.fit_predict(df[['diseas_encode']])

print(df[['age','diseas','diseas_encode']])