import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:/download/householdtask3.csv')
df= pd.DataFrame(data)
pd.set_option('display.max_columns', 50)
print(data)

print("*"*200)

print(data.describe())

print("*"*200)

print("IS NULL",data.isnull().sum())
print("*"*200)

data= data.drop_duplicates()               # if any duplicates are there so remove it
print(data)
print("*"*200)


print("SCATTER PLOT ")
plt.scatter(df["year"],df["own"],marker="*",color="red")
plt.title("SCATTER PLOT")
plt.xlabel("Total Households")
plt.ylabel("Owner")
plt.show()


print("LINE CHART")
plt.plot(df["year"],df["own"],linewidth=2,linestyle="-",marker="o",markerfacecolor='red',markersize=10,color="blue")
plt.title("Line Chart")
plt.xlabel("Year")
plt.ylabel("Owner")
plt.show()


print("BAR CHART")
color=["green","brown","skyblue","yellow","red"]
plt.bar(df["year"],df["own"],color=color,width=1,edgecolor='black')
plt.title("Bar Chart")
plt.xlabel("Year")
plt.ylabel("Owner")
plt.show()

print("voilen chart")
plt.violinplot(df["income"],showmedians=True)
plt.ylabel("Income")
plt.xlabel("own")
plt.title("Violin Chart")
plt.show()