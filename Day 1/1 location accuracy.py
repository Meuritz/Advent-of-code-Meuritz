import numpy as np


def location_Accuracy(list1, list2):
    
    #initizialize a varible to store the "accuracy"
    difference = 0
    
    #until there are no more elements in the first list
    while len(list1) != 0:
        
        #we take the minimum element from each list and remove it from it at the same time
        x = list1.pop(list1.index(min(list1)))
        y = list2.pop(list2.index(min(list2)))

        #we do the difference and we add it to difference value
        difference += abs(x - y)
    
    return difference 


#here we take the numbers from the file
data = np.genfromtxt("input.txt", dtype="int")

left = []
right = []

for row in data:
    left.append(row[0])
    right.append(row[1])

print(location_Accuracy(left, right))



