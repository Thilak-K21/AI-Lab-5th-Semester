import random

def display(a):
  print('|',a[0],'|',a[1],'|',a[2],'|')
  print('|',a[3],'|',a[4],'|',a[5],'|')
  print('|',a[6],'|',a[7],'|',a[8],'|')

arr=["-","-","-","-","-","-","-","-","-"]
visited=[0,0,0,0,0,0,0,0,0]
win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def check_win(a, player):
    char = 'X' if player == 1 else 'O'
    for condition in win:
        if a[condition[0]] == char and a[condition[1]] == char and a[condition[2]] == char:
            return True
    return False

def tictactoe(a,n,player):
  if (visited[n-1]!=1):
      arr[n-1]='X' if player == 1 else 'O'
      visited[n-1]=1
      display(arr)
      return True
  else:
    print("Invalid move" )
    return False

def tictactoee(a,n,player):
  if (visited[n-1]!=1):
      arr[n-1]='X' if player == 1 else 'O'
      visited[n-1]=1
      display(arr)
      return True
  else:
    while(1):
      print("Invalid move")
      n=int(input("Re-Enter the position "))
      if (visited[n-1]!=1):
        arr[n-1]='X' if player == 1 else 'O'
        visited[n-1]=1
        display(arr)
        break



size=9
count=0

display(arr)

while(count<size):
  player=1
  print("Player 1 :")
  p1=int(input("Enter the position you want to insert : "))
  if tictactoe(arr,p1,player):
    count+=1
    if check_win(arr, player):
        print("Player 1 won!")
        break
    if (count==size):
      print("It's a draw!")
      break
  else:
    p1=int(input("Enter the position you want to insert : "))
    tictactoee(arr,p1,player)

  if (count==size):
    break

  player=2
  print("Player 2 :")
  p2=int(input("Enter the position you want to insert : "))
  if tictactoe(arr,p2,player):
    count+=1
    if check_win(arr, player):
        print("Player 2 won!!!!!!")
        break
    if (count==size):
      print("It's a draw!!")
      break
  else:
    p2=int(input("Enter the position you want to insert : "))
    tictactoee(arr,p2,player)













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

def dfs_limited(start, limit):
    stack = [(start, [])]
    visited = set()
    while stack:
        current, path = stack.pop()
        if current == goal:
            return path + [current]
        if len(path) >= limit:
            continue
        key = board_to_string(current)
        if key in visited:
            continue
        visited.add(key)
        for neighbor in get_neighbors(current):
            stack.append((neighbor, path + [current]))
    return None

def iterative_deepening_dfs(start, max_depth=20):
    for depth in range(max_depth):
        result = dfs_limited(start, depth)
        if result:
            return result
    return None

start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

solution = iterative_deepening_dfs(start)
print(type(solution))

if solution:
    print("Solution steps:")
    for step in solution:
        for row in step:
            print(row)
else:
    print("No solution found.")
