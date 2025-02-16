#=== Instructions ==========

matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', '', '#'],
    ['s', 'M', ''],
    ['$', 'a', ''],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

                                  
matrix_grid = [''.join(row) for row in matrix]
print(matrix_grid)

new_matrix = []
for column in range(len(matrix[0])): 
    for row in matrix_grid:  
        if column < len(row): 
            char = row[column]
            # print(char)
            if char.isalpha():  # check alphabet char or not
                new_matrix.append(char)
                # print(new_matrix)
            elif new_matrix and new_matrix[-1] != " ":
                new_matrix.append(" ") #change symbol to space
                # print(new_matrix)

# delete space
coding_message = ''.join(new_matrix).strip()
print(coding_message)
