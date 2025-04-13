fruit = input("Input: ").lower()
fda = {
    "apple" : "130",
    "avacado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "60",
    "grapes" : "90",
    "honeydew melon" :"50",
    "kivifruit" : "90",
    "lemon" : "15",
    "lime" : "20",
    "nectarine" : "60",
    "orange" : "80",
    "peach" : "60",
    "pear" : "100",
    "pineapple" : "50",
    "plums" : "70",
    "strawberries" : "50",
    "sweet cherry" : "100",
    "tangerine" : "50",
    "watermelon" : "80",
}
if fruit in fda:
    print(f"Calories: {fda[fruit]}")
else:
    pass
    