string = input("Input: ")

dic = {
    ":1st_place_medal:" : "🥇",
    ":money_bag:" : "💰",
    ":smile_cat:" : "😸",
    }

for x,y in dic.items():
    string = string.replace(x,y)  

print(f"Output: {string}")

"""
Before :: pip install emoji in terminal
import emoji
def main():
    user_input = input("Input: ")
    emojized_text = emoji.emojize(user_input, use_aliases=True)
    print(f"Output: {emojized_text}")
main()
"""