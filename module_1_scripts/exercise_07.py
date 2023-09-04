def get_ints():
    quit = False
    iter_num = 0
   
    values = []

    while not quit:
        value = input("Please enter a number or enter QUIT to quit: ")
        
        try:
            if type(int(value)) == int:
                values.append(int(value))

        except ValueError:
            if type(value) == str and value == "QUIT":
                quit = True
                break
        
    evens = [x for x in values if x % 2 == 0]

    print("Values: ", values)
    print("Evens: ", evens)


if __name__ == "__main__":
    get_ints()