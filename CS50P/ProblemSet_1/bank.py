def main():
    greeting = input("Greeting: ").strip().lower()
    if greeting.startswith("hello"):        #The startswith() method is a string method in Python that returns True 
        print("$0")                         # if the string starts with the specified prefix,
                                            # otherwise it returns False.
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
