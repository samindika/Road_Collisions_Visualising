import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Road_Collisions.csv")

df_London = df[(df["Region or Country"]=="London") & (df["Severity"]=="Killed")]
df_Wales = df[(df["Region or Country"]=="Wales") & (df["Severity"]=="Killed")]
df_Scotland = df[(df["Region or Country"]=="Scotland") & (df["Severity"]=="Killed")]
df_SouthEast = df[(df["Region or Country"]=="South East") & (df["Severity"]=="Killed")]


x=df_London["Road user type"]
b1=df_London['2021'].astype(int)
b2=df_Wales["2021"].astype(int)
b3=df_Scotland["2021"].astype(int)
b4=df_SouthEast["2021"].astype(int)

b = np.arange(len(x))
width = 0.2


plt.figure() 
plt.bar(b-0.2, b1, width,color='red',label="London")
plt.bar(b, b2, width,color='green',label="Wales")
plt.bar(b+0.2, b3, width,color='blue',label="Scotland ")
plt.bar(b+0.4, b4, width,color='orange',label="South East ")
plt.xticks(b, ['Pedestrians', 'Pedal cyclists', 'Motorcycle users', 'Car occupants'])
plt.xlabel("Collision type")
plt.ylabel("Amount")
plt.title("Road Collisions of London, Wales, Scotland")
plt.legend()
plt.show()
