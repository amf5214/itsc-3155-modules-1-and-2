def compare_num_lists():
    values1 = []
    values2 = []

    value = None

    print("List 1")
    for n in range(0, 5):
            value = input("Please enter a number:")
            values1.append(int(value))
    print("List 2")
    for n in range(0, 5):
            value = input("Please enter a number:")
            values2.append(int(value))

    print("List 1: ", values1)
    print("List 2: ", values2)
    print("Common list: ", [x for x in values1 if x in values2])


if __name__ == "__main__":
        compare_num_lists()