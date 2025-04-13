def main():
    grocery_list = {}
    try:
        while True:
            item = input().lower()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1 
    except EOFError:
        pass
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}") 
main()                    

