# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   12.17.1: LAB: Plotting data
# Date:         14 November 2022

import csv
import numpy as np
import matplotlib.pyplot as plt

with open("WeatherDataCLL.csv", "r") as weatherDataCSV:
    data = []
    for i in csv.reader(weatherDataCSV, delimiter = ","):
        data.append(i)
data = data[1:]
"""DATES ARE STRINGS, CAST TO INT WHEN PROCESSING, TODO: ADD DAYS SINCE STARTING WITH 0"""
data = np.array(data) 
print(data)
# plot 1 - line graph: max temp (f) and avg wind speed (mph) vs days
fig, ax = plt.subplots()

# plot 2 - histogram of average wind speed


# plot 3 - scatterplot of average wind speed (mph) y vs min temp (f) x


# plot 4 - bar chart of one bar per month months 1-12: bars are avg temp (f), lines of highest high and lowest low of the month

