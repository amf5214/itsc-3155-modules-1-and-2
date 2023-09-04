def get_num_average(num=None):
    if num==None:
        num = input("Please enter a number greater than 1:")

    try:
        num = int(num)
        values = []
        for n in range(0, num):
            value = input("Please enter a number:")
            values.append(int(value))
        
        print(f"List: {values}")
        print(f"Average: {sum(values)/len(values)}")

    except ValueError:
        get_num_average()


if __name__ == "__main__":
    get_num_average()
