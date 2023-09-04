def split_string():
    string = input("Enter a string: ")
    characters = [*string]
    rtn_lst = []
    cur_lst = []
    for x in characters:
        if len(cur_lst) == 3:
            rtn_lst.append(cur_lst)
            cur_lst = []
        cur_lst.append(x)
    
    if len(cur_lst) > 0:
        rtn_lst.append(cur_lst)

    print(rtn_lst)
    return rtn_lst

if __name__ == "__main__":
    split_string()