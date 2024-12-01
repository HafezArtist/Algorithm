# n = 8
# queens = [0] * 8
# col = False * 8
# diag1 = False * 15
# diag2 = False * 15


# def put (row, col):
#     if col[col] or diag1(row + col) or diag2(row - col +7):
#         return False

#     col[col] = diag1(row + col) = diag2(row - col + 7) = True
#     queens[row] = col
#     return True


# def pick(row, col):

#     col[col] = diag1(row + col) = diag2(row - col + 7) = False


# def find(row):
#     if row == n:
#         # print_solution()
#         print(queens)
#         return
#     for i in range(n):
#         if put(row, i):
#             find(row + 1)
#             pick(row, i)


# find(0)



n = 8
queens = [0] * n
col = [False] * n
diag1 = [False] * (2 * n - 1)  # برای قطرها
diag2 = [False] * (2 * n - 1)  # برای قطرها


def put(row, col_index):
    if col[col_index] or diag1[row + col_index] or diag2[row - col_index + (n - 1)]:
        return False

    col[col_index] = True
    diag1[row + col_index] = True
    diag2[row - col_index + (n - 1)] = True
    queens[row] = col_index
    return True


def pick(row, col_index):
    col[col_index] = False
    diag1[row + col_index] = False
    diag2[row - col_index + (n - 1)] = False


def find(row):
    if row == n:
        print(queens)
        return
    for i in range(n):
        if put(row, i):
            find(row + 1)
            pick(row, i)


find(0)