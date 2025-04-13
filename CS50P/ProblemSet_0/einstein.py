def marks_to_grade_point(marks):
    """
    Convert marks (out of 100) to grade points (out of 10).
    """
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    else:
        return 0  # Fail


def calculate_cgpa(marks_and_credits):
    """
    Calculate CGPA based on marks and credits.

    :param marks_and_credits: List of tuples, each containing marks (out of 100) and credit.
    :return: CGPA (float)
    """
    total_points = 0
    total_credits = 0

    for marks, credit in marks_and_credits:
        grade_point = marks_to_grade_point(marks)
        total_points += grade_point * credit
        total_credits += credit

    if total_credits == 0:
        return 0  # Avoid division by zero

    return total_points / total_credits


# Take user input
def get_user_input():
    """
    Get user input for marks and credits for multiple subjects.
    """
    n = int(input("Enter the number of subjects: "))
    marks_and_credits = []

    for i in range(n):
        print(f"\nSubject {i + 1}:")
        marks = float(input("Enter marks (out of 100): "))
        credits = int(input("Enter credits for the subject: "))
        marks_and_credits.append((marks, credits))

    return marks_and_credits


# Main program
if __name__ == "_main_":
    print("### CGPA Calculator ###")
    marks_and_credits = get_user_input()
    cgpa = calculate_cgpa(marks_and_credits)
    print(f"\nYour CGPA is: {cgpa:.2f}")
