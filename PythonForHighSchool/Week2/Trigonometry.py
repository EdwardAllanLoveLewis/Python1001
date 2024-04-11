"""
Trigonometry.py
Written By: Edward Lewis
Date: 8/4/24
Last Edited: 8/4/24
Program which will calculate the sides of a right-angled triangle given an initial side and angle
"""


import numpy as np

angleConverter = np.pi/180  # Angles need to be in radians this will convert degrees to radians
angle = 30 * angleConverter  # angle of 30 degrees
sideAdjacent = 3  # Side length adjacent to the angle in cm

sideOpposite = sideAdjacent * np.tan(angle)  # Side length opposite angle in cm
hypotenuse = sideAdjacent * np.cos(angle)  # Hypotenuse length in cm

print(sideAdjacent, sideOpposite, hypotenuse)
"""
How can we check if this is true?
Well we can plug this in to pythagoras's theorem 
and if it works we know its true
"""

check = (sideAdjacent**2 + sideOpposite**2)**(1/2)  # Should be equal to the hypotenuse
print(check)
print(hypotenuse)

"""
Whoops! Something isn't working correctly? 
There is a bug in our code... can anyone see whats wrong?
"""