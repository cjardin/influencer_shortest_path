import pprint
import sys
"""
WHITE = HAS NOT
GREY = Working on it
Black = None
"""

intervals = [ {"start" : 0, "end" : 10 },
              {"start" : 1, "end" : 3},
              {"start" : 2, "end" : 20},
              {"start" : 9, "end" : 18},
              {"start" : 12, "end" : 15},
              {"start" : 16, "end" : 23},
              {"start" : 22, "end" : 25}
            ]

colors = {}


            

def interval_rec_coloring(G, start):

    colors[start] = "GREY"

    colors_taken = []
    for v in  range( start, len(G) ):
        #don't go further than the end of our interval
        if G[start]['end'] <  G[v]['start']:
            break

        if v not in colors:
            result = interval_rec_coloring(G, v)
            node_color =  result['node_color']
            colors_taken.append( node_color )
        else:
            colors_taken.append(  colors[v] )

    my_color = None
    for i in range( len(G) ): #MAX node Deg is the total number of intervals 
        if i not in colors_taken:
            my_color = i
            break

    colors[start] = my_color
    return { "node_color" : my_color}

#Merge sort by start
intervals.sort(key=lambda s: s['start'] )

interval_rec_coloring(intervals, 0 ) 

for i in range(len(intervals)):
    print( intervals[i], colors[i] )





