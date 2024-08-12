# Question 2
# Leetcode 1
# Find Pairs - Two Sum
# Write a program to find all pairs of integers whose sum is equal to a given number
# [2,6,3,9,11] 9 ---> [6,3]

# Questions to ask:
    # Does the array contain only positive or negative numbers?
    # What if the same pair repeats twice, should we print it every time?
    # If the reverse of the pair is acceptable e.g. can we print both (4,1) and (1,4) if the given sum is 5.
    # Do we need to print only distinct pairs? does (3,3) is valid pair for given sum of 6?
    # How big is the array?

# pairs have to be distinct

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]: # this part is to ensure we have distinct pairs
                continue
            elif nums[i] + nums[j] == target:
                print(i,j)

myList = [1,2,3,2,3,4,5,6]
findPairs(myList, 6)

""""
def findPairs(nums, target):
This line defines a function named findPairs that takes two arguments:

nums: A list of numbers.
target: The target sum that we're trying to find by adding two distinct numbers from the list.
Outer Loop
    for i in range(len(nums)):
This loop iterates over the entire list nums using the index i. The loop will start at the first element and go through each element one by one.

Inner Loop
        for j in range(i+1, len(nums)):
This inner loop starts from the element right after i (i.e., i+1) and goes to the end of the list. This ensures that every pair of numbers is considered only once (i.e., no duplicate pairs).

Condition to Ensure Distinct Pairs
            if nums[i] == nums[j]: # this part is to ensure we have distinct pairs
                continue
This condition checks if the elements at indices i and j are the same. If they are the same, the loop skips the rest of the code in the current iteration with continue and moves on to the next iteration. This ensures that we only consider distinct pairs (i.e., pairs where the two numbers are different).

Checking the Sum
            elif nums[i] + nums[j] == target:
                print(i, j)
If the sum of nums[i] and nums[j] equals the target, the function prints the indices i and j. This means that the pair of numbers at these indices adds up to the target sum.


Example Execution
myList = [1,2,3,2,3,4,5,6]
findPairs(myList, 6)
The list myList is [1, 2, 3, 2, 3, 4, 5, 6], and we're looking for pairs of distinct elements that sum to 6.

Let's walk through the iterations of the loops:

i=0, nums[i]=1

j=1, nums[j]=2 → 1 + 2 = 3 (Not equal to 6)
j=2, nums[j]=3 → 1 + 3 = 4 (Not equal to 6)
j=3, nums[j]=2 → 1 + 2 = 3 (Not equal to 6)
j=4, nums[j]=3 → 1 + 3 = 4 (Not equal to 6)
j=5, nums[j]=4 → 1 + 4 = 5 (Not equal to 6)
j=6, nums[j]=5 → 1 + 5 = 6 (This is a match! print(0, 6) is called)
j=7, nums[j]=6 → 1 + 6 = 7 (Not equal to 6)
i=1, nums[i]=2

j=2, nums[j]=3 → 2 + 3 = 5 (Not equal to 6)
j=3, nums[j]=2 → 2 + 2 = 4 (Skip because nums[i] == nums[j])
j=4, nums[j]=3 → 2 + 3 = 5 (Not equal to 6)
j=5, nums[j]=4 → 2 + 4 = 6 (This is a match! print(1, 5) is called)
j=6, nums[j]=5 → 2 + 5 = 7 (Not equal to 6)
j=7, nums[j]=6 → 2 + 6 = 8 (Not equal to 6)
i=2, nums[i]=3

j=3, nums[j]=2 → 3 + 2 = 5 (Not equal to 6)
j=4, nums[j]=3 → 3 + 3 = 6 (Skip because nums[i] == nums[j])
j=5, nums[j]=4 → 3 + 4 = 7 (Not equal to 6)
j=6, nums[j]=5 → 3 + 5 = 8 (Not equal to 6)
j=7, nums[j]=6 → 3 + 6 = 9 (Not equal to 6)
i=3, nums[i]=2

j=4, nums[j]=3 → 2 + 3 = 5 (Not equal to 6)
j=5, nums[j]=4 → 2 + 4 = 6 (This is a match! print(3, 5) is called)
j=6, nums[j]=5 → 2 + 5 = 7 (Not equal to 6)
j=7, nums[j]=6 → 2 + 6 = 8 (Not equal to 6)
i=4, nums[i]=3

j=5, nums[j]=4 → 3 + 4 = 7 (Not equal to 6)
j=6, nums[j]=5 → 3 + 5 = 8 (Not equal to 6)
j=7, nums[j]=6 → 3 + 6 = 9 (Not equal to 6)
i=5, nums[i]=4

j=6, nums[j]=5 → 4 + 5 = 9 (Not equal to 6)
j=7, nums[j]=6 → 4 + 6 = 10 (Not equal to 6)
i=6, nums[i]=5

j=7, nums[j]=6 → 5 + 6 = 11 (Not equal to 6)
Final Output
The function prints the following index pairs that add up to 6:

(0, 6)
(1, 5)
(3, 5) 
"""