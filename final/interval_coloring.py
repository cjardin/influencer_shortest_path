import pprint
import sys
"""
WHITE = HAS NOT
GREY = Working on it
Black = None
"""

graph = {'B': {"color" : "WHITE" , "location" : 0 , "vertices" : ['A', 'C']},
        'A': {"color" : "WHITE" , "location" : 1 , "vertices" : ['B', 'C', 'D']},
        'C': {"color" : "WHITE" , "location" : 2 , "vertices" : ['B', 'A', 'D', 'E']},
        'D': {"color" : "WHITE" , "location" : 3 , "vertices" : ['A', 'F', 'C', 'E']},
        'E': {"color" : "WHITE" , "location" : 4 , "vertices" : ['C', 'D']},
        'F': {"color" : "WHITE" , "location" : 5 , "vertices" : ['D', 'G', 'C']},
        'G': {"color" : "WHITE" , "location" : 6 , "vertices" : ['F']}
        }


#Sort the nodes by location on the timeline
sorted_nodes = {k: v for k, v in sorted(graph.items(), key=lambda item: -item[1]['location'])}

print(sorted_nodes)
sys.exit()


        

def outerplanr_coloring(G, start):

    G[start]['color'] = "GREY"

    colors_taken = []
    for v in  G[start]['vertices'] :
        if G[v]['color'] == "WHITE":
            node_color =  outerplanr_coloring(G, v)
           
            #did we find out that we are not outerplanr?
            if node_color == 0:
                return 0
            colors_taken.append( node_color )
        else:
            colors_taken.append( G[v]['color'] )

    my_color = None
    #At max 3 color outerplanr
    for i in range(1,4): # 3 color, offset by 1 so 0 = error
        if i not in colors_taken:
            my_color = i
            break

    #Not Outerplanr
    if my_color == None:
        return 0

    G[start]['color'] = my_color
    return my_color
        


print( outerplanr_coloring(graph, "C") )

pprint.pprint(graph)





