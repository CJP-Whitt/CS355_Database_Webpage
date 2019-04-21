"""
Script for grabbing every 1000th row of input file and then writing that row to an output file
"""
import itertools

inp = open("AirportStats.csv")

out = open("AirportStats1000th_1.csv", "w")

thousandlines = itertools.islice(inp, 0, None, 1000)
for line in thousandlines:
    out.write(line)

inp.close()
out.close()

