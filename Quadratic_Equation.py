print("Consider y= ax^2 + bx + c")

a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))

if a == 0:
    print("ERORR! Quadratic factor is 0.")

delta = (b**2) - (4*a*c)

# if delta < 0:

rooted_delta = delta**(1/2)
x1 = ((rooted_delta) + (-b)) / (2 * a)
x2 = ((rooted_delta) - (-b)) / (2 * a)

print(f"one root of x is: {x1} and the other is {x2}.")