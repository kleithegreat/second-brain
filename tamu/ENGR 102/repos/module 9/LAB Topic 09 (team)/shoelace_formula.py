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

def getpoints(stringIn):
    points = []
    for i in range(len(stringIn)):
        try:
            if stringIn[i] in "0123456789" and stringIn[i + 1] == "," and stringIn[i + 2] in "0123456789":
                points += [int(stringIn[i]), int(stringIn[i + 2])]
        except:
            continue
    return points
    
    
def cross(pointA, pointB):
    return pointA[0] * pointB[1] - pointA[1] * pointB[0]
    
def shoelace(points):
    crossTotal = 0
    for i in range(len(getpoints(points))):
        crossTotal += cross(getpoints(points)[i], getpoints(points)[i + 2])
    return crossTotal / 2
    
def main():
    points = input("Please enter the verticies: ")
    getpoints(points)
    print(f"The area of the polygon is {shoelace(points)}")
    
if __name__ == "__main__":
    main()
