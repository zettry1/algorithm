def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    rows = set()
    cols = set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] ==0:
                rows.add(x)
                cols.add(y)

    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return matrix


def zero_matrix_pythonic(matrix):
    matrix = [["X" if x==0 else x for x in row] for row in matrix]
    indices =[]

    for idx, row in enumerate(matrix):
        if "X" in row:
            indices = indices +[i for i,j in enumerate(row) if j=="X"]
            matrix[idx] = [0]* len(matrix[0])
    matrix = [[0 if row.index(i) in indices else i for  i in row] for row in matrix]

    return matrix
