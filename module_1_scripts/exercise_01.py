def get_grade_value(value):
    return ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"][value//10]

def get_grade_classification(grade=None):
    if grade==None:
        grade = input("Enter a grade from 0 to 100: ")
    try:
        grade = int(grade)
        grade = get_grade_value(grade)
        print("Your grade is ", grade) 
        return grade

    except (ValueError, IndexError):
        get_grade_classification()


if __name__ == "__main__":
    get_grade_classification()