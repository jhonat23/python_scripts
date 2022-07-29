"""
Sean invented a game involving a 2nx2n matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the nxn submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for  matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.
data input:
1
2
112 42 83 119
56 125 56 49
15 78 101 43
62 98 114 108
"""

def flippingMatrix(matrix):
    res = []
    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            res.append(max(matrix[i][j], matrix[i][len(matrix)-1-j],matrix[len(matrix)-1-i][j], matrix[len(matrix)-1-i][len(matrix)-1-j]))
    return sum(res)
    # Write your code here

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)