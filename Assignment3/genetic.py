from board import Board

"""pass in the dna encoded ordering of the queens 
   and get the the fitness of the board setup step 3"""
def encoded_fitness(gene):
    """Raymond"""

"""pass in a gene's fitness along with a list of the other fitnesses and receive 
   a normalized value for gene fitness step 4"""
def normalize_fitness(gene, geneFitnesses):
    """Raymond2"""

"""function that uses normalized fitness value as chance of selection
   Note: needs to take in the number of genes, and the normalized values to determine selection step 5"""
def selection():
    """RayRay"""

""" step 6"""
def pairs():
    """Raymond"""

"""step 7"""
def cross_over():
    """Raymond """
    
"""step 8"""
def mutation():
    """raymond"""

"""function to make nxn board with no queens"""
def n_zeros(board):
    map = board.get_map()
    for row in range(len(map)):
        for col in range(len(map)):
            if map[row][col] == 1:
                board.flip(row,col)

"""pass in the dna encoded ordering of queens 
   and get the board object returned"""
def gene_to_board(gene):
    board = Board(len(gene))
    n_zeros(board)
    map = board.get_map()
    row = 0
    for col in gene:
        map[row][int(col)] = 1
        row += 1
    return board
    
"""function that takes a board object and converts it to a string representation 
   for further genetic programming"""
def board_to_gene(board):
    stringList = []
    map = board.get_map()
    for row in range(len(map)):
        for col in range(len(map)):
            if map[row][col] == 1:
                stringList.append(str(col))
    return "".join(stringList) # represents the gene

if __name__ == "__main__":
    test = Board(5)

    test.show_map()
    print(board_to_gene(test))



