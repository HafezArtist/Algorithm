A = "1011001"
m = len(A)
number = 0
k = 0
decimal_number = int(A, 2)
print(decimal_number)


while decimal_number > 0:

    two_bits = decimal_number % 4
    decimal_number //= 4

    number += two_bits * (4 ** k)
    k += 1
    print(f"number is {number}")

reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

print(reversed_number)