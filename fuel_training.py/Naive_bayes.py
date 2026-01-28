# from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score


# x=[[1],[2],[3],[4],[5]]
# y=[0,0,0,1,1]

# model=GaussianNB()
# model.fit(x,y)

# print(model.predict([[3.9]]))



# x=[[100],[96],[84],[74],[50]]
# y=[1,1,1,0,0]

# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

# model=GaussianNB()
# model.fit(x_train,y_train)


# y_pred=model.predict([[95]])
# print(y_pred)
# print("Accuracy: " , accuracy_score(y_test,y_pred))     




# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split

# x=['free','congratulation','money','company','prize','heartly','sorry','unfortunaitly']
# y=[0,0,0,1,0,1,1,1]

# vect=CountVectorizer()

# z=vect.fit_transform(x)
# z_train,z_test,y_train,y_test=train_test_split(z,y,test_size=0.2)

# model=MultinomialNB()
# model.fit(z_train,y_train)

# y_pred=model.predict(z_test)
# print('accuracy: ',accuracy_score(y_test,y_pred))


# new_pred = model.predict(vect.transform(['company prize']))
# print("Prediction for 'company prize':", new_pred)


from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

x=[[1,1,0],[0,1,0],[0,0,0],[1,1,1],[0,0,0]]
y=[1,0,0,1,0]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

model=BernoulliNB()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print("accuracy: ",accuracy_score(y_test,y_pred))

pre=model.predict([[0,0,1]])
print(pre)


