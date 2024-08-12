# Question 1 - Missing Number
# Leetcode 1
# How to find the missing nmber in an integer array of 1 to 100?

# trick is using the sum of n serious eqution 
# 1+2+3+...+n = n*(n+1)/2
# n is the number of should be elements in the list, in the below case its 10


def findMissingNumber(array, n):
    sum1 = n*(n+1) / 2
    sum2 = sum(array)
    missingNumer = sum1 - sum2
    return missingNumer

print(findMissingNumber([1,2,3,4,5,6,7,8,10],10))