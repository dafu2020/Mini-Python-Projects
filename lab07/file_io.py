import doctest

def top_ten_words(file_name: str) -> None:
    """Count top ten word of a file.

    :param file_name: a string and a text file
    :precondition: file_name must be a string and a text file
    :postcondition: Count and print the top ten word of a file
    :return: the correctly counted and printed result of the top ten word of a file

    >>> my_file = 'moby_dick.txt'
    >>> top_ten_words(my_file)
    the - 14508
    of - 6700
    and - 6434
    a - 4690
    to - 4657
    in - 4201
    that - 2939
    his - 2519
    it - 2356
    i - 1942

    >>> my_file = 'alice.txt'
    >>> top_ten_words(my_file)
    the - 1804
    and - 912
    to - 797
    a - 684
    of - 622
    she - 538
    it - 529
    said - 462
    in - 425
    you - 418

    """
    text = open(file_name, 'r').read()
    # replace punctuation mark with ' '(space)
    for character in ',.~!@#$%^&*()_+-={}[]|/<>:\'\";':
        text = text.replace(character, '')
    text = text.lower()

    # get the individual words from the text
    word_in_text = text.split()

    # count the frequency of the text
    word_count = {}
    for word in word_in_text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # the sorted nested list = sorting the dictionary by value
    sorted_word_count = sorted([value, key] for (key, value) in word_count.items())

    # find the top ten
    new_list = []
    for i in reversed(list(range(-10, 0))):
        new_list.append(sorted_word_count[i])

    # convert the nested list to dictionary form for printing purpose
    final_dic = {}
    for i in new_list:
        for _ in i:
            dic_key = i[1]
            final_dic[dic_key] = i[0]

    # print the word - frequency
    for key, value in final_dic.items():
        print(key, "-", value)


def main():
    doctest.testmod()
    my_file = input("Please enter the name of the text file you wish to count the top ten words(with .txt): ")

    try:
        top_ten_words(my_file)
    except FileNotFoundError:
        print('No such file found under the directory')


if __name__ == '__main__':
    main()
