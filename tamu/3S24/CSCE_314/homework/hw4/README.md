# CSCE 314 HW4
Kevin Lei, UIN 432009232

---
## Compiling and running
To compile the programs, run the following command in the terminal:
```bash
javac *.java
```
Then you can run the following commands to run each program:
```bash
java SubsetOutputFib
java ImprovedFibonacci
java VehicleTest
java PassengerVehicle
```
Make sure to run the commands in the same directory as the source files, which should just be the project root.
## Running SubsetOutputFib
The program will prompt you to enter two numbers in the terminal, which will be used as the lower and upper indices of the Fibonacci sequence to be printed. When prompted for the lower index, enter a number and press enter. When prompted for the upper index, enter a number and press enter. If you enter nonsensical input, the program will try to correct it and accordingly and inform you of the correction(s) made.
## Example/Expected Output
All code was compiled and run with the following versions:
```bash
> java --version
java 21.0.2 2024-01-16 LTS
Java(TM) SE Runtime Environment (build 21.0.2+13-LTS-58)
Java HotSpot(TM) 64-Bit Server VM (build 21.0.2+13-LTS-58, mixed mode, sharing)
```
### SubsetOutputFib
```bash
Enter the beginning index: 2
Enter the ending index: 6
2: 1
3: 2 *
4: 3
5: 5
6: 8 *
```
```bash
Enter the beginning index: -1
Enter the ending index: -7
The beginning index cannot be negative. The absolute value is used instead.
The ending index cannot be negative. The absolute value is used instead.
1: 1
2: 1
3: 2 *
4: 3
5: 5
6: 8 *
7: 13
```
### ImprovedFibonacci
```bash
1: 1
2: 1   
3: 2 * 
4: 3   
5: 5   
6: 8 * 
7: 13  
8: 21  
9: 34 *
```
### VehicleTest
```bash
Owner Names: 
bruh1
bruh2
bruh3
bruh4
bruh5
lmao
bruh
poggers
Hyunyoung Lee
Joe Biden
Changing owner name of Vehicle 1: 
Vehicle 1 initial owner: bruh1    
Vehicle 1 new owner: bruh lmao    
Vehicle IDs:
1
2
3
4
5
6
7
8
9
10
Max Vehicle ID: 10
Testing speed methods:
Vehicle 1 initial speed: 0
Changing speed of Vehicle 1 to 50:
Vehicle 1 new speed: 50
Stopping Vehicle 1:
Vehicle 1 new speed: 0
Testing direction methods:
Vehicle 1 initial direction: 0
Turning Vehicle 1 22 degrees:
Vehicle 1 new direction: 22
Turning Vehicle 1 left:
Vehicle 1 new direction: -68
Turning Vehicle 1 right:
Vehicle 1 new direction: 22
Testing toString on v1:
Owner: bruh lmao, Speed: 0, Direction: 22
```
### PassengerVehicle
```bash
Owner: George W. Bush, Speed: 0, Direction: 0, Total Seats: 5, Occupied Seats: 0
Owner: Barack Obama, Speed: 0, Direction: 0, Total Seats: 4, Occupied Seats: 0 
Owner: Donald Trump, Speed: 0, Direction: 0, Total Seats: 3, Occupied Seats: 0 
Owner: Joe Biden, Speed: 0, Direction: 0, Total Seats: 2, Occupied Seats: 2    
Owner: Hyunyoung Lee, Speed: 0, Direction: 0, Total Seats: 1, Occupied Seats: 1
```