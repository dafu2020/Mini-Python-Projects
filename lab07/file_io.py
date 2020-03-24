"""
Demonstrate how to find the top ten occurrence words from a text file.
"""
import doctest


def open_text(file_name: str) -> str:
    """Open and read file.

    :param file_name: a string
    :precondition: file_name must be a file
    :postcondition: open and read a file
    :return: file opens a str

    >>> my_file = 'doctest_1.txt'
    >>> open_text(my_file)
    'this file is for the purpose of doctest:'

    >>> my_file = 'doctest_2.txt'
    >>> open_text(my_file)
    'this is also a file that is for the purpose of doctest: a a a a a a A,A,A B. b, b'
    """
    # open file
    with open(file_name) as file_object:
        text = file_object.read()
    return text


def format_text(text: str) -> list:
    """Format the text into individual words

    :param text: a string
    :precondition: file_name must be a file
    :postcondition: remove punctuation marks; convert all character into lowercase;
                    split the entire text into individual words in a list
    :return: the formatted individual words as one list

    >>> my_text = 'this file IS for the PurPose of doctest:'
    >>> format_text(my_text)
    ['this', 'file', 'is', 'for', 'the', 'purpose', 'of', 'doctest']

    >>> my_text =  'Alice, was beginning to get very tired of sitting by HER sister!'
    >>> format_text(my_text)
    ['alice', 'was', 'beginning', 'to', 'get', 'very', 'tired', 'of', 'sitting', 'by', 'her', 'sister']
    """
    # replace punctuation mark with ' '(space)
    for character in ',.~!@#$%^&*()_+-={}[]|/<>:\'\";':
        text = text.replace(character, '')
    text = text.lower()

    # get the individual words from the text
    word_in_text = text.split()

    return word_in_text


def word_occurrence(word_in_text: list) -> dict:
    """Count the word occurrence

    :param word_in_text: a list
    :precondition: word_in_text must be a list
    :postcondition: count the word occurrence and store in a dictionary
    :return: the counted word occurrence and responding words stored as a dictionary

    >>> my_words = ['this', 'file', 'is', 'for', 'the', 'purpose', 'of', 'doctest']
    >>> word_occurrence(my_words)
    {'this': 1, 'file': 1, 'is': 1, 'for': 1, 'the': 1, 'purpose': 1, 'of': 1, 'doctest': 1}

    >>> my_words = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    >>> word_occurrence(my_words)
    {1: 1, 2: 2, 3: 3, 4: 4}
    """

    # count the frequency of the text
    word_count = {}
    for word in word_in_text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def top_ten(word_count: dict) -> list:
    """Find the top ten occurrence words

    :param word_count: a dictionary
    :precondition: must be a dictionary containing words and word occurrence pairs
    :postcondition: sort the dictionary and find the top ten words and word occurrence pairs and store in a list
    :return: the top ten words and the corresponding word occurrence as a list

    >>> my_dict = { 0:0, 1: 1, 2: 2, 3: 3, 4: 4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10}
    >>> top_ten(my_dict)
    [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]

    >>> my_dict = {'nothing':1, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10}
    >>> top_ten(my_dict)
    [[10, 'ten'], [9, 'nine'], [8, 'eight'], [7, 'seven'], [6, 'six'], [5, 'five'], [4, 'four'], [3, 'three'], [2, 'two'], [1, 'one']]

    """

    # the sorted nested list = sorting the dictionary by value
    sorted_word_count = sorted([value, key] for (key, value) in word_count.items())

    # find the top ten
    occurrence_list = []
    for i in reversed(list(range(-10, 0))):
        occurrence_list.append(sorted_word_count[i])

    return occurrence_list


def print_result(occurrence_list: list) -> None:
    """Print the result of top ten word occurrence

    :param occurrence_list: a list
    :precondition: must be a list containing the top ten words and corresponding word occurrence pairs
    :postcondition: print the result from top one to top ten in a word- word occurrence format

    >>> my_occurrence_list = [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]
    >>> print_result(my_occurrence_list)
    10 - 10
    9 - 9
    8 - 8
    7 - 7
    6 - 6
    5 - 5
    4 - 4
    3 - 3
    2 - 2
    1 - 1

    >>> my_occurrence_list=[[10, 'ten'], [9, 'nine'], [8, 'eight'], [7, 'seven'], [6, 'six'], [5, 'five'], [4, 'four'], [3, 'three'], [2, 'two'], [1, 'one']]
    >>> print_result(my_occurrence_list)
    ten - 10
    nine - 9
    eight - 8
    seven - 7
    six - 6
    five - 5
    four - 4
    three - 3
    two - 2
    one - 1

    """

    # convert the nested list to dictionary form for printing purpose
    final_dic = {}
    for i in occurrence_list:
        for _ in i:
            dic_key = i[1]
            final_dic[dic_key] = i[0]

    # print the word - frequency
    for key, value in final_dic.items():
        print(key, "-", value)


def main():
    """
    Drive the program.
    """
    doctest.testmod()
    my_file = input("Please enter the name of the text file you wish to count the top ten words(with .txt): ")

    try:
        my_text = open_text(my_file)
        individual_word = format_text(my_text)
        word_frequency = word_occurrence(individual_word)
        top_ten_words = top_ten(word_frequency)
        print_result(top_ten_words)

    except FileNotFoundError:
        print('No such file found under the directory')


if __name__ == '__main__':
    main()
