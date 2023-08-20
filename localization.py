#Models a robot localizing itself within its environment.
#Belief of the presence of an object is modeled by probability.
p = [0.0, 0.5, 0.0, 0.0, 0.5]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOver = 0.1
pUnder = 0.1

#Changes probability of cell based off of what is in the cell.
def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        #if Z == world[i], hit = true = 1...
        q.append(p[i]*(hit*pHit + (1-hit)*pMiss))
    s = sum(q)
    for i in range(len(p)):
        q[i] = q[i]/s
    return q

#Moves cells based off a cyclic world. With list slicing [:], note that slicing, whether + or -,
#always moves from left to right.
def move(p, U):
    q = []
    #p[-U:] starts at index -U and ends at last index on the right (inclusive).
    #p[:-U] starts at first index on the left and ends at -U on the right (exclusive).
    p = p[-U:] + p[:-U]
    #Takes into account probability of inexact motion, if robot undershoots or overshoots a cell.
    for i in range(len(p)):
        q.append(p[i-1]*pUnder + p[i]*pExact + p[i-len(p)+1]*pOver)
    return q

#Updates probability for every time the robot senses red / green, and then moves n cells to the right.
for i in range(len(motions)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])

#Prints probability of objects in a location.
print(p)