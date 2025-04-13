def main():
    x=input()
    print(convert(x))

def convert(y):
    return y.replace(":)","😊").replace(":(","☹️")

if __name__ == "__main__":
    main()


# short method 
#i= input()
#print(i.replace(":)", "🙂").replace(":(", "🙁"))