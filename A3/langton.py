#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:52:55 2020

Langton's ant implementation

        ---> +x
   XXXXXXXX
   XXX0XXXX
 | XXXXXXXX
 | XXXXXXXX
 ↓
 +y
 
     0d
 270d  90d
    180d
 

@author: isaiah
"""
import numpy as np

class LangtonsAnt:
    def __init__(self, N=256, colourCount=2, TurnSeq="LR"):
        self.grid = np.zeros((N,N), np.uint)
        self.x = int(N/2)
        self.y = int(N/2)
        self.bearing = 0;
        self.colourCount = colourCount
        self.turnSeq = TurnSeq
        
    def getStates(self):
        return self.grid
    
    def changeFloorValue(self, current):
        newValue = (current + 1) % self.colourCount
        self.grid.itemset((self.x, self.y), newValue)
    
    def update(self):
        currentFloorValue = self.grid.item((self.x, self.y))
        # Change current floor colour
        self.changeFloorValue(currentFloorValue)
        # move to next spot
        self.advanceAnt(self.turnSeq[currentFloorValue])
            
    def advanceAnt(self, antDirn):
        if antDirn == "L":
            # minus 90 degrees from ant heading
            self.bearing -= 90 
        elif antDirn == "R":
            self.bearing += 90
        
        self.bearing = self.bearing % 360

        # Ant facing upwards
        if self.bearing == 0:
            self.x += 0
            self.y += 1
        # Ant facing right
        elif self.bearing == 90:
            self.x += 1
            self.y += 0
        # Ant facing downwards
        elif self.bearing == 180:
            self.x += 0
            self.y += -1
        # Ant facing left
        elif self.bearing == 270:
            self.x += -1
            self.y += 0
        
    

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
