n = int(input("Enter the Number: "))
result = 1

for i in range(1 , n + 1):
    result *= i

print(n ,"! is: " ,result)