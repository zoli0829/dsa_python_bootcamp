# import everything from the array module
from array import *

# 1. Create an array and traverse it
array1 = array('i', [1,2,3,4,5])
for i in array1:
    print(i)
# The time complexity for this operation is 0(n), because we are traversing through all element

# 2. Access individual elements trough indexes
print('Step 2')
print(array1[0])
print(array1[3])
#

# 3. Append any value to the array using append() method
print('Step 3')
array1.append(6)
print(array1)
# The time complexity is o(1)

# 4. Insert value in an array using insert() method
print('Step 4')
array1.insert(3, 11)
print(array1)
# Its a very time consuming operation because the other elements have to shift to the right

# 5. Extend python array using extend() method with multiple elements
print('Step 5')
array1.extend([7,8,9])
print(array1)


# 6. Add items from list into array using fromlist() method
print('Step 6')
tempList = [20,21,22]
array1.fromlist(tempList)
print(array1)

# 7. Remove any array element using remove() method
print('Step 7')
array1.remove(11)
print(array1)
# Very time consuming, o(n) time complexity

# 8. Remove last array element using pop() method
print('Step 8')
array1.pop()
print(array1)
# o(1)

# 9. Fetch any element through its index using index() method
print('Step 9')
print(array1.index(21))

# 10. Reverse a python array using the reverse() method
print('Step 10')
array1.reverse()
print(array1)

# 11. Get array buffer information through buffer_inf() method
print('Step 11')
print(array1.buffer_info())

# 12. Check for number of occurences of an element using count() method
# in python it counts how many times the argument appears in the array, 
# unlike in most other languages where it counts the number of all elements
print('Step 12')
array1.append(7)
print(array1.count(7))
print(array1)

# 13. Convert array to a string using tostring() method
print('Step 13')
# strTemp = array1.tostring() # in python 3.9 and later thes was removed
print('strTemp = array1.tostring() # in python 3.9 and later thes was removed')

# 14. Convert array to a python list with same elements using tolist() method
print('Step 14')
# print(array1.tolist())

# 15. Append a string to char array using fromstring() method
print('Step 15')
# Its also deprecated in python 3.9 and later.

# 16. Slice elements from an array
print('Step 16')
print(array1[1:4])
# It starts from the first element and the 4th element is exlusive
print(array1[:4])
# It prints all the elements until the 4th index