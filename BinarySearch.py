#Let's see how does binary search works:

maximum = 1000
minimum = 1

questions = 0

print("Consider a number between 1 to 1000...")

while maximum >= minimum:

    middle = (maximum + minimum) // 2

    choice = int(input(f"Is the number greater than {middle} or smaller than {middle} or equal to {middle}? Enter 1 if greater than, 2 if smaller than, and 3 if equal to."))
    questions = questions + 1

    if choice == 1:
        minimum = middle + 1

    elif choice == 2:
        maximum = middle - 1

    else:
        print(f"I found the number! The number is {middle}. I found the number with {questions} questions.")
        break