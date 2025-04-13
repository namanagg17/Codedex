def main():
    plate = input("Plate: ")  # Step 1: Ask the user for a plate.
    if is_valid(plate):  # Call is_valid to check if the plate is valid.
        print("Valid")  # If valid, print "Valid".
    else:
        print("Invalid")  # Otherwise, print "Invalid".


def is_valid(plate):
    # Step 2: Check if the length of the plate is between 2 and 6 characters.
    if not (2 <= len(plate) <= 6):
        return False  # If not, return False.
    
    # Step 3: Ensure the first two characters are letters.
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False  # If not, return False.

    # Step 4: Check if numbers come only at the end and not start with '0'.
    number_started = False  # Keep track if we've seen a number.
    for i, char in enumerate(plate):
        if char.isdigit():
            if char == '0' and not number_started:
                return False  # Step 4a: Numbers cannot start with '0'.
            number_started = True  # Mark that numbers have started.
        elif number_started:
            return False  # Step 4b: Letters can't follow numbers.

    # Step 5: Ensure the plate contains only alphanumeric characters (no punctuation or spaces).
    if not plate.isalnum():
        return False  # If there are non-alphanumeric characters, return False.
    
    return True  # If all checks pass, return True.


main()  # Call the main function to run the program.
