# INFO
# Austin Fraley
# 09/03/2023
# Intermediate Python Exercises 1 

def get_unique_list(obj=None):

    """
    Function to take in a list and output a new list with the unique elements from the input list
    @arg obj list object
    @return rtn_list list object
    """

    rtn_list = []

    for x in obj:
        if x not in rtn_list:
            rtn_list.append(x)

    return rtn_list

if __name__ == "__main__":
    test_list = [1,1,1,1,1,1,2,2,5,3,3,2,7,8,6,5,4,32,4,5,56,7,8,9,7,6,5,9]
    print(get_unique_list(test_list))