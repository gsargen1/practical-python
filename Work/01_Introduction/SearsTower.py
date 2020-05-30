"""
One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago. 
Each day thereafter, you go out double the number of bills. 
How long does it take for the stack of bills to exceed the height of the tower?
"""

DOLLAR_BILL_THICKNESS = 0.000358333333
SEARS_TOWER_HEIGHT = 1450

days = 1
height = DOLLAR_BILL_THICKNESS

while height < SEARS_TOWER_HEIGHT:
    height = height * 2
    days +=1

    print('Day: ' + str(days) + '\t' + 'Height: ' + str(round(height, 2)))
    
