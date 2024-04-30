Title: Homework 5 README
Name: Kevin Lei
UIN: 432009232
----------
Problem 2
----------
How to compile:

- Navigate to the P2 directory in the terminal
- Run the command `javac *.java`

How to execute:

- Run the command `java Main S input.txt`

Expected output:

input.txt
s ( 14.5, 1.0 ) 12.5
c ( 23, 37.5 ) 19
s ( 6.5, 11.1 ) 25
c ( 30, 50 ) 3
c ( 51, 15 ) 4.1
s ( 30, 60 ) 12
c ( 16.5, 10.5 ) 52
s ( 73.5, 35 ) 100
s ( 16.5, 10.5 ) 52
c ( 6.5, 11.1 ) 20
s ( 26.5, 41.1 ) 5
The input file contains 11 shapes.
11 shapes have been created
Square with side length 12.5 and upper left corner at (14.5, 1.0)
Circle with radius 19.0 and center at (23.0, 37.5)
Square with side length 25.0 and upper left corner at (6.5, 11.1)
Circle with radius 3.0 and center at (30.0, 50.0)
Circle with radius 4.1 and center at (51.0, 15.0)
Square with side length 12.0 and upper left corner at (30.0, 60.0)
Circle with radius 52.0 and center at (16.5, 10.5)
Square with side length 100.0 and upper left corner at (73.5, 35.0)
Square with side length 52.0 and upper left corner at (16.5, 10.5)
Circle with radius 20.0 and center at (6.5, 11.1)
Square with side length 5.0 and upper left corner at (26.5, 41.1)
Shapes sorted in ascending order of area:
Square with side length 5.0 and upper left corner at (26.5, 41.1)
Circle with radius 3.0 and center at (30.0, 50.0)
Circle with radius 4.1 and center at (51.0, 15.0)
Square with side length 12.0 and upper left corner at (30.0, 60.0)
Square with side length 12.5 and upper left corner at (14.5, 1.0)
Square with side length 25.0 and upper left corner at (6.5, 11.1)
Circle with radius 19.0 and center at (23.0, 37.5)
Circle with radius 20.0 and center at (6.5, 11.1)
Square with side length 52.0 and upper left corner at (16.5, 10.5)
Circle with radius 52.0 and center at (16.5, 10.5)
Square with side length 100.0 and upper left corner at (73.5, 35.0)
Total area of all shapes: 24620.953051077784

----------
Problem 3
----------

How to compile:

- Navigate to the P3 directory in the terminal
- Run the command `javac *.java`

How to execute:

- Run the command `java CellTest`

Expected output:

===
1 22 21 12 24 17     
sum of intlist is 97 
sum of null list is 0
===
===
1.0 16.0 13.72 5.0 22.0 7.1 
sum ints = 97.0
sum doubles = 64.82
===

----------
Problem 4
----------

How to compile:

- Navigate to the P3 directory in the terminal (still in the P3 directory)
- Run the command `javac *.java`

How to execute:

- Run the command `java CellListTest`

Expected output:

stringlist = [(head: A) -> (the) -> (the) -> (dove)]
stringlist2 = [(head: A) -> (dove) -> (the) -> (the)]
stringlist3 = [(head: A) -> (dove) -> (dove) -> (the)]
stringlist equals to stringlist2 ? true
stringlist equals to stringlist3 ? false
CellList<Integer> equals to CellList<String> ? false
list  = [(head: 1) -> (2) -> (3) -> (4)]
list1 = [(head: 2) -> (4) -> (3) -> (1)]
list == list1 is false
list.equals(list1) = true
list3 = [(head: 1) -> (2) -> (3) -> (1)]
list4 = [(head: 1) -> (2) -> (3) -> (1) -> (4)]
list1.equals(list3) = false
list1.equals(list4) = false
list.compareTo(list1) = 0
list.compareTo(list4) = -1
[(head: )]
[(head: 1) -> (2) -> (3) -> (4)]
1
[(head: 22) -> (21) -> (2) -> (3) -> (4)]
22
[(head: 22) -> (21) -> (2) -> (3) -> (4)]
22 22
21 21
2 2
3 3
4 4
[(head: )]
list1 = [(head: 2) -> (4) -> (3) -> (1)]
list2 = [(head: 4) -> (3) -> (2) -> (21) -> (22) -> (1) -> (2) -> (3) -> (4)]
list2.compareTo(list1) = 1
=== end of test