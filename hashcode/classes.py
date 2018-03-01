
class vehicle():

    def __init__(self, id,pos=[0,0], route=None):
        self.id = id
        self.pos = pos
        self.route = route
        self.routesDone = []
        self.eta = -1

    def onTime(self, step_now, new_route):
        #Distancia al punto origen
        distToStart = abs(self.pos[0] - new_route.start_node[0]) + abs(self.pos[1] - new_route.start_node[1])

        #Si hay que esperar, pa fuera
        if distToStart + step_now < new_route.start_time:
            return False

        #Distancia total de hacer esa ruta
        total_steps = distToStart + new_route.manhattan()
        self.eta = total_steps + step_now
        #Si el total de pasos es mayor que el step
        #límite para obtener recompensa, pasamos de la ruta
        if total_steps+step_now > new_route.finish_time:
            return False
        else:
            self.routesDone.append(new_route.id)
            return True

    def check(self, step_now):
        if self.eta != -1 and self.eta >= step_now:
            print("COCHE {} - FINALIZADA RUTA: {} EN STEP {}".format(self.id, self.route, step_now))
            self.pos = self.route.finish_node
            self.route = None
            return True
        else:
            return False

    def __repr__(self):
        return "{} {}".format(len(self.routesDone), self.routesDone.__str__().replace("[", "").replace("]", "").replace(",",""))


class route():
    def __init__(self, id, start_node, finish_node, start_time, finish_time):
        self.id = id
        self.start_node = start_node
        self.finish_node = finish_node
        self.start_time = start_time
        self.finish_time = finish_time
        self.state = 0 #0 = Pendiente, 1=Asignada

    def manhattan(self):
        return abs(self.start_node[0]-self.finish_node[0]) + abs(self.start_node[1]-self.finish_node[1])

    def __repr__(self):
        return "id:{}, start: {}, finish:{}, T0:{}, TF:{}, State:{}".format(self.id ,self.start_node ,self.finish_node ,self.start_time ,self.finish_time ,self.state)
