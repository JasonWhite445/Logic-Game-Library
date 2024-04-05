import random

# Size will be changed later to be user input
size = 5
nums = [i+1 for i in range(size**2)]
random.shuffle(nums)
# Grid is a random array of the numbers from 1 to size^2
grid = [nums[size*i:size*(i+1)] for i in range(size)]
operators = ['+', '-', '*', '/']
# operators_easy = ['+', '-', '*']
# # n rows of n-1 operators
# row_operators = [[random.choice(operators) for _ in range(size-1)]for _ in range(size)]
# # n-1 rows of n operators
# col_operators = [[random.choice(operators) for _ in range(size)]for _ in range(size-1)]
# print(grid)
# print(row_operators)
# print(col_operators)
#
# # These two loops can make the equations and evaluate them
# # Need to modify so that we only get integer outputs
# bad = []  # Used for testing
# for r in range(size):
#     temp = ''
#     for n in range(size-1):
#         temp += f"{grid[r][n]}{row_operators[r][n]}"
#     temp += f"{grid[r][-1]}"
#     if eval(temp) != int(eval(temp)):
#         bad.append(f"Row {r+1}")
#     print(f"{temp} = {eval(temp)}")
# for c in range(size):
#     temp = ''
#     for n in range(size-1):
#         temp += f"{grid[n][c]}{col_operators[n][c]}"
#     temp += f"{grid[-1][c]}"
#     if eval(temp) != int(eval(temp)):
#         bad.append(f"Column {c+1}")
#     print(f"{temp} = {eval(temp)}")
# print(bad)

row_operators = []
for r in range(size):
    row_signs = []
    temp = f'{grid[r][0]}'
    n = 0
    while n < size-1:
        temp_op = random.choice(operators)
        new = f'{temp_op}{grid[r][n+1]}'
        if eval(temp+new) == int(eval(temp+new)):
            row_signs += temp_op
            temp += new
            n += 1
    row_operators.append(row_signs)
    print(f'{temp} = {int(eval(temp))}')
    print(row_signs)
col_operators = []
for r in range(size):
    col_signs = []
    temp = f'{grid[0][r]}'
    n = 0
    while n < size-1:
        temp_op = random.choice(operators)
        new = f'{temp_op}{grid[n+1][r]}'
        if eval(temp+new) == int(eval(temp+new)):
            col_signs += temp_op
            temp += new
            n += 1
    col_operators.append(col_signs)
    print(f'{temp} = {int(eval(temp))}')
    print(col_signs)