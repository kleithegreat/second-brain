
"""
Demonstrates how to operate a VProbe object.
Voltage probe must be connected to run this script.
"""

from lab.cnc import VProbe

# Initialize
probe = VProbe()

# Take reading
reading = probe.get_voltage()
print("Probe reading: {} V".format(reading))
