# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   
# Date:         07 November 2022

import csv

with open("WeatherDataCLL.csv", "r") as weatherDataCSV:
    data = []
    for i in csv.reader(weatherDataCSV, delimiter = ","):
        data.append(i)
    data = data[1:]
    
threeYearMax = 0
threeYearMin = int(data[0][5])
totalPrecip = 0
for i in data:
    if int(i[4]) > threeYearMax:
        threeYearMax = int(i[4])
    if int(i[5]) < threeYearMin:
        threeYearMin = int(i[5])
    totalPrecip += float(i[2])

print(f"3-year maximum temperature: {threeYearMax} F")
print(f"3-year minimum temperature: {threeYearMin} F")
print(f"3-year average precipitation: {totalPrecip / len(data):.3f} inches")


month = input("Please enter a month: ")
year = input("Please enter a year: ")
calendar = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

# worst code ive ever written in my life
for i in data:
    i[0] = i[0].split("/")
for i, day in enumerate(data):
    if not (int(day[0][0]) == calendar[month] and int(day[0][2]) == int(year)):
        data[i] = ""
    
try:
    while True:
        data.remove("")
except ValueError:
    lmao = 0

totalMaxDailyTemp = 0
totalWind = 0
totalPrecipDays = 0
for i in data:
    totalMaxDailyTemp += int(i[4])
    totalWind += float(i[1])
    if float(i[2]) != 0:
        totalPrecipDays += 1
    
print(f"For {month} {year}:")
print(f"Mean maximum daily temperature: {totalMaxDailyTemp / len(data):.1f} F")
print(f"Mean daily wind speed: {totalWind / len(data):.2f} mph")
print(f"Percentage of days with precipitation: {totalPrecipDays * 100 / len(data):.1f}%")
