while True:
    try: 
        x = input("Fraction: ")
        num,den = x.split('/')
        num = int(num)
        den = int(den)

        if den == 0:
            raise ZeroDivisionError  # NEW NEW NEW NEW 
        if num > den:
            raise ValueError
        
        y = (num / den)*100
        y = round(y)

        if y <= 1:
            print("E")
        elif y >= 99:
            print("F")
        else:        
            print(f"{y}%")
        break    

    except (ValueError,ZeroDivisionError):
        continue





