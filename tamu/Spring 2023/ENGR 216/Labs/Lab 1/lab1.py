import csv
import math
import matplotlib.pyplot as plt

# reads data into array
with open("bruh.csv", "r") as rawData:
    data = []
    for i in csv.reader(rawData, delimiter=","):
        data.append(i)
    
# creating new array with complete data only  
dataSorted = []
for i in data:
    add = True
    for j in range(len(i)):
        if not i[j]:
            add = False
            break
    if add:
        dataSorted.append(i)
dataSorted = dataSorted[1:]

# converts strings to ints
for i, v in enumerate(dataSorted):
    for j, k in enumerate(v):
        dataSorted[i][j] = int(k)

#for i in dataSorted:
#    print(i)
#print(len(dataSorted))


# pink to orange
widths = []
# calculating and storing the widths into array 
for i in dataSorted[1:]:
    width = math.sqrt( (i[4]-i[2])**2 + (i[5]-i[3])**2 )
    widths.append(width)
avgWidth = sum(widths)/len(widths)
print(avgWidth)

# orange to green
length = []
for i in dataSorted:
    length.append(math.sqrt((i[0] - i[4])**2 + (i[1] - i[5])**2))
avgLength = sum(length) / len(length)
print(avgLength)

# calculating areas
# area from average length and width + uncertainty

temp = 0
for i in widths:
    temp += i - avgWidth
stdevWidths = math.sqrt( (1/len(widths)) * temp**2 )
print(stdevWidths)

# error of lengths using sample standard dev
temp = 0
for i in length:
    temp += i - avgLength
stdevLength = math.sqrt( (1/len(length)) * temp**2 )
print(stdevLength)

#propagated error of area
avgArea = avgLength * avgWidth
print(avgArea)
avgAreaError = avgArea * math.sqrt( (stdevLength/avgLength)**2 + (stdevWidths/avgWidth)**2 )
print(avgAreaError)


# area from average of sum of areas + uncertainty
areas = []
for i, k in enumerate(length):
    areas.append(k * widths[i])
statAvgArea = sum(areas)/len(areas)
print(statAvgArea)

temp = 0
for i in areas:
    temp += i - statAvgArea
stdevAreas = math.sqrt( (1/len(areas)) * temp**2 )
print(stdevAreas)

# histogram of width
plt.hist(widths, bins=10, ec='black')
plt.xlabel('Width in Pixels')
plt.ylabel('Count')
plt.title('Measruements of Width')
plt.show()

# histogram of length
plt.hist(length, bins=10, ec='black')
plt.xlabel('Length in Pixels')
plt.ylabel('Count')
plt.title('Measruements of Length')
plt.show()