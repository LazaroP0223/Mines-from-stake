import random
rows, cols = (5, 5)
arr = [[0]*cols]*rows
gemCount = 0
gemMax = 1

print(arr)
def gemRandomization(array):

    for i in range (5):
        for j in range(5):
            isGemquestion = 1
            if (isGemquestion == 1 & gemCount <= gemMax):
                 arr[i][j] =  isGemquestion

gemRandomization(arr)
for i in range (5):
        for j in range(5):
            print(arr[i][j], end = " ")