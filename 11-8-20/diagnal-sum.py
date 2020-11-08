def sum_diagonals(matrix):
    pos1 = 0
    total = 0
    
    if len(matrix) == 1:
        if len(matrix[0]) == 0:
            return 0
        return matrix[0][0] * 2
    
    for i in matrix:
        total += i[pos1]
        pos1 += 1
        
    pos1 = pos1 - 1

    for i in matrix:
        total += i[pos1]
        pos1 -= 1
    return total