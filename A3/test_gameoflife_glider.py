# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""

import conway




"""
Uncomment loadPattern calls one at a time and set N accordingly
"""
N = 150 # SET SIZE HERE
life = conway.GameOfLife(N, False, True)

""" Blinker 20 """
#life.insertBlinker((0,0))
""" Glider (N = 50) """
#life.insertGlider((0,0))
""" Glider gun fixed (N = 50) """
life.insertGliderGun()
""" Pufferfish (N = 200) """
##############https://www.conwaylife.com/wiki/Pufferfish_spaceship
#life.loadPattern("pufferfish.cells", (100, 70))
""" 13 engine corder ship (N = 300)  """
##############https://conwaylife.com/wiki/13-engine_Cordership
#life.loadPattern("13enginecordership.cells", (100, 100))   
""" 3-engine Cordership gun (N = 1024)  """
##############https://www.conwaylife.com/wiki/3-engine_Cordership_gun
#life.loadPattern("3enginecordershipgun.cells", (500,500))
""" 6-engine Cordership gun (N = 1400)  """
##############https://conwaylife.com/wiki/6-engine_Cordership_gun
#life.loadPattern("6enginecordershipgun.cells", (100, 100));
""" Big p448 dart gun (N = 2400) """
##############https://www.conwaylife.com/wiki/P448_dart_gun
#life.loadPattern("p448.cells", (100, 100));

#------------------------------------------------------------------------#
cells = life.getStates() #initial state

#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)

def animate(i):
    """perform animation step"""
    global life
    
    life.evolve()
    cellsUpdated = life.getStates()
    
    img.set_array(cellsUpdated)
    
    return img,

interval = 100 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
