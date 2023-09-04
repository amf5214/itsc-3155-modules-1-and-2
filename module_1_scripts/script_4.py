# INFO
# Austin Fraley
# 09/03/2023
# Intermediate Python Exercises 1 

def get_and_add_ints():

    """
    Function to take in and add 5 ints
    """

    ints = []

    while len(ints) < 5:
        value = input("Please input an integers: ")
        
        try:
            value = int(value)
            ints.append(value)

        except ValueError:
            print("Error: Please enter a valid integer")
            continue

    print( "Sum of integers entered: ",sum(ints))
    

if __name__ == "__main__":
    get_and_add_ints()
