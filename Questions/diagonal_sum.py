# Given 2D list calculate the sum of diagonal elements.
# The diagonal element is the one where the row and column indices are the same (i.e., matrix[i][i]).
matrix= [[1,2,3],[4,5,6],[7,8,9]]

def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0
 
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
 
    return total

print(diagonal_sum(matrix))