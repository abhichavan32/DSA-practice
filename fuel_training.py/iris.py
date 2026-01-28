from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data=load_iris()
x_train,x_test,y_train,y_test=train_test_split(data.data,data.target,test_size=0.2,random_state=42)
model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)

# print("Accuracy: ",model.score(x_test,y_test))
x=data.data
y=data.target

print(x[:5])       # first 5 rows
print(y[:5])  