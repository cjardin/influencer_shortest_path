import random
NAMES = []
#load a list of names 
with open("names", "r") as a:
    NAMES = a.read().split("\n")

TOTAL_POPULATION = 100
MAX_NODE_DEGREE = TOTAL_POPULATION / 2
MIN_NODE_DEGREE = TOTAL_POPULATION / 10

class Node:
    def __init__(self):
        self.neighbors = [] 
        self.weight = []  
        self.node_name = random.choice(NAMES) + "_" + random.choice(NAMES)
        self.visited = False

    def connect_vertices(self, vertices):
        #what should my node degree be?
        node_degree =  random.randint(MIN_NODE_DEGREE, MAX_NODE_DEGREE)
        for i in range( node_degree ):
            new_neighbor = random.choice(vertices)
            if new_neighbor not in self.neighbors:
                self.neighbors.append( new_neighbor )

    def distance_to_vertex(self, max_distance, current_distance, visted_vertices, target_vertex):
        if self == target_vertex:
            return current_distance

        if current_distance >= max_distance:
            return -1

        if self in visted_vertices:
            return -2
        visted_vertices.append(self)

        for vertex in self.neighbors:
            if vertex == target_vertex:
                return current_distance + 1
            r_value = vertex.distance_to_vertex(max_distance, current_distance + 1, visted_vertices, target_vertex)
            if r_value > 0 :
                return r_value
        return -3
        

def dijkstra ( input_vertices, start_vertex ):
    while True:
        for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]





vertices = []

for i in range(TOTAL_POPULATION):
    vertices.append( Node() )

for vertex in vertices:
    vertex.connect_vertices(vertices)
    vertex.visited



print(vertices[0].node_name)
print(f"has a node degree of { len(vertices[0].neighbors) } " )
#for vertex in vertices[0].neighbors:
#    print( vertex.node_name) 

