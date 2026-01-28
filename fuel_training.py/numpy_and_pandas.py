# import numpy as np

# marks=np.array([123,124,125])
# print(sum(a)//3)
# print(max(a))


# for mark in marks:
#     if mark <= 100:
#         print("you are fail")
#     print("you are pass")

# print(f"total mark obtained: {sum(marks)}")
# print(f"percentage: {(sum(marks)/450)* 100}")

# c = float(input("Enter temperature in Celsius: "))
# f = (c * 9/5) + 32
# print("Fahrenheit:", f)

# for i in marks:
#     if i%2 !=0:
#         pass
#     else:
#         print(f"{i}is even")

# import random
# print(random.randint(100,125))

# import numpy as np

# A = np.array([[1, 2],
#               [3, 4]])

# B = np.array([[5, 6],
#               [7, 8]])
# result = A + B
# print(result)

".........................................................................................................................."

import pandas as pd

# 1D series data
"""
marks=pd.Series([70,77,90,100])
print(marks)

"""

# 2D data
# data={
#     "name":["amit","sanket","anisha","neha"],
#     "marks":["90","100","99","45"],
#     "Result":["Pass","Pass","Pass","Fail"]
# }

# """
# data={
#     "Company":["TCS","META","SUZLON","MAHINDRA"],
#     "CGPA":["7.5","6.5","6","NULL"],
#     "Package":["3LPA","6LPA","4.5LPA","5LPA"]
# }
# df=pd.DataFrame(data)
# df.to_csv("sample.csv")


# df=pd.read_csv(r"C:\Users\acer\OneDrive\Desktop\DSA\sample.csv")
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.describe())
# """

# data={
#     "Company":["TCS","META","SUZLON","MAHINDRA"],
#     "CGPA":["7.5","6.5","6","NULL"],
#     "Package":["3LPA","6LPA","4.5LPA","5LPA"]
# }
# df=pd.DataFrame(data)
# # df.to_csv("sample.csv")
# company_col=df["Company"]
# pack_comp=df["Company","Package"]
# print(pack_comp)
# print(company_col)

# selecting coloums
"""
df=pd.DataFrame(data)
print(df["marks"])"""

# adding new col
"""
df["passed"]=df["marks"] > 100
print(df)
"""
# data={
#     "marks":[[100,124,108],[120,111,122]],
#     "sub":["physics","chem","math"]
# }
# df=pd.DataFrame(data)
"""
min_mark=min(df["marks"])
max_mark=max(df["marks"])
sum_mark=sum(df["marks"])
mean_mark=df["marks"].mean
print(min_mark)
print(max_mark)
print(sum_mark)
print(mean_mark)"""

# print(df.sort_values("marks"))
# print(df.sort_values("marks",ascending=False))
# print(df.groupby("sub")["marks"])

# data={
#     "name":["Abhi","pradip","sandip","suraj"],
#     "Package":["4lpa","6lap","8lpa","4.5lpa"],
#     "company":["TCS","cognizant","wipro","suzlon"]
#     }
# df=pd.DataFrame(data)
# print(df)
# df.to_csv("session.csv")
# pd.read_csv(r"C:\Users\acer\OneDrive\Desktop\DSA\session.csv")
import pandas as pd
"""
students = {
    "Name": ["Abhi", "Ravi", "Sneha", "Kiran", "Neha"],
    "Marks": [78, 45, 88, 34, 67]
}

df = pd.DataFrame(students)

average = df["Marks"].mean()
print(f"Average is {average}")

print("Topper of class")
topper = df[df["Marks"] == df["Marks"].max()]
print(topper)

print("Passed student list")
passed=df[df["Marks"] > 45]
print(passed)

print("failed students list")
failed= df[df["Marks"] < 45]
print(failed)"""

import pandas as pd

data = {
    "Employee": ["Amit", "Ravi", "Neha", "Sneha", "Kiran", "Pooja"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Salary": [60000, 45000, 75000, 68000, 52000, 80000]
}

df = pd.DataFrame(data)

max_salary=df.groupby("Department")["Salary"].max()
print(max_salary)














