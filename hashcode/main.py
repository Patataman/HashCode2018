import numpy as np
import math
import sys

from classes import *

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
        rows, columns, num_vehicles, rides, bonus, steps = [int(val) for val in line.split()]

        #Rutas a realizar
        books = []
        print(rows)
        for row in range(rows):
            data = f.readline().split()
            print(data)
            books.append(route(row,[int(data[0]),int(data[1])],[int(data[2]),int(data[3])],int(data[4]),int(data[5])))

        #Lista de vehiculos disponibles
        vehicles = []
        for num in range(num_vehicles):
            vehicles.append(vehicle())

    return rows, columns, vehicles, rides, bonus, steps, books

def getOutputFile(vehicles):
    output = open("output.txt","w+")
    print(vehicles)
    for veh in vehicles:
        output.write("{}\n".format(veh))
    output.close()

def main():

    rows, columns, vehicles, rides, bonus, steps, books = read_input("a_example.in")

    #Mientras puedas hacer rutas o tengas tiempos
    surrender = False
    current_step = 0
    score = 0

    print("COCHES:",vehicles)
    print("RUTAS",books)
    while (current_step < steps) and not surrender:
        #Haces cosas
        # 1 - Encuentras 1 ruta a hacer
        for vehicle in vehicles:
            #if vehicle.moving:
            #    break
            #Si el coche está libre
            if vehicle.route is None:
                for route in books:
                    if route.state != 1:
                        #Por cada ruta se mira si puede hacerla a tiempo
                        #onTime(self, step_now, new_route):
                        if vehicle.onTime(current_step, route):
                            vehicle.route = route
                            route.state = 1
                            break
                        else:
                            print("No on time")

        # 2 - Mover vehículos
        for vehicle in vehicles:
            if vehicle.route is not None:
                vehicle.check(current_step)

        current_step += 1

    getOutputFile(vehicles)

if __name__ == "__main__":
    main()
