import random
arr = [[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
gemCount = 0
gemMax = 24
myList = [1, 2, 3, 4, 0]

print(arr)
def gemRandomization(array, gCount, gMax):

    while gCount < gMax:
        x = random.choice(myList)
        y = random.choice(myList)
        
        if(array[x][y] != 1):
            gCount = gCount + 1
            array[x][y] = 1
                    

gemRandomization(arr,gemCount, gemMax)

print(arr)