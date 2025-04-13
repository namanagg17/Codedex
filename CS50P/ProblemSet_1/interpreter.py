user_input = input("Expressions: ")

x,y,z = user_input.split(" ")

x=float(x)
z=float(z)

if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)  
elif y == "/":
    print(x/z)      