import pprint
"""
WHITE = HAS NOT
GREY = Working on it
Black = None
"""

graph = {'A': {"color" : "WHITE" , "vertices" : ['B', 'D']},
         'B': {"color" : "WHITE" , "vertices" : ['A', 'D', 'C']},
         'C': {"color" : "WHITE" , "vertices" : ['B', 'D']},
         'D': {"color" : "WHITE" , "vertices" : ['C', 'B', 'A']}
        }

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
        


print( outerplanr_coloring(graph, "A") )

pprint.pprint(graph)





