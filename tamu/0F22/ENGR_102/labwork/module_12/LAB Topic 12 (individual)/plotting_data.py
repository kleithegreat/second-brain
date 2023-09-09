# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   12.17.1: LAB: Plotting data
# Date:         14 November 2022

import csv, numpy as np, matplotlib.pyplot as plt

data = []
with open("WeatherDataCLL.csv", "r") as weatherDataCSV:
    for i in csv.reader(weatherDataCSV, delimiter = ","):
        data.append(i)
        
data = data[1:] # removes column titles

for index, value in enumerate(data): 
    data[index].append(index) # adds days since
    data[index][0] = data[index][0].split("/")[0] # change date to only month
    
for i, v in enumerate(data): # change all elements of data to float before converting to numpy array
    for j, v2 in enumerate(v):
        data[i][j] = float(data[i][j])

data2D = list(data)
data = np.array(data, dtype = float) # converts to numpy array with float data type

# plot 1 - line graph: max temp (f) and avg wind speed (mph) vs days
x = data[0:, 6] # days starting at 0
maxTemps = data[0:, 4]
avgWindSpeed = data[0:, 1]

fig1, ax1 = plt.subplots()
fig1.suptitle("Maximum Temperature and Average Wind Speed")
ax1.set_xlabel("Date")
ax1.set_ylabel("Maximum Temperature, F")

ln1 = ax1.plot(x, maxTemps, color = "red")

ax2 = ax1.twinx()
ax2.set_ylabel("Average Wind Speed, mph")
ln2 = ax2.plot(x, avgWindSpeed, color = "blue")

plt.legend(ln1+ln2, ["Max Temp", "Avg Wind"], loc = "lower left")
plt.show()

# plot 2 - histogram of average wind speed
fig2, ax1 = plt.subplots()
fig2.suptitle("Histogram of average wind speed")
ax1.set_xlabel("Average wind speed, mph")
ax1.set_ylabel("Number of days")
ax1.hist(avgWindSpeed, bins = 30, color = "green", linewidth = 1, edgecolor = "black")

plt.show()

# plot 3 - scatterplot of average wind speed (mph) y vs min temp (f) x
minTemps = data[0:, 5]

fig3, ax1 = plt.subplots()
fig3.suptitle("Average wind speed vs Minimum Temperature")
ax1.set_xlabel("Minimum Temperature, F")
ax1.set_ylabel("Average Wind Speed, mph")
ax1.scatter(minTemps, avgWindSpeed, color = "black", s = 10)

plt.show()

# plot 4 - bar chart of one bar per month months 1-12: bars are avg temp (f), lines of highest high and lowest low of the month
dataByMonths = []
for i in range(1, 13, 1):
    currentMonth = []
    for j in data2D:
        if j[0] == i:
            currentMonth.append(j)
    dataByMonths.append(currentMonth)

monthAverages = []
for i in range(12):
    total = 0
    for j in dataByMonths[i]:
        total += j[3]
    monthAverages.append(total / len(dataByMonths[i]))
    
highs = []
for i in range(12):
    high = 0
    for j in dataByMonths[i]:
        if j[4] > high:
            high = j[4]
    highs.append(high)
    
lows = []
for i in range(12):
    low = 9999
    for j in dataByMonths[i]:
        if j[5] < low:
            low = j[5]
    lows.append(low)

fig4, ax1 = plt.subplots()
fig4.suptitle("Temperature by Month")
ax1.set_xlabel("Month")
ax1.set_ylabel("Average Temperature, F")
ax1.bar(range(1, 13, 1), monthAverages, color = "darkkhaki")
ax1.plot(range(1, 13, 1), highs, color = "red", label = "High T")
ax1.plot(range(1, 13, 1), lows, color = "blue", label = "Low T")
plt.xticks(range(1, 13, 1))
plt.legend()

plt.show()