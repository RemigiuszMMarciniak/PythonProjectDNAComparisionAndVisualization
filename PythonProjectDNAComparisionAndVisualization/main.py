def main():
    print("Hello in DNA comparision and visualization program. \nSelect how do you want to reach the data: \n"
          "1. Insert the data manually. \n2. Read the data from a file. \n3. Read the data from the server")
    label = input("select:\n")
    while label != "1" or label != "2" or label != "3":
        if label == "1":
            print("Selected 1st option")
            manual_insert()
            break
        elif label == "2":
            print("Selected 2nd option")
            # method
            break
        elif label == "3":
            print("Selected 3rd option")
            # method
            break
        else:
            print("Please select correct method ")
            label = input("select:\n")


def manual_insert():
    user_input = input("Insert tag:")
    user_data = ">" + user_input + "\n"
    user_input = input("Enter DNA sequence")
    user_data += user_input

    print(user_data)


if __name__ == "__main__":
    main()
