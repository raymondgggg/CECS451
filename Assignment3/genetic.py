# Raymond Guevara Lozano
# 018504731
import random
import time
from board import Board

def genetic_algorhythm(numGenes):
    boards = generate_boards(numGenes, 5)
    population = [0] * numGenes

    for i in range(len(boards)): # get gene representation of boards
        population[i] = board_to_gene(boards[i])

    winingGene = ''
    geneFitness = -1
    while geneFitness != 0:
        nFitness = normalize_fitness(population)

        selectedGenes = []
        for gene in population:
            selectedGenes.append(selection(population, nFitness))

        genePairs = pairs(selectedGenes)
        crossedGenes = cross_over(genePairs)
        mutatedGenes = mutation(crossedGenes)

        population = mutatedGenes

        for gene in population:
            if encoded_fitness(gene) == 0:
                geneFitness = 0
                winingGene = gene

    return winingGene

"""function that generates n boards mxm"""
def generate_boards(n, m):
    boards = [0] * n
    for i in range(n):
        boards[i] = Board(m)
    return boards

"""pass in the dna encoded ordering of the queens 
   and get the the fitness of the board setup"""
def encoded_fitness(gene):
    geneBoard = gene_to_board(gene)
    return geneBoard.get_fitness()
    
"""pass in list of gene pool and get back a list of normalized gene fitnesses"""
def normalize_fitness(genePool): #optimized 
    geneFitnesses = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(geneFitnesses)):
        geneFitnesses[i] = encoded_fitness(genePool[i])
        
    fitnessSum = sum(geneFitnesses)

    nGeneFitnesses = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    for gFitness in geneFitnesses:
        nGeneFitnesses[i] = gFitness / fitnessSum
        i += 1

    return nGeneFitnesses
    
"""function that uses normalized fitness value as chance of selection
   Note: needs to take in the genes, and the normalized values to determine selection
   and both the genes list and normalizedGenes list need to correspond"""
def selection(genes,normalizedGenes):
    r = random.uniform(0,1)

    selectValues = [0] * 8
    selectSum = 0
    for i in range(len(normalizedGenes)):
        selectSum += normalizedGenes[i]
        selectValues[i] = selectSum
    
    if r < selectValues[0]:
        return genes[0]
    elif r < selectValues[1]:
        return genes[1]
    elif r < selectValues[2]:
        return genes[2]
    elif r < selectValues[3]:
        return genes[3]
    elif r < selectValues[4]:
        return genes[4]
    elif r < selectValues[5]:
        return genes[5]
    elif r < selectValues[6]:
        return genes[6]
    else:
        return genes[7]

"""function that takes in a list of genes and returns a list of tuples of pairs"""
def pairs(genes):
    genesPairs = []
    for i in range(len(genes)-1):
        genesPairs.append((genes[i], genes[i+1]))
    return genesPairs

"""function that takes in the gene pairs, chooses random crossover index, 
   and combines the two genes, genePairs: [(gene1, gene2), (gene3, gene4)]
   returns a list of new genes"""
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
   randomly mutatate a part of each gene 
   genes: [gene1, gene2, ... , geneN] 
   genes encoded as strings"""
def mutation(genes): #optimized
    mutatedGenes = [0] * len(genes)
    for i in range(len(genes)):
        randomIndex = random.randint(0, len(genes[i])-1)
        randomMutation = random.randint(0, len(genes[i])-1)

        geneToList = list(genes[i])
        geneToList[randomIndex] = str(randomMutation)

        mutatedGenes[i] = "".join(geneToList)
    return mutatedGenes

"""function to make nxn board with no queens"""
def n_zeros(board): #optimized 
    map = board.get_map()
    for row in range(len(map)):
        map[row] = [i * 0 for i in map[row]]

"""pass in the dna encoded ordering of queens 
   and get the board object returned"""
def gene_to_board(gene): #optimized
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
def board_to_gene(board): # doesn't need optimization
    stringList = []
    map = board.get_map()
    for row in range(len(map)):
        for col in range(len(map)):
            if map[row][col] == 1:
                stringList.append(str(col))
    return "".join(stringList) # represents the gene

if __name__ == "__main__":
    start = time.time()
    solutionGene = genetic_algorhythm(8)
    end = time.time()

    solutionBoard = gene_to_board(solutionGene)
    print(f"Running time: {round(1000 * (end-start))} ms")
    
    map = solutionBoard.get_map()
    for row in range(len(solutionBoard.get_map())):
        for col in range(len(solutionBoard.get_map())):
            if map[row][col] == 0:
                print("-", end=" ")
            else:
                print(map[row][col], end=" ")
        print()