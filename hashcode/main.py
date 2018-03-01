import numpy as np
import math
import sys

# 3 4 2 3 2 10
# 0 0 1 3 2 9
# 1 2 1 0 0 9
# 2 0 2 2 0 9

# 3 rows, 4 columns, 2 vehicles, 3 rides, 2 bonus and 10 steps
# ride from [0, 0] to [1, 3], earliest start 2, latest finish 9
# ride from [1, 2] to [1, 0], earliest start 0, latest finish 9
# ride from [2, 0] to [2, 2], earliest start 0, latest finish 9

def read_input(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        rows, columns, vehicles, rides, bonus, steps = [int(val) for val in line.split()]

        books = []
        for row in range(rows-1):
            data = f.readline().split()
            print(books)
            books.append(car_deliveries([data[0],data[1]],[data[2],data[3]],data[4],data[5]));


    return rows, columns, vehicles, rides, bonus, steps, books


class car_deliveries:
    def __init__(self, start_node, finish_node, start_time, finish_time):
        self.start_node = start_node
        self.finish_node = finish_node
        self.start_time = start_time
        self.finish_time = finish_time

def main():
    print("starting")
    rows, columns, vehicles, rides, bonus, steps, books = read_input("a_example.in")
    print books

if __name__ == "__main__":
    main()
