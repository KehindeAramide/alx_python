def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = [item ** 2 for item in row]
        new_matrix.append(new_row)
    return new_matrix