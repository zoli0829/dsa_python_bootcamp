# A list is a data structure that holds an ordered collection of items.
# The main difference between a list and an array is that the elements dont have to be the same data type.

integers = [1,2,3,4]
stringList = ['Milk', 'Cheese', 'Butter']
mixedList = [1, 1.5, 'map']
nestedList = [1,2,3,4,5, [1.5, 1.6], ['test']]
empty = []

print(integers)
print(stringList)
print(mixedList)
print(nestedList)
print(empty)

# Accessing/Traversing the list
print('ACCESSING AND TRAVERSING')
shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[0])
# starts from the back 
print(shoppingList[-1])
# returns if there is 'Milk' in he list
print('Milk' in shoppingList)

# TRAVERSAL
print('TRAVRSING')
for i in shoppingList:
    print(i)

# range, stop value is not inclusive
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList[i])

# this wont print out anything
empty = []
for i in empty:
    print('Empty')

#Update/Insert List
print('UPDATE')
myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
myList[4] = 55
print(myList)
# Time complexity is o(1) because we just use the index, space complexity is o(1)

#Insertion
print('INSRTION')
print(myList)
myList.insert(0, 11) # o(n) time complexity, o(1) space complexity
print(myList)

myList.append(55) # o(1) time complexity, o(1) space complexity
print(myList)

newList = [11,12,13,14]
myList.extend(newList) # o(n) time complexity, o(n) space complexity
print(myList)

#Slice
print('SLICE')
myList2 = ['a', 'b', 'c', 'd', 'e', 'f']
# exclude everything from the 2nd index
print(myList2[0:2])
# starts from the 1st element and continues until the last element
print(myList2[1:])
# update multiple elements with slicing
myList2[0:2] = ['x', 'y']
print(myList2)

#Delete
print('Delte')
# deletes the last element or the element at the provided index
# pop also returns the removed element
myList2.pop() # o(1)/ o(n)
print(myList2)

del myList2[3]
del myList2[2:4]
print(myList2) #o(n)
print(myList2)

myList2.remove('x') # o(n)
print(myList2)
print(myList2)
# space complexity for all these delete methods is o(1)