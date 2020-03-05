import urllib

import requests


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

    # filtering
    window_size = input("Enter window size: ")

    threshold = input("Enter threshold: ")

    window_size = int(str(window_size))

    threshold = int(str(threshold))

    filtered_dot_plot = filter_dot_plot(window_size, threshold, dot_plot)

    show_filtered_dot_plot(filtered_dot_plot)

    # show matrix as a figure
    # title,axes,legends,scale

    # save matrix to a graphical file


def show_filtered_dot_plot(filtered_dot_plot):
    for i in range(len(filtered_dot_plot)):
        for j in range(len(filtered_dot_plot[i])):
            print(filtered_dot_plot[i][j], end=' ')
        print()


def filter_dot_plot(window_size, threshold, dot_plot):
    filtered_dot_plot = dot_plot
    window_x = 0
    window_y = 0
    window_x_range = window_size
    window_y_range = window_size

    for i in range(len(dot_plot) - window_size):
        window_x += i
        print(window_x)
        window_x_range += i
        print(window_x_range)
        for j in range(len(dot_plot[i]) - window_size):
            window_y += j
            print(window_y)
            window_y_range += j
            print(window_y_range)

            counter = 0

            for window_x in range(window_x_range):
                for window_y in range(window_y_range):
                    if window_x == window_y:
                        if dot_plot[window_x][window_y] == 1:
                            counter += 1

            if counter >= window_size - threshold:

                for window_x in range(window_x_range):
                    for window_y in range(window_y_range):
                        if window_x == window_y:
                            if dot_plot[window_x][window_y] == 1:
                                filtered_dot_plot[i][j] = 1
                            else:
                                filtered_dot_plot[i][j] = 0
                        else:
                            filtered_dot_plot[i][j] = 0

    return filtered_dot_plot


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


def read_file_from_web(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    print(text)
    return text


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
            db = 'nuccore'
            nuccore_id = input("Enter id:")
            # covid 2019 id = 1798174254
            url_address = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=%s&id=%s&rettype=fasta&retmode=text" % (
                db, nuccore_id)
            file = read_file_from_web(url_address)
            return string_to_array(file)
            break
        else:
            print("Please select correct method ")
            label = input("select:\n")


if __name__ == "__main__":
    main()
