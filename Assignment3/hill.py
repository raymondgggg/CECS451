from board import Board
import copy
import time

"""function that returns a list of tuples of the adjacent 
   spaces for a given space (x,y) of the board --> [(x1,y1), ... , (Xn, Yn)]"""
def get_adjacent_spaces(board, x, y):
    map = board.get_map()
    aIndices  = []

    if x > 0: # appends the index above (x,y)
        aIndices.append((x-1, y))
    if x-1 >= 0 and 0 <= y-1 < len(map): # appends the top left adjacent diagonal index 
        aIndices.append((x-1, y-1))
    if x-1 >= 0 and y+1 < len(map): # appends the top right adjacent diagonal index
        aIndices.append((x-1, y+1))
    if x+1 < len(map): # appends the index below (x,y)
        aIndices.append((x+1, y))
    if x+1 < len(map) and 0 < y-1 < len(map): # appends the bottom left adjacent diagonal index
        aIndices.append((x+1, y-1))
    if x+1 < len(map) and y+1 < len(map): # appends the bottom right adjacent diagonal index
        aIndices.append((x+1, y+1))
    if y > 0: # appends the index to the left 
        aIndices.append((x,y-1))
    if y+1 < len(map):
        aIndices.append((x,y+1))

    return aIndices
    
"""This function returns 
   a board that has 
   a lower number of 
   attacking pairs"""
def get_neighbor(board):
    nQueens = len(board.get_map())
    adjacentboards = []

    for row in range(nQueens):
        for column in range(nQueens):             
            if is_full(board, row, column):
               adjacentSpaces = get_adjacent_spaces(board, row, column)
               for space in adjacentSpaces:
                    newBoard = copy.deepcopy(board)
                    if is_full(newBoard, space[0], space[1]):
                        continue

                    newBoard.flip(row, column)
                    newBoard.flip(space[0], space[1])
                    adjacentboards.append(newBoard)

                    for newBoard in adjacentboards:
                        if newBoard.get_fitness() + row_fitness(newBoard) < board.get_fitness() + row_fitness(board):
                            board = newBoard
                    adjacentboards = []
    return board

"""function to see if space inputted has a queen already"""
def is_full(board,i,j):
    board_map = board.get_map()
    if board_map[i][j] == 1:
        return True
    return False

"""function to determine row fitness"""
def row_fitness(board):
    attackingRows = 0
    map = board.get_map()
    for row in range(len(map)):
        if sum(map[row]) > 1:
            attackingRows += 1
    return attackingRows

"""Make sure that I implement random restart (somehow)"""
def hill_climbing(board):
    currentBoard = board

    while True:
        currentBoard = get_neighbor(currentBoard)
        currentBoardFitness = currentBoard.get_fitness() + row_fitness(currentBoard)
        if currentBoardFitness == 0:
            return currentBoard
        else:
            currentBoard = Board(len(currentBoard.get_map())) # random restart


if __name__ == '__main__':
    test = Board(5)
    start = time.time()
    newBoard = hill_climbing(test)
    end = time.time()

    print(f"Running time: {round(1000 * (end-start))} ms")
    map = newBoard.get_map()
    for row in range(len(newBoard.get_map())):
        for col in range(len(newBoard.get_map())):
            if map[row][col] == 0:
                print("-", end=" ")
            else:
                print(map[row][col], end=" ")
        print()