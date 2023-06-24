
"""
Demonstrates using the .move_to() method.
"""

# Import
from lab.cnc import CNC

# Initialize
cnc = CNC()
cnc.issue_warning()
cnc.home()

# Set points to go travel to
points = [(100, 200, 0), (200, 100, 100), (300, 400, 0), (400, 200, 100)]

# Move CNC to points
for point in points:
    cnc.move_to(*point)

# Return home
cnc.move_to(0, 0, 0)
