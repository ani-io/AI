def solve_n_queens(n):
    board = [-1] * n  # board[i] = column of queen in row i
    solutions = []

    def is_safe(row, col):
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions

# Display the solutions
n = 4
results = solve_n_queens(n)
print(f"Total solutions: {len(results)}")
for sol in results:
    for i in sol:
        print("." * i + "Q" + "." * (n - i - 1))
    print()
