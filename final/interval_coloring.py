import pprint
import sys
"""
WHITE = HAS NOT
GREY = Working on it
Black = None
"""

graph = {'B': {"color" : "WHITE" , "interval" : 0 , "vertices" : ['A', 'C']},
        'A': {"color" : "WHITE" , "interval" : 1 , "vertices" : ['B', 'C', 'D']},
        'C': {"color" : "WHITE" , "interval" : 2 , "vertices" : ['B', 'A', 'D', 'E']},
        'D': {"color" : "WHITE" , "interval" : 3 , "vertices" : ['A', 'F', 'C', 'E']},
        'E': {"color" : "WHITE" , "interval" : 4 , "vertices" : ['C', 'D']},
        'F': {"color" : "WHITE" , "interval" : 5 , "vertices" : ['D', 'G', 'C']},
        'G': {"color" : "WHITE" , "interval" : 6 , "vertices" : ['F']}
        }


def interval_coloring(G):

    #sort the graph.. Assume merge sort = O(n log n)
    sorted_nodes = {k: v for k, v in sorted(graph.items(), key=lambda item: item[1]['interval'])}
    print(sorted_nodes)

    #Create Jump list for loop..
    jump_list = {}
    for s in sorted_nodes:
        jump_list[ sorted_nodes[s]['interval'] ] = s

    #Get the maximum ...Theory is.. If we walk the interval from start to finish.. we are done!
    max_interval_node = sorted_nodes[list(sorted_nodes.keys())[-1]]

    #loop through all 
    largest_visited_interval = sorted_nodes[list(sorted_nodes.keys())[0]]['interval']
    while largest_visited_interval < max_interval_node['interval']:
        node_index = jump_list[largest_visited_interval]

        result =  interval_rec_coloring(G, node_index)
        largest_visited_interval = result['max_interval']

    return sorted_nodes
        

def interval_rec_coloring(G, start):

    G[start]['color'] = "GREY"

    colors_taken = []
    max_interval = G[start]['interval']
    for v in  G[start]['vertices'] :
        if G[v]['color'] == "WHITE":
            result = interval_rec_coloring(G, v)
            node_color =  result['node_color']
            if result['max_interval'] > max_interval:
                max_interval = result['max_interval']
            colors_taken.append( node_color )
        else:
            colors_taken.append( G[v]['color'] )

    my_color = None
    for i in range( len(G) ): #MAX node Deg is the total number of intervals 
        if i not in colors_taken:
            my_color = i
            break

    G[start]['color'] = my_color
    return { "node_color" : my_color, "max_interval" : max_interval}
        


print( interval_coloring(graph) )






