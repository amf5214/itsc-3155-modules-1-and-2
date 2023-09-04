def separate_letters_by_case():

    string = input("Please enter a string: ")
    characters = [*string]
    lowercase = []
    uppercase = []
    
    for x in characters:
        if x == " ":
            continue
        elif x.isupper():
            uppercase.append(x)
        elif x.islower():
            lowercase.append(x)

    for x in uppercase:
        lowercase.append(x)

    print("".join(lowercase))


if __name__ == "__main__":
    separate_letters_by_case()