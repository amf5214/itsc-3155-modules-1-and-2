def test_suffix(string1=None, string2=None):
    if string1==None:
        string1 = input("Please enter a valid string: ")
    if string2==None:
        string2 = input("Please enter a valid string: ")


    if (string1.lower() in string2.lower()) | (string2.lower() in string1.lower()):
        print("True")
        return True

    else:
        print("False")
        return False
        

if __name__ == "__main__":
    test_suffix()