# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               Quinn Hamilton
#               Jinyu Zhou
#               Joaquin Torres
#               
# Section:      522
# Assignment:   9.15.1: LAB: Shoelace formula
# Date:         24 October 2022

def getpoints(stringIn): # takes a string of points and turns it into a list for computation
    pointsList = stringIn.split(" ")
    for i in pointsList:
        pointsList[pointsList.index(i)] = i.split(",")
    for i in pointsList:
        for j in i:
            pointsList[pointsList.index(i)][i.index(j)] = int(j)
    return pointsList

def cross(pointA, pointB): # returns the cross product of two given points
    return pointA[0] * pointB[1] - pointA[1] * pointB[0]
    
def shoelace(points): # returns the area of a polygon given an array of points using the shoelace formula
    crossTotal = 0
    for i in range(len(points) - 1):
        crossTotal += cross(points[i], points[i + 1])
    crossTotal += cross(points[len(points) - 1], points[0])
    return crossTotal / 2

def main():
    points = input("Please enter the vertices: ")
    print(f"The area of the polygon is {shoelace(getpoints(points))}")
    
if __name__ == "__main__":
    main()
