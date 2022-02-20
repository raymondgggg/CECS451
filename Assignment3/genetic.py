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
   Note: needs to take in the genes, and the normalized values to determine selection
   and both the genes list and normalizedGenes list need to correspond"""
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

"""function that takes in a list of genes and returns a list of tuples of pairs"""
def pairs(genes):
    genesPairs = []
    for i in range(len(genes)-1):
        genesPairs.append((genes[i], genes[i+1]))
    return genesPairs


"""function that takes in the gene pairs, chooses random crossover index, 
   and combines the two genes, genePairs: [(gene1, gene2), (gene3, gene4)]"""
def cross_over(genePairs):
    newGenes = []
    geneLength = len(genePairs[0][0])
    crossoverIndex = random.randint(0, geneLength-1)
    for pair in genePairs:
        gene1 = pair[0]
        gene2 = pair[1]

        gene1FirstHalf = gene1[0:crossoverIndex]
        gene1SecondHalf = gene1[crossoverIndex:]

        gene2FirstHalf = gene2[0:crossoverIndex]
        gene2SecondHalf = gene2[crossoverIndex:]

        newGene1 = gene1FirstHalf + gene2SecondHalf
        newGene2 = gene2FirstHalf + gene1SecondHalf

        newGenes.append(newGene1)
        newGenes.append(newGene2)
    
    return newGenes

    
"""function that will take the new crossed over genes and 
   randomly mutation a part of each gene 
   genes: [gene1, gene2, ... , geneN] 
   genes encoded as strings"""
def mutation(genes):
    mutatedGenes = []
    for gene in genes:
        randomIndex = random.randint(0, len(gene)-1)
        randomMutation = random.randint(0, len(gene)-1)

        geneToList = list(gene)
        geneToList[randomIndex] = str(randomMutation)

        mutatedGenes.append("".join(geneToList))
    return mutatedGenes


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

    genes = ["01234", "03421", "23104" ,"13204"]
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






