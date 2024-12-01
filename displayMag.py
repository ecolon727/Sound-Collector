import csv
import array 
import numpy as np
import matplotlib.pyplot as plt


#Append CSV to array
dataList = []
with open('mag-data2.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        dataList.append(lines)

#Convert string array to float
float_array = np.array(dataList, dtype=float)


#Create plot
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plt.plot(x, float_array)

plt.title("Magnitude (Hertz)")
plt.xlabel("Sample number")
plt.ylabel("Magnitude")
plt.show()