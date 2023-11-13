#1
def init_matrix(vector):
    k = 0
    X = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    for i in range(9):
        for j in range(9):
            X[i][j] = vector[k]
            k += 1
    return X

def constraints(X, i, j, value):
    for k in range(9):
        if X[i][k] == value:
            return False
        if X[k][j] == value:
            return False

    for k in range(3):
        for l in range(3):
            if X[(i//3)*3 + k][(j//3)*3 + l] == value:
                return False

    if X[i][j] == -1:
        if value % 2 == 1:
            return False

    return True

def generate_domains(X):
    domains = {}
    for i in range(9):
        for j in range(9):
            if X[i][j] == 0:
                for k in range(9):
                    if constraints(X, i, j, k+1):
                        if (i, j) not in domains:
                            domains[(i, j)] = [k+1]
                        else:
                            domains[(i, j)].append(k+1)
            elif X[i][j] == -1:
                for k in [2, 4, 6, 8]:
                    if constraints(X, i, j, k):
                        if (i, j) not in domains:
                            domains[(i, j)] = [k]
                        else:
                            domains[(i, j)].append(k)
            else:
                domains[(i, j)] = [X[i][j]]
    return domains


#2 FORWARD CHECKING

def next_unassigned_variable(X):
    for i in range(9):
        for j in range(9):
            if X[i][j] == 0 or X[i][j] == -1:
                return (i, j)

def is_complete(X):
    for i in range(9):
        for j in range(9):
            if X[i][j] == 0 or X[i][j] == -1:
                return False
    return True

def BKT_with_FC(X, domains):
    if is_complete(X):
        return X

    i, j = next_unassigned_variable(X)
    if(i, j) in domains:
        for value in domains[(i, j)]:
            if constraints(X, i, j, value):
                new_X = [row[:] for row in X]
                new_X[i][j] = value
                new_domains = generate_domains(new_X)
                if not any([len(new_domains[key]) == 0 for key in new_domains]):
                    result = BKT_with_FC(new_X, new_domains)
                    if result is not None:
                        return result

    return None

init = init_matrix([8, 4, 0, 0, 5, 0, -1, 0, 0,
                    3, 0, 0, 6, 0, 8,  0, 4, 0,
                    0, 0, -1, 4, 0, 9, 0, 0, -1,
                    0, 2, 3, 0, -1, 0, 9, 8, 0,
                    1, 0, 0, -1, 0, -1, 0, 0, 4,
                    0, 9, 8, 0, -1, 0, 1, 6, 0,
                    -1, 0, 0, 5, 0, 3, -1, 0, 0,
                    0, 3, 0, 1, 0, 6, 0, 0, 7,
                    0, 0, -1, 0, 2, 0, 0, 1, 3])
domains_i = generate_domains(init)
rez = BKT_with_FC(init, domains_i)
print("FORWARD CHECKING------------------------------------------------------------")
for i in range(9):
    print(rez[i])

#3 MRV

def next_unassigned_variable_MRV(X, domains):
    min = 10
    imin = 0
    jmin = 0
    for i in range(9):
        for j in range(9):
            if X[i][j] == 0 or X[i][j] == -1:
                if (i,j) in domains:
                    if len(domains[(i,j)]) < min:
                        min = len(domains[(i, j)])
                        imin = i
                        jmin = j
    return (imin, jmin)

def BKT_with_FC_MRV(X, domains):
    if is_complete(X):
        return X

    i, j = next_unassigned_variable_MRV(X, domains)
    if(i, j) in domains:
        for value in domains[(i, j)]:
            if constraints(X, i, j, value):
                new_X = [row[:] for row in X]
                new_X[i][j] = value
                new_domains = generate_domains(new_X)
                if not any([len(new_domains[key]) == 0 for key in new_domains]):
                    result = BKT_with_FC(new_X, new_domains)
                    if result is not None:
                        return result

    return None

init = init_matrix([8, 4, 0, 0, 5, 0, -1, 0, 0,
                    3, 0, 0, 6, 0, 8,  0, 4, 0,
                    0, 0, -1, 4, 0, 9, 0, 0, -1,
                    0, 2, 3, 0, -1, 0, 9, 8, 0,
                    1, 0, 0, -1, 0, -1, 0, 0, 4,
                    0, 9, 8, 0, -1, 0, 1, 6, 0,
                    -1, 0, 0, 5, 0, 3, -1, 0, 0,
                    0, 3, 0, 1, 0, 6, 0, 0, 7,
                    0, 0, -1, 0, 2, 0, 0, 1, 3])
domains_i = generate_domains(init)
rez = BKT_with_FC_MRV(init, domains_i)
print("MRV--------------------------------------------------------------------")
for i in range(9):
    print(rez[i])