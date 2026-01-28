# Machine learning
import pandas as pd

# x=np.array([[1],[2],[3],[4],[5]])
# y=np.array([35,40,45,50,55])
# model=LinearRegression()
# model.fit(x,y)
# prediction=model.predict([[6]])
# print(prediction)





# import numpy as np
# from sklearn.linear_model import LinearRegression
# name=np.array([["Abhi"],["Suraj"],["Kiran"],["pradip"],["sandip"]])
# salary=np.array([12000,13000,14000,15000,16000])
# model=LinearRegression()
# model.fit(name,salary)
# prediction=model.predict([["Rajesh"],["rahul"]])
# print(prediction)







# import numpy as np
# from sklearn.linear_model import LinearRegression

# location=np.array([[1],[2],[3],[4]])
# price=np.array([1200,2300,12500,1400])
# model=LinearRegression()
# model.fit(location,price)
# prediction=model.predict([[8]])
# print(f"{prediction} sqft")



import numpy as np
from sklearn.linear_model import LinearRegression

km=np.array([[1],[2],[3],[7],[12]])
time=np.array([12,16,18,21,28])
model=LinearRegression()
model.fit(km,time)
prediction=model.predict([[24]])
print(f"{prediction} min")

