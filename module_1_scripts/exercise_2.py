def print_string_backwards():
    string = input("Please enter a string: ")
    characters = [*string]
    print("".join(characters[::-1]))

if __name__ == "__main__":
    print_string_backwards()