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
            if len(data)>0:
                books.append(route(row,[int(data[0]),int(data[1])],[int(data[2]),int(data[3])],int(data[4]),int(data[5])))

        #Lista de vehiculos disponibles
        vehicles = []
        for num in range(num_vehicles):
            vehicles.append(vehicle(num))

    return rows, columns, vehicles, rides, bonus, steps, books

def getOutputFile(vehicles, file):
    output = open("output_{}.txt".format(file.replace(".in","")),"w+")
    print(vehicles)
    for veh in vehicles:
        output.write("{}\n".format(veh))
    output.close()

def orderVehicles(veh):
    if veh.route is not None:
        return 1
    else:
        return 0

def orderRoutes(route):
    if route.state != 0:
        return 1
    else:
        return 0


def main():

    files = ["a_example.in", "b_should_be_easy.in", "c_no_hurry.in", "d_metropolis.in", "e_high_bonus.in"]

    for f in files:
        rows, columns, vehicles, rides, bonus, steps, books = read_input(f)

        #Mientras puedas hacer rutas o tengas tiempos
        surrender = False
        current_step = 0
        score = 0

        print("COCHES:",vehicles)
        print("RUTAS",books)
        while (current_step < steps) and not books[0].state == 1:
            #Haces cosas
            # 1 - Encuentras 1 ruta a hacer
            vehicles.sort(key=orderVehicles)
            for vehicle in vehicles:
                if vehicle.route is not None:
                    break
                #Si el coche está libre
                if vehicle.route is None:
                    books.sort(key=orderRoutes)
                    for route in books:
                        if route.state != 0:
                            break
                        if route.state != 1:
                            #Por cada ruta se mira si puede hacerla a tiempo
                            #onTime(self, step_now, new_route):
                            if vehicle.onTime(current_step, route):
                                print("COCHE {} COGE RUTA {}".format(vehicle.id, route))
                                vehicle.route = route
                                route.state = 1
                                break
                            #else:
                                #print("No on time")

            # 2 - Mover vehículos
            for vehicle in vehicles:
                if vehicle.route is not None:
                    vehicle.check(current_step)

            current_step += 1

        getOutputFile(vehicles, f)

if __name__ == "__main__":
    main()
