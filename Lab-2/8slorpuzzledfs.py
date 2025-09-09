goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def copy_board(board):
    return [row[:] for row in board]

def get_neighbors(board):
    x, y = find_zero(board)
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = copy_board(board)
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append(new_board)
    return neighbors

def board_to_string(board):
    return str(board)

def dfs(start, max_depth=20):
    stack = [(start, [])]
    visited = set()

    while stack:
        current, path = stack.pop()
        if current == goal:
            return path + [current]
        if len(path) >= max_depth:
            continue
        key = board_to_string(current)
        if key in visited:
            continue
        visited.add(key)
        for neighbor in get_neighbors(current):
            stack.append((neighbor, path + [current]))
    return None

start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

solution = dfs(start)
print(type(solution))

if solution:
    print("Solution steps:")
    for step in solution:
        for row in step:
            print(row)
        print("-----")
else:
    print("No solution found.")


