import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Road_Collisions.csv")
df_northeast = df[(df["Region or Country"]=="North East") & (df["Severity"]=="Killed")]
x = df_northeast["Road user type"]

y1=df_northeast["2018"]
y2=df_northeast["2019"]
y3=df_northeast["2020"]
y4=df_northeast["2021"]

plt.figure(figsize=(8,8))
plt.subplots_adjust(hspace=0.4, wspace=0.4)

plt.subplot(2, 2, 1)
plt.axis("equal")
plt.pie(y1,labels=x,autopct='%1.0f%%',radius=1.2)
plt.title("2018")

plt.subplot(2, 2, 2) 
plt.axis("equal")
plt.pie(y2,labels=x,autopct='%1.0f%%',radius=1.2)
plt.title("2019")

plt.subplot(2, 2, 3) 
plt.axis("equal")
plt.pie(y3,labels=x,autopct='%1.0f%%',radius=1.2)
plt.title("2020")

plt.subplot(2, 2, 4) 
plt.axis("equal")
plt.pie(y4,labels=x,autopct='%1.0f%%',radius=1.2)
plt.title("2021")

plt.show()
