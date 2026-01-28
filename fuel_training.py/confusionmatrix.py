from sklearn.metrics import confusion_matrix,classification_report
x=[[12,23,14],[13,34,32],[16,45,23],[19,54,32]]
y=[1,0,1,0]
model=classification_report()
model.fit()
y=model.predict(x)

print(confusion_matrix())