#QUESTION 1 AND 2

import numpy as np

def is_safe(board, row, col, n):
    
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def nqueen(board, row, n, ans):
    if row == n:
        ans.append(board.copy())
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            nqueen(board, row + 1, n, ans)
            board[row][col] = 0

n = int(input("Enter the size of the board (n): "))
board = np.zeros((n, n), dtype=int)
ans = []
nqueen(board, 0, n, ans)
print("Number of solutions: ", len(ans))
print("One solution is: ")
print(np.array(ans[0]))