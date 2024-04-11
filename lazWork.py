import random

#0's represent bombs, 1's gems
arr = [[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#current gems in the variable
gemCount = 0
# number of gems the user wants in the board
gemMax = 10
myList = [1, 2, 3, 4, 0]


def gemRandomization(array, gCount, gMax):

    while gCount < gMax:
        x = random.choice(myList)
        y = random.choice(myList)
        
        if(array[x][y] != 1):
            gCount = gCount + 1
            array[x][y] = 1
                    

gemRandomization(arr,gemCount, gemMax)

print(arr)