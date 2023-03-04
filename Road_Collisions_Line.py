import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Road_Collisions.csv")


df_midlands = df[(df["Region or Country"]=="West Midlands") & (df["Severity"]=="Killed")]

df_t = pd.DataFrame.transpose(df_midlands)

df_t.columns = df_t.iloc[2]

df_t = df_t.iloc[4:14,:]

df_t.index = pd.to_numeric(df_t.index)

plt.figure(figsize=(9,6))
plt.plot(df_t.index, df_t["Pedestrians"].astype(int), label="Pedestrians")
plt.plot(df_t.index, df_t["Pedal cyclists"].astype(int), label="Pedal cyclists")
plt.plot(df_t.index, df_t["Motorcycle users"].astype(int), label="Motorcycle users")
plt.plot(df_t.index, df_t["Car occupants"].astype(int), label="Car occupants")
plt.xticks([2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])
plt.xlabel("Collision type")
plt.ylabel("Amount")
plt.legend()
plt.show()
