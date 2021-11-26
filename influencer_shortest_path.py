from graph_tools import Graph, Node
from astar import astar_search

# The main entry point for this module
def main():
    import random

    NAMES = []
    #load a list of names 
    with open("names", "r") as a:
        NAMES = a.read().split("\n")

    # Create a graph
    graph = Graph()

    TOTAL_POPULATION = 500
    NORMAL_MAX_NODE_DEGREE = 50
    NORMAL_MIN_NODE_DEGREE = 1

    INF_MAX_NODE_DEGREE = 400 
    INF_MIN_NODE_DEGREE = 100 

    
    heuristics = {}

    #make list of people
    NAME_LIST = []
    for i in range(TOTAL_POPULATION):
        NAME_LIST.append( random.choice(NAMES) + "_" + random.choice(NAMES) )

    #connect the people
    for n in NAME_LIST:
        #degree range = the node degree for the vertex
        degree_range = range(random.randint(NORMAL_MIN_NODE_DEGREE, NORMAL_MAX_NODE_DEGREE))
        if random.uniform(0, 1) >= .8: #meaning top 20% are influencers
            #make an influencer 
            degree_range = range(random.randint(INF_MIN_NODE_DEGREE, INF_MAX_NODE_DEGREE))

        for j in degree_range: 
            new_neighbor = random.choice(NAME_LIST)
            if new_neighbor == n :
                continue
            graph.connect(n, new_neighbor, 1) #1 = weight of connection
            heuristics[new_neighbor] = 1 # 1 = heuristic

    # Make graph undirected, create symmetric connections
    graph.make_undirected()


    #create ranked vertex list by node degree
    ranked = {}
    for g in graph.nodes():
        ranked[g] = len(graph.get(g))

    #Order ranked in order of highest to lowest
    ranked = {k: v for k, v in sorted(ranked.items(), key=lambda item: item[1],reverse=True)}

    #walked the ranked, node degree list from highest node degree to least
    random_start_vertex = random.choice(NAME_LIST)
    distance_to_max_influencer = None
    for vertex in ranked:
        #skip ourself 
        if vertex == random_start_vertex:
            continue
        path = astar_search(graph, heuristics, random_start_vertex , vertex)
        #path = ['BAXTER_BRADY: 0', 'MCDANIEL_JACOBS: 1', 'MOSES_MOYER: 2']
        cost_to_path = int(path[-1].split(':')[-1])

        #Have we found the path to the closest influencer?
        if distance_to_max_influencer != None and  distance_to_max_influencer[1] < cost_to_path:
            break
        if distance_to_max_influencer == None or distance_to_max_influencer[1] > cost_to_path:
            distance_to_max_influencer = [vertex, cost_to_path, path]
        #don't update on a tie
        print("Pathing ---> " + str(path) )
    

    print("Ending Path from " + random_start_vertex + " to " + distance_to_max_influencer[0] + " ==== " + str(distance_to_max_influencer[2]))

if __name__ == "__main__": 
    main()

