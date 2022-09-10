# 2D lists are very powerful and have a lot of application in data science and machine learning.
# A 2D list is like we have an array or a matrix in mathematics, we can define a matrix as below

matrix = [[1,8,9],[4,7,1],[4,7,4]]

# We can access individual items in the following manner

print(matrix[0][2])

# We can use the same index to modify the individual elements of the list

matrix[2][1] = 20

print (matrix[2][1])

print(matrix)                   # We can also print the complete matrix

# to Access all individual items in the matrix, we can use nested for loops like below

for rows in matrix:
    for item in rows:
        print(item)        
