def get_unique_ints():
    values = []

    while(len(values) < 10):
        value = input("Please enter a number: ")
        try:
            value = int(value)
            values.append(value)

        except ValueError:
            continue

    print("Original values: ", values)
    print("Nums that only appear once: ", get_unique_values(values))

def count_values(lst):
    dict = {}
    for x in lst:
        if str(x) in dict.keys():
            dict[str(x)] += 1
        
        else:
            dict[str(x)] = 1


    return dict

def get_unique_values(lst):
    dict = count_values(lst)
    rtn_value = []

    for x in lst:
        if dict[str(x)] == 1:
            rtn_value.append(x)

    return rtn_value


if __name__ == "__main__":
    get_unique_ints()