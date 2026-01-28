from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
from sklearn.preprocessing import LabelEncoder 


# x=[[1],[2],[3],[4],[5]]
# y=[30000,35000,40000,45000,50000]

# model=KNeighborsRegressor(n_neighbors=2)
# model.fit(x,y)

# print(model.predict([[2.94]]))


marks=[[100],[80],[70],[40],[20]]
status=['pass','pass','pass','fail','fail']

le = LabelEncoder()
T_status = le.fit_transform(status)

model=KNeighborsRegressor(n_neighbors=2)
model.fit(marks,T_status)
value=model.predict([[77]])

data={
    0:'fail',
    1:'pass'
}
result=[data[i] for i in value]
print(result)
