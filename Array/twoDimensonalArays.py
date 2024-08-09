# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

print('PRINTING 2D ARRAY')
twoDArray = np.array([
    [11, 15, 10, 6], 
    [10, 14, 11, 5], 
    [12, 17, 12, 8], 
    [15, 18, 14, 9]])
print(twoDArray)

# Insertion
# Adding column
print('INSERTING A COLUMN')
# np.insert(array, index, elementsToInsert, column or row)
newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]],axis=1)
print(newTwoDArray)

# Adding row
print('INSERTING A ROW')
newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]],axis=0)
print(newTwoDArray)

# Append at the end
print('APPENDING AN ARRAY')
newTwoDArray = np.append(twoDArray, [[1,2,3,4]],axis=0)
print(newTwoDArray)

# Access an element
print('ACCESSING AN ELEMENT')
    # a[i][j] --> i is row index and j is column index

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):        # o(1)
        print('incorrect index')                                    # o(1)
    else:
        print(array[rowIndex][colIndex])                            # o(1)
    # time complexity is o(1) space complexity is o(1)
accessElements(twoDArray, 2, 3)

# Traversing 2D arrays
print('TRAVERSING AN ARRAY')

def traverse2DArray(array):
    # checks the rows
    for i in range(len(array)):                 # o(mn)
        # checks the columns                
        for j in range(len(array[0])):          # o(n)          time complexity is o(n2)
            print(array[i][j])                  # o(1)          space complexity is o(1)

traverse2DArray(twoDArray)

# Searching 2D array
print('SEARCHING')

def search2DArray(array, value):
    for i in range(len(array)):                 # o(mn)
        for j in range(len(array[0])):          # o(n)
            if array[i][j] == value:            # o(1)
                return 'The value is located at index ' + str(i) +' ' + str(j)
    return 'The element is not found'
# space complexity is o(1)

print(search2DArray(twoDArray, 55))

# Deletion
print('DELETION')

# time comlexity o(mn) because we need to copy the new array without the deleted row to a new array
# m is the number of columns and n is the number of rows
# space complexity o(mn)
print(twoDArray)

# delete first row of the array
new2DArray = np.delete(twoDArray, 0, axis = 0)
print(new2DArray)

# delete first column of the array
new2DArray = np.delete(twoDArray, 0, axis = 1)
print(new2DArray)

'''
Operation                       Time complexity                 Space Complexity
    Creating an empty array         o(1)                            o(1)
    Creating an array with elements o(mn)                           o(mn)
    Inserting a column/row in an array  o(mn)                       o(mn)
    Traversing a given array        o(mn)                           o(1)
    Accessing a given cell          o(1)                            o(1)
    Searching a given value         o(mn)                           o(1)
    Deleting a column/row           o(mn)                           o(mn)
'''

# When to use 
    # To store multiple variables of same data type
    # Random access
# When to avoid
    # same data type elements
    # reserve memory