import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score,confusion_matrix

# x=np.array([[3],[6],[4],[1],[2],[5],[7]])
# y=np.array([0,0,0,1,1,1,1])

# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

# model=LogisticRegression()
# model.fit(x_train,y_train)

# y_pred=model.predict(x_test)
# print("predict: ", y_pred)
# print('Accuracy: ',y_test)

z=np.array([[1],[2],[3],[4],[5],[6],[7]])   #employess
x=np.array([[3],[6],[4],[1],[2],[5],[7]])   # year of experience
y=np.array([0,1,1,0,0,1,1])                  # salery 0 = 1.5 ,1=6.5

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print("predict: ", y_pred)
print('Accuracy: ',y_test)
print(model.predict([[12]]))

