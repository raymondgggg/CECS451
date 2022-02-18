from board import Board
import copy


"""function that returns a list of tuples of the adjacent 
   spaces for a given space of the board [(x1,y1), ... , (Xn, Yn)]"""
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
        if newBoard.get_fitness() < board.get_fitness():
            board = newBoard

    return board


"""function to see if space inputted has a queen already"""
def is_full(board,i,j):
    board_map = board.get_map()
    if board_map[i][j] == 1:
        return True
    return False




"""Make sure that I implement random restart (somehow)"""
def hill_climbing(board):
    current_matrix = board.get_map()
    while True:
        """I will come back to this"""
        
        


    return "raymond"





if __name__ == '__main__':
    test = Board(5)

    aSpaces = get_adjacent_spaces(test, 0,2)
    print(aSpaces)
    

    # print(test.get_fitness())
    # test.show_map()
    # print(is_full(test,0,0))
