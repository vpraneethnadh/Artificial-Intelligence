Q = int(input("Enter the number of queens to be placed: "))

board = [[0] * Q for _ in range(Q)]


def AttackQueen(i, j):
    for k in range(0, Q):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    for k in range(0, Q):
        for l in range(0, Q):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False


def NQueens(n):
    if n == 0:
        return True
    for i in range(0, Q):
        for j in range(0, Q):
            if (not (AttackQueen(i, j))) and (board[i][j] != 1):
                board[i][j] = 1
                if NQueens(n - 1):
                    return True
                board[i][j] = 0
    return False


NQueens(Q)
print("\nAfter placing the Queens of your choice on the board: ")
for i in board:
    print(i)
