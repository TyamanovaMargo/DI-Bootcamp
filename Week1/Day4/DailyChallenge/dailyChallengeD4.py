#=== Instructions ==========
<<<<<<< HEAD

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
=======
# create 2D list
# matrix = [
#     ['7', 'i', 'i'],
#     ['T', 's', 'x'],
#     ['h', '%', '?'],
#     ['i', '', '#'],
#     ['s', 'M', ''],
#     ['$', 'a', ''],
#     ['#', 't', '%'],
#     ['^', 'r', '!']
# ]
# matrix_griid = '''
# 7ii
# Tsx
# h%?
# i #
# sM 
# $a 
# #t%
# ^r!
# '''
                                  
matrix_grid = [''.join(row) for row in matrix]
print(matrix_grid)
# print(len(matrix[0])



new_matrix = []
for column in range(len(matrix[0])): #len(matrix[0]) gives the number of columns
>>>>>>> f4e6ea9 (last save 8.01)
    for row in matrix_grid:  
        if column < len(row): 
            char = row[column]
            # print(char)
<<<<<<< HEAD
            if char.isalpha():  # check alphabet char or not
=======
            if char.isalpha():  # check alphabet char or not isdigit for numbers
>>>>>>> f4e6ea9 (last save 8.01)
                new_matrix.append(char)
                # print(new_matrix)
            elif new_matrix and new_matrix[-1] != " ":
                new_matrix.append(" ") #change symbol to space
                # print(new_matrix)

# delete space
coding_message = ''.join(new_matrix).strip()
print(coding_message)
