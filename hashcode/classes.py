
class vehicle():

    def __init__(self, pos=[0,0], route=None):
        self.pos = pos
        self.route = route

    def onTime(self, step_now, new_route):
        #Distancia al punto origen
        distToStart = abs(self.pos[0] - new_route.start[0]) + abs(self.pos[1] - new_route.start[1])
        #Distancia total de hacer esa ruta
        total_steps = distToStart + new_route.manhattan()
        #Si el total de pasos es mayor que el step
        #límite para obtener recompensa, pasamos de la ruta
        if total_steps+step_now > new_route.last_step:
            return False
        else:
            return True


class route():
    def __init__(self, start_node, finish_node, start_time, finish_time):
        self.start_node = start_node
        self.finish_node = finish_node
        self.start_time = start_time
        self.finish_time = finish_time

    def manhattan(self):
        return (abs(self.start_node[0]-self.finish_node[0])+abs(self.start_time[1]-self.finish_time[1]))
