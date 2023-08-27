
"""
Demonstrates using the .circle() method.
"""

# Import
from lab.cnc import CNC

# Initialize
cnc = CNC()
cnc.home()
cnc.move_to(100, 400, 0)

# Loop
for radius in range(50, 300, 50):
    print("Making circle of radius {} mm".format(radius))
    cnc.circle(radius, 150)

# Return home
cnc.move_to(0, 0, 0)
