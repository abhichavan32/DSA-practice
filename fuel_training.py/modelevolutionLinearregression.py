import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.model_selection import train_test_split

# x=np.array([[500],[800],[1000],[1200],[1500]])
# y=np.array([50,80,100,120,150])

# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

# model=LinearRegression()
# model.fit(x_train,y_train)

# print(model.predict([[300]]))

# x=[50,60,70,80,90]
# y=[48,64,67,75,89]

# # mae=mean_absolute_error(x,y)
# # print("MAE: ",mae)

# MSE=mean_squared_error(x,y)
# print("MSE: ",MSE)

actual=[120,130,125,145,129]
predict=[119,126,120,143,128]

MAE=mean_absolute_error(actual,predict)
MSE=mean_squared_error(actual,predict)

print(MAE)
print(MSE)