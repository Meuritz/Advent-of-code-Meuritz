import numpy as np

#we define the function to obtain the similarity score
def similarity(list1, list2):
    """
    Calculate the similarity score between two lists.
    The similarity score is calculated by counting the occurrences of each element 
    from the first list in the second list, then multiplying each element by its 
    occurrences and summing the results.
    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.
    Returns:
        int: The similarity score between the two lists.
    """

    #we initialize a dictionary that will store a number from list1 and it's occurencies
    occurencies = {}

    #we cycle for each element in the first list
    for x in list1:
        
        #we initialize a counter, to count the occurencies in the other list, of the actual number
        times = 0
        
        #we cycle the elements in the second list, if the element y it's same as the one passing in x, we increment the times 
        for y in list2:
            if x == y:
                times += 1
        #we add the key value pair that we found to the dictionary
        occurencies[x] = times

    #we initialize a variable for the similarity score
    similarity_score = 0
    
    #for each element in the first list, we multiply that number for it's occurencies stored in the dictionary
    for number in list1:

        #we use the number as a key to get the occurencies 
        similarity_score += number*occurencies[number]
    
    return similarity_score


#here we take the numbers from the file
data = np.genfromtxt("input.txt", dtype="int")

#initialize the list to store the values
left = []
right = []

# Loop through each row in the data, and assign the values to the list created previously
for row in data:
    
    left.append(row[0])
    right.append(row[1])

# Print the similarity score between the left and right lists
print(similarity(left, right))













