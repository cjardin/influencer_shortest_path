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

def interval_rec_coloring(G, start):

    G[start]['color'] = "GREY"

    colors_taken = []
    for v in  G[start]['vertices'] :
        if G[v]['color'] == "WHITE":
            result = interval_rec_coloring(G, v)
            node_color =  result['node_color']
            colors_taken.append( node_color )
        else:
            colors_taken.append( G[v]['color'] )

    my_color = None
    for i in range( len(G) ): #MAX node Deg is the total number of intervals 
        if i not in colors_taken:
            my_color = i
            break

    G[start]['color'] = my_color
    return { "node_color" : my_color}
        
sorted_nodes = {k: v for k, v in sorted(graph.items(), key=lambda item: item[1]['interval'])}

print( interval_rec_coloring(sorted_nodes, list(sorted_nodes.keys())[0]) )
print( sorted_nodes)






