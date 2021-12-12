import pprint
import sys
"""
WHITE = HAS NOT
GREY = Working on it
Black = None
"""

intervals = [ {"Name" : "A", "start" : 0, "end" : 10, "color" : "WHITE"},
              {"Name" : "B", "start" : 1, "end" : 3, "color" : "WHITE"},
              {"Name" : "C", "start" : 2, "end" : 20, "color" : "WHITE"},
              {"Name" : "D", "start" : 11, "end" : 18, "color" : "WHITE"},
              {"Name" : "E", "start" : 12, "end" : 15,"color" : "WHITE"},
              {"Name" : "F", "start" : 16, "end" : 23,"color" : "WHITE"},
              {"Name" : "G","start" : 22, "end" : 25,"color" : "WHITE"}
            ]


            

def interval_rec_coloring(G, start):

    G[start]['color'] = "GREY"

    colors_taken = []
    for v in  range( start, len(G) ):
        #don't go further than the end of our interval
        if G[start]['end'] <  G[v]['start']:
            break

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

intervals.sort(key=lambda s: s['start'] )
print( intervals )

print( interval_rec_coloring(intervals, 0 ) )
print( intervals )






