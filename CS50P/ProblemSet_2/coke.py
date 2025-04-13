cost = 50
valid_coins = [25,10,5]
while cost > 0:
    coin = int(input(f"Amount Due: {cost} \nInsert Coin: " ))    # \n can be used to get insert coins in next line 
    if coin in valid_coins:
        cost -= coin   # more pythonic way 
if cost < 0:
    print(f"Change owned: {-cost}")
else:
    print("Change owned: 0")    