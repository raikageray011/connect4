board = [[" " for _ in range(7)] for _ in range(6)]

def draw_board():
  print("0 1 2 3 4 5 6")
  for row in board:
    print(" ".join(row))

def get_move(player):
  while True:
    try:
      col = int(input(f"{player}, enter column: "))
      if col in range(7):
        return col
      else:
        print("Invalid column. Please try again.")
    except ValueError:
      print("Invalid input. Please try again.")

def make_move(player, col):
  for i in range(6):
    if board[5-i][col] == " ":
      board[5-i][col] = player
      return
  print("Column is full. Please try again.")

def game_over():
  # Check for horizontal win
  for row in board:
    for i in range(4):
      if row[i] == row[i+1] == row[i+2] == row[i+3] and row[i] != " ":
        return row[i]
  # Check for vertical win
  for col in range(7):
    for i in range(3):
      if board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col] and board[i][col] != " ":
        return board[i][col]
  # Check for diagonal win
  for i in range(3):
    for j in range(4):
      if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] and board[i][j] != " ":
        return board[i][j]
      if board[i][6-j] == board[i+1][5-j] == board[i+2][4-j] == board[i+3][3-j] and board[i][6-j] != " ":
        return board[i][6-j]
  # Check for draw
  for row in board:
    if " " in row:
      return False
  return "Draw"

def play_game():
  draw_board()
  while not game_over():
    col = get_move("X")
    make_move("X", col)
    draw_board()
    if game_over():
      break
    col = get_move("O")
    make_move("O", col)
    draw_board()
  result = game_over()
  if result == "X":
    print("X wins!")
  elif result == "O":
    print("O wins!")
  else:
    print("It's a draw!")

play_game()
