import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# marks=[45,43,25,67,46,48,53,56,95]

# mb.boxplot(marks)
# mb.title("box plot")
# mb.show()



# area=[500,800,1000,1200,1500]
# price=[20,13,45,75,65]

# mb.scatter(area,price)
# mb.xlabel("Area")
# mb.ylabel("Price")
# mb.show()

df=sns.load_dataset("iris")
sns.pairplot(df,hue="species")
plt.show()