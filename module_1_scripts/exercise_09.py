def get_words():
    values = []

    while(len(values) < 10):
        value = input("Please enter a word: ")
        values.append(value)
        values.append(" ")

    print("".join(values))


if __name__ == "__main__":
    get_words()