def main():
    time = input("What time it is? ")
    time2 = convert(time)
    if 7 <= time2 <= 8 :
        print("Breakfast time")
    elif 12 <= time2 <= 13:
        print("Lunch Time")
    elif 18 <= time2 <= 19:
        print("Dinner Time")


def convert(time):
    hours,minutes= time.split(":")
    hours=float(hours)
    minutes=int(minutes)
    return hours + (minutes/60)
    
if __name__ == "__main__":
    main()
