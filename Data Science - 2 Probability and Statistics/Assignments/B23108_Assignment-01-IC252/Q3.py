#3.1
import numpy as np

mat = np . array ([[1 ,3 ,4 ,5 ,2] ,[1 ,5 ,2 ,4 ,3] ,[5 ,2 ,3 ,4 ,1 ,] ,[1 ,4 ,2 ,6 ,9] ,[4 ,5 ,2 ,1 ,7]])
def left_diagonal_sum ( mat : np . ndarray ) ->float :
    sum = 0
    i = 0
    j = 0
    while i<=4 and j<=4 :
        sum = sum + mat[i][j]
        i+=1
        j+=1
    return sum
def right_diagonal_sum ( mat : np . ndarray ) ->float :
    sum = 0
    i = 0
    j = 4
    while i<=4 and j>=0 : 
        sum = sum + mat[i][j]
        i+=1
        j-=1
    return sum
print (f'Left Diagonal Sum of { mat =} is { left_diagonal_sum (mat)}')
print (f'Left Diagonal Sum of { mat =} is { right_diagonal_sum (mat)}')

#3.2

def submatrix_3x4 ( mat : np . ndarray ) -> np . ndarray :
    array = np.array([mat[0:3,1:5]])
print (f'The desired submatrix of \n { mat } is \n { submatrix_3x4 ( mat )}')