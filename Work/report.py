# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    """
    Open a given portfolio file, read it into list of tuples
    """

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    """
    Read a set of prices into a dictionary where the keys of the dictionary are the stock
    names and the values in the dictionary are the stock prices.
    """

    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                pass
    return prices