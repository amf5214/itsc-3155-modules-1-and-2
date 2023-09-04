# INFO
# Austin Fraley
# 09/03/2023
# Intermediate Python Exercises 1 

def add_dictionaries(dict1, dict2):

    """
    Function to take in two dictionaries and outputs a new dictionary with the value elements added for the shared key values
    @arg dict1 dictionary object
    @arg dict2 dictionary object
    @return rtn_dict dictionary object
    """

    rtn_dict = {}

    if dict1 != None and dict2 != None:
        for key, value in dict2.items():
            if key in dict1:
                rtn_dict[key] = dict1[key] + value
        
        return rtn_dict
    
    else:
        return None


if __name__ == "__main__":
    dict1 = {"a":5, "b":9, "c":90, "d":34}
    dict2 = {"b":89, "c":34, "e": 8}
    print(add_dictionaries(dict1, dict2))