import numpy as np

# both dat structures are mutable
# boh can be indexed and iterated through
# they can be both sliced

# arrays are optimized for arithmetic operations
myArray = np.array([1,2,3,4,5,6]) # elements need to be the same data type
myList = [1,2,3,4,5,] # do not have to be the same data type

print(myArray / 2)
# print(myList / 2) this would return an error

# time and space complexity of lists
'''
operation                           time complexity                         space complexity
creating an empty list                  o(1)                                    o(1)
creating a list with elements           o(n)                                    o(n)
inserting a value in a list             o(n)                                    o(1)
traversing a list                       o(n)                                    o(1)
accessing a given cell in a list        o(1)                                    o(1)
searching a given value in a list       o(n)                                    o(1)
deleting a value from list              o(1)                                    o(1)
'''

