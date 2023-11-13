# 1. Reprezentare cu matrice, retinand ultima celula mutata sub forma de pereche [i, j]
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
last_moved_cell = []


# 2. Functie de initializare a starii
def init_state(vector):
    k = 0
    for i in range(3):
        for j in range(3):
            matrix[i][j] = vector[k]
            k += 1
    last_moved_cell = [-1, -1]
    return (matrix, last_moved_cell)


# 2. Functie care verifica daca starea este finala
def is_final_state(mat):
    value = 1
    for row in mat:
        for cell in row:
            if cell == value:
                value += 1

    return value == 9


# 3. Functie care verifica ca o mutare este valida
def is_valid(mat, cell, direction):
    global last_moved_cell

    if cell == last_moved_cell:
        return False

    if direction == 'up':
        if cell[0] == 0:
            return False
        elif mat[cell[0] - 1][cell[1]] == 0:
            return True
        else:
            return False

    elif direction == 'down':
        if cell[0] == 2:
            return False
        elif mat[cell[0] + 1][cell[1]] == 0:
            return True
        else:
            return False

    elif direction == 'left':
        if cell[1] == 0:
            return False
        elif mat[cell[0]][cell[1] - 1] == 0:
            return True
        else:
            return False

    elif direction == 'right':
        if cell[1] == 2:
            return False
        elif mat[cell[0]][cell[1] + 1] == 0:
            return True
        else:
            return False

    return True


# 3. Functie care realizeaza un swap intre 2 celule
def swap(mat, cell1, cell2):
    aux = mat[cell1[0]][cell1[1]]
    mat[cell1[0]][cell1[1]] = mat[cell2[0]][cell2[1]]
    mat[cell2[0]][cell2[1]] = aux
    return mat


# 3. Functie care realizeaza o tranzitie
def transition(mat, cell, direction):
    global last_moved_cell
    if is_valid(mat, cell, direction) == False:
        return mat, "Invalid move"

    if direction == 'up':
        mat = swap(mat, cell, [cell[0] - 1, cell[1]])
        last_moved_cell = [cell[0] - 1, cell[1]]
    elif direction == 'down':
        mat = swap(mat, cell, [cell[0] + 1, cell[1]])
        last_moved_cell = [cell[0] + 1, cell[1]]
    elif direction == 'left':
        mat = swap(mat, cell, [cell[0], cell[1] - 1])
        last_moved_cell = [cell[0], cell[1] - 1]
    elif direction == 'right':
        mat = swap(mat, cell, [cell[0], cell[1] + 1])
        last_moved_cell = [cell[0], cell[1] + 1]
    return mat, "Valid move"

#4
def iddfs(matrix, last_moved_cell, depth, visited_states):

    if is_final_state(matrix):
        print("Solutia iddfs: ", matrix)
        return []

    if depth == 0:
        return None

    directions = ['up', 'down', 'left', 'right']

    for i in range(3):
        for j in range(3):
            cell = [i, j]

            for direction in directions:
                new_matrix, result = transition(matrix, cell, direction)
                if result == "Valid move":
                    new_last_moved_cell = last_moved_cell
                    if cell != last_moved_cell:
                        new_last_moved_cell = cell

                    new_matrix_tuple = tuple(tuple(row) for row in new_matrix)

                    if new_matrix_tuple not in visited_states:
                        visited_states.add(new_matrix_tuple)

                        solution = iddfs(new_matrix, new_last_moved_cell, depth - 1, visited_states)
                        if solution is not None:

                            return [cell, direction] + solution

                        visited_states.remove(new_matrix_tuple)

    return None


def solve_puzzle_with_iddfs(matrix, last_moved_cell, max_depth):
    visited_states = set()
    for depth in range(max_depth + 1):
        solution = iddfs(matrix, last_moved_cell, depth, visited_states)
        if solution is not None:
            return solution




#5
def create_final_state(state):
    zero = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero = [i, j]
    f_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    cnt = 1
    for i in range(3):
        for j in range(3):
            if [i, j] != zero:
                f_state[i][j] = cnt
                cnt += 1
            else:
                f_state[i][j] = 0
    return f_state

def manhattan_distance(state):
    final_state = create_final_state(state)
    dist = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != final_state[i][j]:
                for k in range(3):
                    for l in range(3):
                        if state[i][j] == final_state[k][l]:
                            dist += abs(i - k) + abs(j - l)

    return dist

def hamming_distance(state):
    final_state = create_final_state(state)
    dist = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != final_state[i][j]:
                dist += 1

    return dist

from math import sqrt

def euclidian_distance(state):
    final_state = create_final_state(state)
    dist = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != final_state[i][j]:
                for k in range(3):
                    for l in range(3):
                        if state[i][j] == final_state[k][l]:
                            dist += (i - k) ** 2 + (j - l) ** 2

    return sqrt(dist)

from queue import PriorityQueue

def greedy(init_state, heuristic):
    pq = PriorityQueue()
    pq.put((init_state, heuristic(init_state)))
    visited = [init_state]
    mutari = -1

    while not pq.empty():
        state,_ = pq.get()
        mutari += 1
        if is_final_state(state):
            return state, mutari

        visited.append(state)

        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    current_cell = (i, j)

                    for direction in ['up', 'down', 'left', 'right']:
                        new_state, message = transition([list(row) for row in state], current_cell, direction)
                        if message == "Valid move":
                            if new_state not in visited:
                                pq.put((new_state, heuristic(new_state)))

    return None

import time
from colorama import Fore

#6
instances = [[8, 6, 7, 2, 5, 4, 0, 3, 1], [2, 5, 3, 1, 0, 6, 4, 7, 8], [2, 7, 5, 0, 8, 4, 3, 1, 6]]
for instance in instances:
    print(Fore.RED + "Pentru instanta: ", instance)
    initial_state, last_moved_cell = init_state(instance)
    print(Fore.RESET)

    start_time = time.time()
    sol = solve_puzzle_with_iddfs(initial_state, last_moved_cell, 15)
    print("Lungimea solutiei: ", int(len(sol)/2))
    print("Timp de executie: ", time.time() - start_time)
    print()

    initial_state, last_moved_cell = init_state( instance)
    start_time = time.time()
    sol, mutari = greedy(initial_state, manhattan_distance)
    print("Solutia greedy (manhattan): ", sol)
    print("Lungimea solutiei: ", mutari)
    print("Timp de executie: ", time.time() - start_time)
    print()

    initial_state, last_moved_cell = init_state(instance)
    start_time = time.time()
    sol, mutari = greedy(initial_state, hamming_distance)
    print("Solutia greedy (hamming): ", sol)
    print("Lungimea solutiei: ", mutari)
    print("Timp de executie: ", time.time() - start_time)
    print()

    initial_state, last_moved_cell = init_state(instance)
    start_time = time.time()
    sol, mutari = greedy(initial_state, euclidian_distance)
    print("Solutia greedy (euclidian): ", sol)
    print("Lungimea solutiei: ", mutari)
    print("Timp de executie: ", time.time() - start_time)
    print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------------" + Fore.RESET)


