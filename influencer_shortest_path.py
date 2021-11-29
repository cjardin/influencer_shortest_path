from graph_tools import Graph, Node
from astar import astar_search
import random
import time

# The main entry point for this module
def main():
    # Create a graph
    print("Creating Graph")
    graph = Graph()

    #Total number of nodes we are going to create
    TOTAL_POPULATION = 500

    #The number of "friends" a non-influencer has
    NORMAL_MAX_NODE_DEGREE = 50
    NORMAL_MIN_NODE_DEGREE = 1 

    #The number of "friends" an influencer has
    INF_MAX_NODE_DEGREE = 400 
    INF_MIN_NODE_DEGREE = 100 


    print("Loading Names")
    NAMES = []
    #load a list of names 
    with open("names", "r") as a:
        NAMES = a.read().split("\n")

    #make list of people
    NAME_LIST = []
    for i in range(TOTAL_POPULATION):
        new_name = random.choice(NAMES) + "_" + random.choice(NAMES)
        if new_name not in NAME_LIST:
            NAME_LIST.append( new_name )


    heuristics = {}
    print("Connecting Population size of " + str(TOTAL_POPULATION))
    t1_start = time.time()
    #connect the people, Create a vertex for each person
    for n in NAME_LIST:
        #degree range = the node degree for the vertex
        degree_range = range(random.randint(NORMAL_MIN_NODE_DEGREE, NORMAL_MAX_NODE_DEGREE))
        if random.uniform(0, 1) >= .8: #meaning top 20% are influencers
            #make an influencer 
            degree_range = range(random.randint(INF_MIN_NODE_DEGREE, INF_MAX_NODE_DEGREE))

        adjacent_nodes = []
        for j in degree_range: 
            new_neighbor = random.choice(NAME_LIST)
            #Only connect to unique nodes
            if new_neighbor in adjacent_nodes:
                continue
            #Do not connect to myself 
            if new_neighbor == n :
                continue

            adjacent_nodes.append(new_neighbor)

            graph.connect(n, new_neighbor, 1) #1 = weight of connection
            heuristics[new_neighbor] = 1 # 1 = heuristic

    t1_stop = time.time()
    print("Elapsed time in Seconds:", t1_stop - t1_start)

    print("Setting graph to undirected")
    # Make graph undirected, create symmetric connections
    graph.make_undirected()


    #create ranked vertex list by node degree
    print("Ranking Max Degree")
    t1_start = time.time()
    ranked = {}
    for g in graph.nodes():
        ranked[g] = len(graph.get(g))

    #ranked = [node_name, node_degree]
    #Order ranked in order of highest to lowest
    ranked = {k: v for k, v in sorted(ranked.items(), key=lambda item: item[1],reverse=True)}

    t1_stop = time.time()
    print("Elapsed time in Seconds:", t1_stop - t1_start)


    print("Executing Algorithm")
    t1_start = time.time()
   

    #Find a random vertex that is not an influencer 
    random_start_vertex = None
    while random_start_vertex == None:
        test_vertex = random.choice(NAME_LIST)
        if len(graph.get(test_vertex)) < INF_MIN_NODE_DEGREE:
            random_start_vertex = test_vertex

    print(f"Starting Vertex -> {random_start_vertex} with node degree of {len(graph.get(random_start_vertex))}") 

    #walked the ranked, node degree list from highest node degree to least
    distance_to_max_influencer = None
    for vertex in ranked:

        print(f"Test {vertex} with node degree of {len(graph.get(vertex))}")

        #skip ourself 
        if vertex == random_start_vertex:
            continue
        
        path = astar_search(graph, heuristics, random_start_vertex , vertex)
        #path example = ['BAXTER_BRADY: 0', 'MCDANIEL_JACOBS: 1', 'MOSES_MOYER: 2']
        astar_cost_to_path = int(path[-1].split(':')[-1])

        #Have we found the path to the closest influencer?
        if distance_to_max_influencer != None and astar_cost_to_path > distance_to_max_influencer['cost_to_path'] :
            #winner!!!
            break
        elif distance_to_max_influencer == None or astar_cost_to_path < distance_to_max_influencer['cost_to_path']:
            #Shorter path than what we had before
            distance_to_max_influencer = {"vertex" :vertex, "cost_to_path" : astar_cost_to_path, "path" : path } 
        else:
            #If we are here.. Then we have a tie. And the first path in the tie has the highest node rank
            #so we do nothing!
            pass

        print("Path ---> " + str(path) )
    

    print("Ending Path from " + random_start_vertex + " to " + distance_to_max_influencer['vertex'] + " ==== " + str(distance_to_max_influencer['cost_to_path']))
    t1_stop = time.time()
    print("Elapsed time in Seconds:", t1_stop - t1_start)

if __name__ == "__main__": 
    main()

