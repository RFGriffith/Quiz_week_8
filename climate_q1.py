import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

connection=sqlite3.connect("./climate.db")
yearsCursor=connection.cursor()
co2Cursor=connection.cursor()
tempCursor=connection.cursor()

yearsCursor.execute("SELECT Year FROM ClimateData")
result=yearsCursor.fetchall()
for x in result:
        years.append(x)
co2Cursor.execute("SELECT CO2 FROM ClimateData")
result=co2Cursor.fetchall()
for y in result:
        co2.append(y)
tempCursor.execute("SELECT Temperature FROM ClimateData")
result=tempCursor.fetchall()
for z in result:
        temp.append(z)
connection.close()

print(years)
print(co2)
print(temp)
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
plt.savefig("co2_temp_1.png") 
