import random
import time
import math
import sys

 

def objective_score(board):
    score = 0
    for i in range(9)  : 
        row = board[i]
        col = [row[i] for row in board] 
        block = get_block(board,i)
        score += conflicts(row)
        score += conflicts(col)
        score += conflicts(block)
    return score
    
def find_empty(board) : 
    for i in range(len(board)) :
        for j in range(len(board[0])) :
            if board[i][j] == 0 : 
                return (i,j)
    return None

def get_block(board,i) :
    row = (i // 3) * 3
    col = (i % 3 )* 3
    arr = []
    for j in range(3) :
        for k in range(3) :
            arr.append(board[row+j][col+k])
    return arr
def conflicts(board)  : 
    list =  []
    score = 0 
    for i in range(9) : 
        if board[i] in list :
            score += 1
        else : 
            list.append(board[i])
    return score

def simulated_annealing_solver(initial_board):

    """Simulated annealing Sudoku solver."""

    current_solution = [row[:] for row in initial_board]
    best_solution = current_solution
    
    current_score = objective_score(current_solution)
    best_score = current_score

    temperature = 1.0
    cooling_rate = ...  #TODO: Adjust this parameter to control the cooling rate

    while temperature > 0.0001:

        try:  

            # TODO: Generate a neighbor (Don't forget to skip non-zeros tiles in the initial board ! It will be verified on Inginious.)
            ...
            neighbor = ...
           

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

            # Cool down the temperature
            temperature *= cooling_rate
        except:

            print("Break asked")
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

    print(objective_score(initial_board))

    # print("\nTime taken:", end_timer - start_timer, "seconds")