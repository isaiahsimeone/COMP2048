========================== Question 1B ==========================

The glider appears to work since the structure stays alive
as it moves across the grid  

========================== Question 1C ==========================

The glider gun itself was setting four cells as alive when they should not
have been. This caused the glider gun to launch one glider, but then break itself

========================== Question 2D ==========================

Langton’s Ant is Turing complete if it can be used to emulate a Turing machine. A Turing
machine at its core requires the following:

    1. A tape divided into cells, one next to the other. Each cell contains some value from a
    specified alphabet.

    2. A read/write head that can write or erase symbols from the aforementioned tape. And
    moves along the tape or the tape moves passed the head.

    3. A finite set of instructions

    4. A way to store the state of the Turing machine.

For Langton’s Ant to be Turing complete, we have to argue for each of the four points.

    1. Langton’s Ant is implemented on a square lattice that can be theoretically infinitely large.
    Since each square in the lattice is next to eachother, and each cell contains a value (in the form
    of a colour) obtained from a specific alphabet (input colour set). Langton’s ant satisfies this
    property. (in fact, since Langton’s Ant is implemented on a 2D square lattice, it satisfies a
    condition of being a two-dimensional Turing machine.)

    2. Langton’s Ant is able to make decisions according to a set of instructions. For example, if the
    ant is on a ‘black’ cell, then it can decide to turn 90 degrees left or right and proceed to the next
    instruction.

    3. Langton’s Ant accepts a finite set of instructions in the form of L/R inputs (e.g. if on a white
    square, turn left.)

    4. Langton’s ant changes to a new state in such a way that the next depends only on the state
    which the ant is currently in (i.e. the colour of the square which the ant is occupying)
    
Hence, with these observations. I believe that Langton’s Ant is Turing complete.
Furthermore, it was shown in the year 2000 that not only is Langton’s Ant Turing complete, it
is also a Universal Turing Machine [1]



[1] A. Gajardo, A. Moreira, E. Goles, Complexity of Langton’s ant, in: Final version in Discrete
Applied Mathematics, Vol. 117, Issue 1-3, pp. 41-50 (2002)

44340120