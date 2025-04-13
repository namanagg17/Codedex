camel_case = input("camelCase: ")
snake_case = ""
for alpha in camel_case:
    if alpha.isupper():
        snake_case += "_" + alpha.lower() 
    else:
        snake_case += alpha
print("snake_case:",snake_case)          