import pprint
import sys
"""
WHITE = HAS NOT
GREY = Working on it
Black = None
"""

bad_graph = {
        'A': {"color" : "WHITE" , "vertices" : ['B', 'D']},
        'B': {"color" : "WHITE" , "vertices" : ['A', 'D', 'C']},
        'C': {"color" : "WHITE" , "vertices" : ['B', 'D']},
        'D': {"color" : "WHITE" , "vertices" : ['A', 'C','E']},
        'E': {"color" : "WHITE" , "vertices" : []}
       }

graph = { 
        'A': {"color" : "WHITE" , "vertices" : ['B', 'D']},
        'B': {"color" : "WHITE" , "vertices" : ['A', 'D', 'C']},
        'C': {"color" : "WHITE" , "vertices" : ['B', 'D']},
        'D': {"color" : "WHITE" , "vertices" : ['A', 'C']}
       } 




def outerplanr_coloring(G, start):

    G[start]['color'] = "GREY"

    colors_taken = []
    max_color = 0
    for v in  G[start]['vertices'] :
        if G[v]['color'] == "WHITE":
            result          = outerplanr_coloring(G, v)
            node_color      = result['node_color']
            max_sub_color   = result['max_sub_color']

            if max_sub_color > max_color:
                max_color = max_sub_color
           
            #did we find out that we are not outerplanr?
            if node_color == 0:
                return {"node_color" : 0, "max_sub_color" : 0}
            colors_taken.append( node_color )
        else:
            colors_taken.append( G[v]['color'] )

    my_color = None
    #At max 3 color outerplanr
    for i in range(1,4): # 3 color, offset by 1 so 0 = error
        if my_color == None and i not in colors_taken:
            my_color = i
        elif max_color < i and i in colors_taken:
            max_color = i

    #Not Outerplanr
    if my_color == None:
        return {"node_color" : 0, "max_sub_color" : 0}

    G[start]['color'] = my_color
    return {"node_color" : my_color, "max_sub_color" : max_color}


def outerplanr_coloring_2_g(G, start):

    G[start]['color'] = "GREY"

    colors_taken = []
    max_color = 0
    node_degree = 0
    for v in  G[start]['vertices'] :
        if G[v]['color'] == "WHITE":
            result          = outerplanr_coloring_2_g(G, v)
            node_color      = result['node_color']
            max_sub_color   = result['max_sub_color']

            if max_sub_color > max_color:
                max_color = max_sub_color

            #did we find out that we are not outerplanr?
            if node_color == 0:
                return {"node_color" : 0, "max_sub_color" : 0, "is_2_core" : result['is_2_core'] }
            colors_taken.append( node_color )
        else:
            colors_taken.append( G[v]['color'] )
        node_degree += 1


    #2-core .. if we have ANY nodes < node degree of 2, then we are not a 2-degenerate graph
    if node_degree < 2:
        return {"node_color" : 0, "max_sub_color" : 0, "is_2_core" : False}    


    my_color = None
    #At max 3 color outerplanr
    for i in range(1,4): # 3 color, offset by 1 so 0 = error
        if my_color == None and i not in colors_taken:
            my_color = i
        elif max_color < i and i in colors_taken:
            max_color = i 

    #Not Outerplanr
    if my_color == None:
        return {"node_color" : 0, "max_sub_color" : ">3" , "is_2_core" : False}

    G[start]['color'] = my_color
    return {"node_color" : my_color, "max_sub_color" : max_color,  "is_2_core" : True}
        


print( outerplanr_coloring(graph, "A") )
pprint.pprint(graph)

#print( outerplanr_coloring_2_g( bad_graph , "A") )
#pprint.pprint(bad_graph)

#print( outerplanr_coloring_2_g( graph , "A") )
#pprint.pprint(graph)





