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
print(f"Average width: {avgWidth}")

# orange to green
length = []
for i in dataSorted:
    length.append(math.sqrt((i[0] - i[4])**2 + (i[1] - i[5])**2))
avgLength = sum(length) / len(length)
print(f"Average length: {avgLength}")   





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



# error of widths using sample standard dev
temp = 0
for i in widths:
    temp += (i - avgWidth)**2
stdevWidths = math.sqrt( (temp/len(widths))  )
stdErrWidths = stdevWidths / math.sqrt(len(widths))
print(f"Width error: {stdevWidths}")

# error of lengths using sample standard dev
temp = 0
for i in length:
    temp += (i - avgLength)**2
stdevLength = math.sqrt( (temp/len(length)) )
stdErrLengths = stdevLength / math.sqrt(len(length))
print(f"Length error: {stdevLength}")


#propagated error of area using average l and w
avgArea = avgLength * avgWidth
print(f"Average area using average len * width: {avgArea}")
avgAreaError = avgArea * math.sqrt( (stdErrLengths / avgLength)**2 + (stdErrWidths / avgWidth)**2 )
print(f"Error: {avgAreaError}")




# area from average of sum of areas + uncertainty
areas = []
for i, k in enumerate(length):
    areas.append(k * widths[i-1])
statAvgArea = sum(areas)/len(areas)
print(f"Average of individual areas: {statAvgArea}")

temp = 0
for i in areas:
    temp += (i - statAvgArea)** 2
stdevAreas = math.sqrt( (1/len(areas)) * temp )
print(f"Error: {stdevAreas/math.sqrt(len(areas))}")
