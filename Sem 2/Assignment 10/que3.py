#QUESTION 3

def print_square(square):
    for row in square:
        print(' '.join(f"{num:2}" for num in row))
    print()

def odd_magic_square(n):
    square = [[0]*n for _ in range(n)]
    i, j = 0, n // 2

    for num in range(1, n*n + 1):
        square[i][j] = num
        i -= 1
        j += 1
        if num % n == 0:
            i += 2
            j -= 1
        elif i < 0:
            i = n - 1
        elif j == n:
            j = 0
    return square

def doubly_even_magic_square(n):
    square = [[(n*i)+j+1 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i + j) % 4 == 3):
                square[i][j] = n*n + 1 - square[i][j]
    return square

def singly_even_magic_square(n):
    half = n // 2
    mini_square = odd_magic_square(half)
    square = [[0]*n for _ in range(n)]
    
    for i in range(half):
        for j in range(half):
            val = mini_square[i][j]
            square[i][j] = val
            square[i + half][j + half] = val + half*half
            square[i][j + half] = val + 2*half*half
            square[i + half][j] = val + 3*half*half

    k = (n - 2) // 4
    for i in range(n):
        for j in range(k):
            if i < half:
                square[i][j], square[i + half][j] = square[i + half][j], square[i][j]
        for j in range(n - k + 1, n):
            if i < half:
                square[i][j], square[i + half][j] = square[i + half][j], square[i][j]
    
    mid = k
    if n > 6:
        for i in range(half):
            square[i][mid], square[i + half][mid] = square[i + half][mid], square[i][mid]
    return square

def generate_magic_square(n):
    if n % 2 == 1:
        return odd_magic_square(n)
    elif n % 4 == 0:
        return doubly_even_magic_square(n)
    else:
        return singly_even_magic_square(n)

for n in range(4, 9):
    print("Magic Square of size", n,"\n")
    print_square(generate_magic_square(n))
