# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# data={
#     "Glucose":[80,100,120,140,160],
#     "Diabetes":[0,0,0,1,1]
# }
# df=pd.DataFrame(data)
# x=df[["Glucose"]]
# y=df[["Diabetes"]]

# model=LogisticRegression()
# model.fit(x,y)
# prediction=model.predict([[100]])
# print(prediction)


# data={
#     "Loan":[12000,13000,14000,30000],
#     "Status":[False,False,True,True]
# }
# df=pd.DataFrame(data)
# x=df[["Loan"]]
# y=df[["Status"]].values.ravel()

# model=LogisticRegression()
# model.fit(x,y)
# prediction=model.predict([[12000]])
# print(prediction)

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# data={
#     "image_id":[12,14,16,18],
#     "Spam":[True,False,True,False]
# }
# df=pd.DataFrame(data)
# x=df[["image_id"]]
# y=df[["Spam"]].values.ravel()
# model=LogisticRegression()
# model.fit(x,y)
# prediction=model.predict([[18]])
# print(prediction)



# data={
#     "marks":[123,143,146,150],
#     "allowed":["NO","YES","YES","YES"]
# }

# df=pd.DataFrame(data)
# x=df[["marks"]]
# y=df[["allowed"]].values.ravel()

# model=LogisticRegression()
# model.fit(x,y)
# prediction=model.predict([[143]])
# print(prediction)

# data={
#     "Age":[14,12,15,18,19,21],
#     "voter":["NO","NO","NO","YES","YES","YES"]
# }
# df=pd.DataFrame(data)
# x=df[["Age"]]
# y=df[["voter"]].values.ravel()

# model=LogisticRegression()
# model.fit(x,y)
# pre=model.predict([[24]])
# print(pre)

# data={
#     "Heart_rate":[120,78,80,45,64],
#     "Diseas":["yes","No","No","yes","No"]
# }
# df=pd.DataFrame(data)
# x=df[["Heart_rate"]]
# y=df[["Diseas"]].values.ravel()

# model=LogisticRegression()
# model.fit(x,y)
# pre=model.predict([[68]])
# print(pre)

data={
    "battery":[0,20,40,80,100],
    "status":["drain","drain","usage","usage","usage"]
}
n=int(input("enter the bettery percentage: "))
df=pd.DataFrame(data)
x=df[["battery"]]
y=df[["status"]].values.ravel()
model=LogisticRegression()
model.fit(x,y)
pre=model.predict([[n]])
print(pre)

