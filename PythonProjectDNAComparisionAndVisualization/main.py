def main():
    print("Hello in DNA comparision and visualization program.")
    print("\nSelect 1st sequence \n")
    data_tuple = select_method()
    data_array_first = list(data_tuple[1])
    description_first = data_tuple[0]

    print(data_array_first)
    print("\nSelect 2nd sequence \n")
    data_tuple = select_method()
    data_array_second = list(data_tuple[1])
    description_second = data_tuple[0]

    # print(data_array_second)
    #
    # print(list(data_array_first))
    # dot plot method
    dot_plot = generate_dot_plot(data_array_first, data_array_second)
    print(dot_plot)

    # show dot plot
    show_dot_plot(data_array_first, description_first, data_array_second, description_second, dot_plot)


def show_dot_plot(data_array_first, name_first, data_array_second, name_second, dot_plot):
    print("first sequence:")
    print(name_first)
    print(data_array_first)
    print("second sequence")
    print(name_second)
    print(data_array_second)

    # print(data_array_second)

    for i in range(len(dot_plot)):
        for j in range(len(dot_plot[i])):
            print(dot_plot[i][j], end=' ')
        print()


def generate_dot_plot(array1, array2):
    dot_plot = [[0 for i in range(len(array2))] for j in range(len(array1))]
    # print(len(dot_plot))
    # print(dot_plot)
    # print(dot_plot[1][1])
    # dot_plot[1][1] = 1
    # print(dot_plot[1][1])
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                dot_plot[i][j] = 1
            else:
                dot_plot[i][j] = 0
    return dot_plot


def string_to_array(string):
    # converts string to 1D array
    string = string.upper()
    index = string.rfind('\n')

    # print(index)

    string_to_list = ""
    description = ""
    is_description_skipped = False
    for x in string:

        if x == "\n":
            is_description_skipped = True

        if is_description_skipped:
            string_to_list += x
        else:
            description += x

    # print(description)

    string_list = ""

    for x in string_to_list:
        if not x == "\n":
            # do not save
            string_list += x

    return description, list(string_list)


def manual_insert():
    user_input = input("Insert tag:")
    user_data = ">" + user_input + "\n"
    user_input = input("Enter DNA sequence")
    for x in user_input:
        user_data += x

        # print(x)
        # if len(user_data) % 80 == 0:
        #     user_data += "\n"

    return user_data


def read_file():
    file_name = input("Enter file name: ")
    with open(file_name) as file_object:
        contents = file_object.read()
        return contents

    # TO DO


def read_file_from_web(url):
    # lib requests
    return url


def select_method():
    print(
        "Select how do you want to reach the data: \n1. Insert the data manually. \n2. Read the data from a file. \n3. Read the data from the server")
    label = input("select:\n")
    while label != "1" or label != "2" or label != "3":
        if label == "1":
            print("Selected 1st option")
            user_data = manual_insert()
            # print(user_data)
            if user_data is not None:
                return string_to_array(user_data)
            break
        elif label == "2":
            print("Selected 2nd option")
            file = read_file()
            if file is not None:
                return string_to_array(file)
            # print(file)
            break
        elif label == "3":
            print("Selected 3rd option")
            # soon
            break
        else:
            print("Please select correct method ")
            label = input("select:\n")


if __name__ == "__main__":
    main()
