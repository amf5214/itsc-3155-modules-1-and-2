def print_cubes_upto_int(num=None):
    if num==None:
        num = input("Please enter a number greater than 1:")

    try:
        num = int(num)
        for n in range(1, num+1):
            print(f"The cube of {n} is {n**3}")

    except ValueError:
        print_cubes_upto_int

if __name__ == "__main__":
    print_cubes_upto_int()