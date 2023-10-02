
# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    position = int(position)
    board[position] = mark


# TODO: print the game board as described at the top of this code skeleton
# If a box is unoccupied, then print the number of that box
def printBoard():
    for k, v in board.items():
        if v == ' ':
            board[k] = str(k)
    for i in range(1, 10):
        print(board[i], end=' | ' if i % 3 != 0 else '\n')
        if i % 3 == 0 and i != 9:
            print("---------")


# TODO: vaidate for the following error, this function should return True or False.
# Wrong Input (invalid position, not entering a position)
# Out of bound position (smaller than 1, or larger than 9)
# The position is already occupied
def validateMove(position):
    position = str(position)
    if position.isdigit() == False:
        return False
    position = int(position)
    if position < 1 or position > 9:
        return False
    if board[position] == 'X' or board[position] == 'O':
        return False
    return True

# TODO: list out all the combinations of winning, you will neeed this
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 5, 9],
    [3, 5, 7],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],

]

# TODO: implement a logic to check if the previous winner just win
def checkWin(player):
    return any(all(board[pos] == player for pos in comb) for comb in winCombinations)


# TODO: implement a function to check if the game board is already full
def checkFull():
    return all(v == 'X' or v == 'O' for v in board.values())


#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
def switch_player(player):
    if player =='X':
        player = 'O'
    else:
        player = 'X'
    return(player)

def restartGame():
  global gameEnded
  restart = input("Do you want to restart the game? Y/N")
  if restart == 'Y' or restart == 'y':
    gameEnded = False
  else:
    exit()

def resetBoard():
  for k, v in board.items():
        if v == 'X' or v == 'O':
            board[k] = str(k)
  printBoard()

while True:
  gameEnded = False
  currentTurnPlayer = 'X'
# loop will continue execute as long as the condition 'gameEnded' is 'False'
# exit when 'gameEnded' becomes 'True'
  while not gameEnded:
      print("Please enter a number from 1-9.")
      move = input(currentTurnPlayer + "'s turn, input: ")
      if validateMove(move) == False:
          print("Invalid number.")
      else:
        markBoard(move, currentTurnPlayer)
        printBoard()
        if checkWin(currentTurnPlayer):
              print(currentTurnPlayer + " win the game.")
              gameEnded = True
        elif checkFull():
              print ("Tie")
              gameEnded = True
        else:
          currentTurnPlayer = switch_player(currentTurnPlayer)
  restartGame()
  resetBoard()
          
# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
