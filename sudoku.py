import random
import time
import math
import sys
from copy import deepcopy
 

def objective_score(board):
    # Return the score of conflicts in the board
    score = 0
    for i in range(9)  : 
        row = board[i]
        score += conflicts(row) #Check for row
        
    for i in range(9) : 
        col = [rows[i] for rows in board] 
        score += conflicts(col) #Check for col
    return score

def get_block(board,i,ignore=False,initials=None) :
    # Return the ith block of the board as a list
    row = (i // 3) * 3
    col = (i % 3 )* 3
    arr = []
    for j in range(3) :
        for k in range(3) :
            if ignore : 
                if (row+j,col+k) not in initials : 
                    arr.append((row+j,col+k))
            else : 
                arr.append(board[row+j][col+k])
    return arr

def conflicts(board)  : 
    # Return the score in a single array
    list =  []
    score = 0 
    for i in range(9) : 
        if board[i] in list :
            score += 1
        else : 
            list.append(board[i])
    return score

def random_zeros(board) : 
    # Give a random value to the zeroes value by block
    for i in range(9) : 
        row = (i // 3) * 3
        col = (i % 3) * 3
        block = get_block(board,i)
        l = []
        for j in range(3) :
            for k in range(3) : 
                if board[row+j][col+k] == 0 : 
                    value = random.randint(1,9)
                    while value in block or value in l : 
                        value = random.randint(1,9)
                    board[row+j][col+k] = value
                    l.append(value)
                     
    return board

def get_initials(board) : 
    # Return array containing all the indexes
    # of the none 0 values
    l = []
    for i in range(9) :
        for j in range(9) :
            if board[i][j] != 0:
                l.append(board[i][j])
    return l
def swap_block(board,initials) : 
    # Swap two squares from a random block
    neighbour = deepcopy(board)
    block_idx = random.randint(0,8)
    block = get_block(neighbour,block_idx,ignore=True,initials=initials)  # Now get_block return a list of tuple 
    to_swap = random.sample(block,2)
    # print("\nBlock to swap : {}",block_idx)
    square1 = to_swap[0]
    square2 = to_swap[1]
    # print("Square 1 : ",square1,"\n")
    # print("Square 2 : ",square2,"\n")
    neighbour[square1[0]][square1[1]],neighbour[square2[0]][square2[1]] = board[square2[0]][square2[1]],board[square1[0]][square1[1]]
    return neighbour

def simulated_annealing_solver(initial_board):

    """Simulated annealing Sudoku solver."""
    board = deepcopy(initial_board)
    initials = get_initials(initial_board)
    current_solution = random_zeros(board)
    best_solution = current_solution
    
    current_score = objective_score(current_solution)
    best_score = current_score

    temperature = 1.0
    cooling_rate = 0.99993 #TODO: Adjust this parameter to control the cooling rate
    count = 0
    while temperature > 0.0001 : 

         
        try : 
            # TODO: Generate a neighbor (Don't forget to skip non-zeros tiles in the initial board ! It will be verified on Inginious.)
            ...
            neighbor = swap_block(current_solution,initials)
            
            
            # Evaluate the neighbor
            neighbor_score = objective_score(neighbor)

            # Calculate acceptance probability
            delta = float(current_score - neighbor_score)

            if current_score == 0:

                return current_solution, current_score

            # Accept the neighbor with a probability based on the acceptance probability
            if neighbor_score < current_score or (neighbor_score > 0 and math.exp((delta/temperature)) > random.random()):

                current_solution = neighbor
                current_score = neighbor_score

                if (current_score < best_score):
                    best_solution = current_solution
                    best_score = current_score
            # if(count % 10000 == 0) : 
            #     print_board(current_solution)
            #     print("\n Best Score : {} Current Score : {} Temp : {}".format(best_score,current_score,temperature))
            count+=1
            # Cool down the temperature
            temperature *= cooling_rate
        except : 
            print("Break Asked")
            break
            
        
    return best_solution, best_score

 
def print_board(board):

    """Print the Sudoku board."""

    for row in board:
        print("".join(map(str, row)))

 

def read_sudoku_from_file(file_path):
    """Read Sudoku puzzle from a text file."""
    
    with open(file_path, 'r') as file:
        sudoku = [[int(num) for num in line.strip()] for line in file]

    return sudoku
 

if __name__ == "__main__":

    # Reading Sudoku from file
    initial_board = read_sudoku_from_file(sys.argv[1])

    # Solving Sudoku using simulated annealing
    start_timer = time.perf_counter()

    solved_board, current_score = simulated_annealing_solver(initial_board)

    end_timer = time.perf_counter()

    print_board(solved_board)
    print("\nValue(C):", current_score)

    # print("\nTime taken:", end_timer - start_timer, "seconds")