# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal, ndimage

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.uint)
        self.neighborhood = np.ones((3,3), np.uint)
        self.neighborhood[1,1] = 0
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        
    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid
    
    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()
               
    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''
       
        #get weighted sum of neighbors
        #PART A & E CODE HERE
        if not self.fastMode: 
            """ DO IT SLOW """
            rowSize = self.grid.shape[0]
            colSize = self.grid.shape[1]
            
            kernel = np.ones((3,3), np.uint8)
            kernel[1,1] = 0 # zero center square 
            neighbourCounts = signal.convolve2d(
                    self.grid, 
                    kernel, 
                    mode='same', 
                    boundary='wrap', 
                    fillvalue=0)
            
            updatedGrid = np.zeros((rowSize, colSize), np.uint8)
            
            for row in range(rowSize):
                for col in range(colSize):
                    aliveNeighbours = neighbourCounts[row, col]
                    targetCell = self.grid.item(row, col)
    
                    if targetCell == self.aliveValue:
                        if aliveNeighbours < 2:
                            updatedGrid.itemset((row, col), self.deadValue)
                        elif aliveNeighbours == 2 or aliveNeighbours == 3:
                            updatedGrid.itemset((row, col), self.aliveValue)
                        elif aliveNeighbours > 3:
                            updatedGrid.itemset((row, col), self.deadValue)
                            
                    if targetCell == self.deadValue:
                        if aliveNeighbours == 3:
                            updatedGrid.itemset((row, col), self.aliveValue)
    
            # Update the grid
            self.grid = updatedGrid
        else:
            neighbours = signal.convolve2d(
                self.grid, 
                self.neighborhood, 
                # The output is the same size as in1, centered with respect to the ‘full’ output.
                mode='same', 
                boundary='wrap', 
                fillvalue=0)
            
            # If Any cell has two or three neighbours, it comes to life so we can do a logical or between
            # those two cases and use this information to update the grid faster 
            self.grid = np.logical_or(np.logical_and(self.grid, np.equal(neighbours, 2)), np.equal(neighbours, 3)).astype(int)
        
    

    def loadPattern(self, filename, index=(0,0)):
        colPos = -1
        rowPos = -1
        with open(filename, 'r') as pattern:
            for line in pattern:
                colPos = 0
                # skip commented lines
                if line[0] == "!":
                    next
                else:
                    rowPos += 1
                    # load the file cell by cell
                    for j in range(0, len(line)):
                        self.grid[rowPos + index[0], colPos + index[1]] = self.aliveValue if line[colPos] == "O" else self.deadValue
                        colPos += 1

    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        
    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue
        
    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+2, index[1]+24] = self.aliveValue
        self.grid[index[0]+2, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+15] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+23] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        self.grid[index[0]+3, index[1]+37] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+13] = self.aliveValue
        self.grid[index[0]+4, index[1]+17] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+23] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        self.grid[index[0]+4, index[1]+37] = self.aliveValue
        
        self.grid[index[0]+5, index[1]+2] = self.aliveValue    #### 1 -> 2
        self.grid[index[0]+5, index[1]+3] = self.aliveValue    #### 2 -> 3
        self.grid[index[0]+5, index[1]+12] = self.aliveValue
        self.grid[index[0]+5, index[1]+18] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        self.grid[index[0]+5, index[1]+23] = self.aliveValue
        
        self.grid[index[0]+6, index[1]+2] = self.aliveValue    #### 1 -> 2
        self.grid[index[0]+6, index[1]+3] = self.aliveValue    #### 2 -> 3
        self.grid[index[0]+6, index[1]+12] = self.aliveValue
        self.grid[index[0]+6, index[1]+16] = self.aliveValue
        self.grid[index[0]+6, index[1]+18] = self.aliveValue
        self.grid[index[0]+6, index[1]+19] = self.aliveValue
        self.grid[index[0]+6, index[1]+24] = self.aliveValue
        self.grid[index[0]+6, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+7, index[1]+12] = self.aliveValue
        self.grid[index[0]+7, index[1]+18] = self.aliveValue
        self.grid[index[0]+7, index[1]+26] = self.aliveValue
        
        self.grid[index[0]+8, index[1]+13] = self.aliveValue
        self.grid[index[0]+8, index[1]+17] = self.aliveValue
        
        self.grid[index[0]+9, index[1]+14] = self.aliveValue
        self.grid[index[0]+9, index[1]+15] = self.aliveValue
