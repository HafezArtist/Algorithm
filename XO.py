#Let's play tic tac toe!

table = [[0] * 3 for i in range (3)]

def init_table(table):
    tableNum = 1
    for i in range(3):
        for j in range(3):
            table[i][j] = tableNum
            tableNum = tableNum + 1


def tableize(table):
    for i in range (3):
        for j in range (3):
            print(table[i][j], end=" " )
        print()


def put(number, symbol):
    row = number // 3
    col = number % 3
    if table[row][col] == "X" or table[row][col] == "O":
        print("You can't put anything here!")
        exit(0)
    table[row][col] = symbol


# def checker(symbol):

#     #checking the rows:
#     if table[0][0] == symbol and table[0][1] == symbol and table[0][2] == symbol:
#         return True
#     if table[1][0] == symbol and table[1][1] == symbol and table[1][2] == symbol:
#         return True
#     if table[2][0] == symbol and table[2][1] == symbol and table[2][2] == symbol:
#         return True
    

#     #checking the cols:
#     if table[0][0] == symbol and table[1][0] == symbol and table[2][0] == symbol:
#         return True
#     if table[0][1] == symbol and table[1][1] == symbol and table[2][1] == symbol:
#         return True
#     if table[0][2] == symbol and table[1][2] == symbol and table[2][2] == symbol:
#         return True
    

#     #checking the diagonals:
#     if table[0][0] == symbol and table[1][1] == symbol and table[2][2] == symbol:
#         return True
#     if table[0][2] == symbol and table[1][1] == symbol and table[2][0] == symbol:
#         return True
    
#     return False


# Writing the above function using "for loop":

def checker(symbol):
    for i in range (3):
        if table[i][0] == symbol and table[i][1] == symbol and table[i][2] == symbol:
            return True
        if table[0][i] == symbol and table[1][i] == symbol and table[2][i] == symbol:
            return True
        
    if table[0][0] == symbol and table[1][1] == symbol and table[2][2] == symbol:
        return True
    if table[0][2] == symbol and table[1][1] == symbol and table[2][0] == symbol:
        return True
    
    return False


init_table(table)
tableize(table)

for move in range(9):
    if move % 2 == 0:
        X = int(input("Enter number of the table, Player 1!:"))
        put(X-1, "X")
        if checker("X"):  #checks if checker X is true or false
            print("Player 1 is the winner!")
            break

    else:
        X = int(input("Enter number of the table, Player 2! : "))
        put(X-1, "O")
        if checker("O"):  #checks if checker O is true or false
            print("Player 2 is the winner!")
            break


    tableize(table)