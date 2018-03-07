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
    for veh in vehicles:
        output.write("{}\n".format(veh))
    output.close()

def orderVehicles(veh):
    if veh.route is not None:
        return 1
    else:
        return 0

def orderRoutes(route):
    return route.start_time

def main():

    files = ["a_example.in", "b_should_be_easy.in", "c_no_hurry.in", "d_metropolis.in", "e_high_bonus.in"]

    for f in files[4:]:
        print(f)
        rows, columns, vehicles, rides, bonus, steps, books = read_input(f)

        #Mientras puedas hacer rutas o tengas tiempos
        surrender = False
        current_step = 0
        score = 0

        #print("COCHES:",vehicles)
        #print("RUTAS",books)
        moments = []
        books.sort(key=orderRoutes)
        while (current_step < steps) and len(books) > 0: # and books[0].state == 0:
            if current_step % 10000 == 0:
                print("ESTOY EN {}".format(current_step))
            #Haces cosas
            # 1 - Encuentras 1 ruta a hacer
            #vehicles.sort(key=orderVehicles)
            for vehicle in vehicles:
                if vehicle.route is not None:
                    continue
                #Si el coche está libre
                if vehicle.route is None:
                    for i in range(len(books)):
                        #Por cada ruta se mira si puede hacerla a tiempo
                        #onTime(self, step_now, new_route):
                        if books[i].state == 0 and vehicle.onTime(current_step, books[i]):
                            moments.append(books[i].finish_time)
                            vehicle.route = books[i]
                            books[i].state = 1
                            books.pop(i)
                            break
                            #aux_reward = vehicle.getReward(current_step, route)
                            #if aux_reward > reward:
                            #    reward = aux_reward
                            #    possibleRoute = route
                        #else:
                            #print("No on time")
                    #print("COCHE {} COGE RUTA {}".format(vehicle.id, route))
                    #if possibleRoute is not None:
                    #    vehicle.route = possibleRoute
                    #    possibleRoute.state = 1

            #books.sort(key=orderRoutes)
            if len(moments) > 0:
                moments.sort()
                print("FROM CURRENT {}".format(current_step))
                current_step = moments.pop(0)
                print("TO CURRENT {}".format(current_step))

            # 2 - Mover vehículos
            for vehicle in vehicles:
                if vehicle.route is not None:
                    vehicle.check(current_step)

            current_step += 1

        getOutputFile(vehicles, f)

if __name__ == "__main__":
    main()
