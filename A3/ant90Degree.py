# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:52:55 2020

Langton's ant implementation

@author: isaiah
"""
import langton
from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 400     # 180 white, black, R,L interesting

"""
90 DEGREE HIGHWAYS     -    https://mathtician.weebly.com/langtons-ant.html  
"""

# The sequence of colours which the ant should set it's previous cell
# e.g. if the ant arrives to a white cell, it will be changed to black
ColourSeq = ["white",
            "black", 
            "red",
            "blue",
            "magenta",
            "yellow",
            "green",
            "orange",
            "gold",
            "purple",
            "aqua"]


# In order with colour sequence (e.g. white -> Right, black -> Left)
TurnSeq = "LRRRRLLLRRR"

############################################################################
updates = 0

ColMap = colors.ListedColormap(ColourSeq)
norm = colors.BoundaryNorm(list(range(len(ColourSeq) + 1)), ColMap.N)
#create the game of life object
ant = langton.LangtonsAnt(N, len(ColourSeq), TurnSeq)


cells = ant.getStates()

fig = plt.figure()


img = plt.imshow(cells, animated=True, cmap=ColMap, norm=norm)
plt.gcf().set_facecolor("black")
def animate(i):
    """perform animation step"""
    global ant
    global updates
    if updates % 1000 == 0:
        print(updates)
    updates += 1
    
    ant.update()
    cellsUpdated = ant.getStates()
    
    img.set_array(cellsUpdated)
    
    return img,

interval = 1 #ms

ani = animation.FuncAnimation(fig, animate, frames=1, interval=interval, blit=True)

plt.show()
