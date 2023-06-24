
"""
Demonstrates how to operate a MAG object.
Magnetic field probe must be connected to run this script.
"""

from lab.cnc import MAG

# Initialize
probe = MAG()

# Get reading
reading = probe.get_field()
print("Probe reading: {}".format(reading))
