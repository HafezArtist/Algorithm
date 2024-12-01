#We are always the winner! in this game!

n = int(input("Enter How many marbles there are: "))

while n > 0:
    if n % 3 == 0:
        print("You play!")
        Youpick = int(input("How many marbles do you pick up?"))
        if Youpick == 2:
            print("I pick up 1 marble.")
            n = n - 1
        else:
            print("I pick up 2 marbles.")
            n = n - 2
    else:
        print("We play!")
        wePick = n % 3
        print(f"We pick {wePick} marbles.")
        n = n - wePick
print("We won the game!")


#the algorithm above looks right. But let's split the while loop and if logic.


# n = int(input("Enter How many marbles there are: "))

# if n % 3 == 0:
#     wePlay = False
#     print("You Play first.")
# else:
#     wePlay = True
#     print("We play first.")
#     wePick = n % 3
#     print(f"We pick up {wePick} marbles.")
#     n = n - wePick


# while n > 0:
#     print(f"There are {n} marbles on the table now.")
#     youPick = int(input("How many marbles do you pick up?"))
#     n = n - youPick
#     wePick = n % 3
#     print(f"We pick up {wePick} marbles.")
#     n = n - wePick

# print("We won the game!")


#Both my algorithm and dr.shrifi's algorithm work. Congratulations!