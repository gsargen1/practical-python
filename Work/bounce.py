"""
A rubber ball is dropped from a height of 100 meters and each time it hits the ground, 
it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a 
table showing the height of the first 10 bounces.
"""

INITIAL_HEIGHT = 100

height = INITIAL_HEIGHT

for bounce in range(10):
    height = height * 3 / 5
    print(bounce, round(height, 4))

