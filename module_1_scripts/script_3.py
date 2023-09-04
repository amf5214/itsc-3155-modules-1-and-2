# INFO
# Austin Fraley
# 09/03/2023
# Intermediate Python Exercises 1 

def count_letters(string):

    """
    Function to count the instances of each unique character
    @arg string str object 
    @return rtn_dict dictionary object
    """

    letters = [*string]
    rtn_dict = {}

    for x in letters:
        if x in rtn_dict:
            rtn_dict[x] += 1
        else:
            rtn_dict[x] = 1

    return rtn_dict


if __name__ == "__main__":
    print(count_letters("hello world"))