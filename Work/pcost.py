# pcost.py
#
# Exercise 1.27

"""
The columns in portfolio.csv correspond to the stock name, number of shares, and purchase 
price of a single stock holding. Write a program called pcost.py that opens this file, 
reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.

Hint: to convert a string to an integer, use int(s). To convert a string to a floating point, use float(s).
"""
import os, sys

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        # skip header row
        next(f)

        for line in f:
            rows = line.split(',')
            
            stock = rows[0]
            shares = rows[1]
            price = rows[2]

            total_cost += float(price) * float(shares)

    return total_cost

# If calling this script from command line, then expect 1st argument to be name of Portfolio csv file.
# If no arguments are provided then assume file is 'Work\\Data\\Portfolio.csv'
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work\\Data\\Portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)    