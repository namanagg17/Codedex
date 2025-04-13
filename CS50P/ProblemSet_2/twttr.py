x = input("Input: ")
vowels = ["A","a","I","i","e","E","o","O","u","U"] # here we can use both "aeiouAEIOU" to check because
result = ""                                             # we are checking for a str only 
for y in x:
    if y not in vowels:
        result += y
print("Output:",result)    # automatically , leaves a space after :  