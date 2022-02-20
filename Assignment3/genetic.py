import random
from board import Board

"""pass in the dna encoded ordering of the queens 
   and get the the fitness of the board setup"""
def encoded_fitness(gene):
    geneBoard = gene_to_board(gene)
    return geneBoard.get_fitness()
    
"""pass in a gene's fitness along with a list of the other fitnesses and receive 
   a normalized value for gene fitness
   gene:string 
   genePool:[string]"""
def normalize_fitness(gene, genePool):
    geneFitness = encoded_fitness(gene)
    genePoolFitSum = 0.0
    for individualGene in genePool:
        genePoolFitSum += encoded_fitness(individualGene)
    return geneFitness/genePoolFitSum
    

"""function that uses normalized fitness value as chance of selection
   Note: needs to take in the genes, and the normalized values to determine selection"""
def selection(genes,normalizedGenes):
    r = random.uniform(0,1)

    if r < normalizedGenes[0]:
        return genes[0]
    elif r < normalizedGenes[1]:
        return genes[1]
    elif r < normalizedGenes[2]:
        return genes[2]
    else:
        return genes[4]

    

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

    genes = ["0123", "0321", "2310" ,"1320"]
    i = 0
    for gene in genes:
        print(f"Gene {i+1} Fitness: {encoded_fitness(gene)}")
        i += 1

    print(normalize_fitness("0123", genes))

    # test = Board(5)

    # test.show_map()
    # gene = board_to_gene(test)
    # print(f"\nString encoding: {gene}\n")

    # originalBoard = gene_to_board(gene)
    # print(f"Board from gene {gene}:\n")
    # originalBoard.show_map()






