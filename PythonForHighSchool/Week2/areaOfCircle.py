"""
areaOfCircle.py
Written By: Edward Lewis
Date: 8/4/24
Last Edited: 8/4/24
Program which will return the area of a circle for any given radius
"""

import numpy as np

"""
Numpy allows us to work with many powerful things
including other math functions such as np.sin, np.cos, np.tan
as well as pi and Euler's number. We will be using numpy all throughout
this course it will get to a point, everytime you create a python file the 
first words you will write is import numpy as np
"""

radius = 5  # radius of a circle in centimeters
area = np.pi * radius**2  # area of circle with radius in centimeters^2

print(area)
