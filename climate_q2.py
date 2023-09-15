import matplotlib.pyplot as plt
import pandas as pd

years = []
co2 = []
temp = []

data=pd.read_csv("climate.csv")
yearsCsv=data["Year"]
co2Csv=data["CO2"]
tempCsv=data["Temperature"]


for x in yearsCsv:
    print(x)
    years.append(x)

for y in co2Csv:
    print(y)
    co2.append(y)

for z in tempCsv:
    print(z)
    temp.append(z)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

