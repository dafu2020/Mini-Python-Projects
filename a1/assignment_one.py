import doctest
import random


def convert_to_roman_numeral(positive_int):
    """
    Decimal to roman numeral conversion.

    The function should accept a single parameter called positive_int, and return it's the roman numeral equivalent.
    Return the Roman numeral as a string.

    Computational Thinking:
    1) Decomposition:
    breaking the positive integer into ones, tens, hundreds, thousands;
        find the roman numerals for each category;
        joining the result.
    2）Patten matching: make 4 lists that contain the ones, tens, hundreds, thousands roman numeral equivalents,
        then find the thousands of representations in the list of the thousands,
        then find the hundreds of representations in the hundreds list and so on.
    3) Algorithms: use list to sort data;
        positive integer use integer division to divide by 1000, the result is used as the index of the
        thousand lists to find the correct roman numeral equivalent at that index.
        Find the remainder, use it for the hundreds.
    4) Generalization: use the same algorithm for the hundreds, tens, and ones.

    :param positive_int: a positive integer in range [1, 10000]
    :precondition: number must be a positive non-zero integer in range [1, 10000]
    :postcondition: converted to the correct roman numeral equivalent
    :return: correctly converted roman numeral equivalent as a string

    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    >>> convert_to_roman_numeral(0)
    'This is not a positive number please re-enter!'
    >>> convert_to_roman_numeral(1998)
    'MCMXCVIII'
    """

    # make lists that contains roman numeral  in corresponding index
    m_list = ["", "M", "MM", "MMM", "MMMM", "MMMMM", "MMMMMM", "MMMMMMM",
              "MMMMMMMM", "MMMMMMMMM", "MMMMMMMMMM"]
    c_list = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x_list = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i_list = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    roman_m = m_list[positive_int // 1000]          # ex) if input number 10000, first 10000//1000  =  10
    roman_c = c_list[(positive_int % 1000) // 100]  # in m_list index 10 is MMMMMMMMMM
    roman_x = x_list[(positive_int % 100) // 10]    # which is the roman numeral equivalent of 10000
    roman_i = i_list[positive_int % 10]

    return roman_m + roman_c + roman_x + roman_i


def colour_mixer():
    """
    A function that mix two primary colours into a secondary colour.

    Computational Thinking:
    1) Decomposition:
        there are three likely situations, first, enter sth other than the primary colors;
        second, enter two same primary colors; third, enter two different primary colors.
    2) Algorithms: use a series of decision making events to find the result of different outputs.

    :precondition: input two different primary colors from "red", "yellow", "blue".
    :postcondition: prints a secondary color according to the inputted primary colors.
    :return: a correct secondary color as a string

    """
    # ask for input and clean the input to the correct value
    color1 = str(input("please input your first color: ")).strip().lower()
    color2 = str(input("please enter your second color: ")).strip().lower()

    # create a list contains all primary colors
    color_list = ["red", "yellow", "blue"]

    # decision making: if both color are primary colors
    if color1 not in color_list or color2 not in color_list:
        print("This is not the correct primary color, please re-enter")
    # decision making: if the two primary colors are identical
    elif color1 == color2 in color_list:
        print("error, please enter two separate primary color!")
    else:
        if color1 == "red":  # ex) decision making: if the first color is red
            if color2 == "yellow":  # ex) decision making: if the second color is yellow
                secondary_color = "orange"
                print(secondary_color)
            else:
                secondary_color = "purple"
                print(secondary_color)
        elif color1 == "yellow":
            if color2 == "red":
                secondary_color = "orange"
                print(secondary_color)
            else:
                secondary_color = "green"
                print(secondary_color)
        else:
            if color2 == "yellow":
                secondary_color = "green"
                print(secondary_color)
            else:
                secondary_color = "purple"
                print(secondary_color)


def time_calculator(seconds):
    """
    A function that express second in the order of days hours minutes seconds.

    Computational Thinking:
    1) Decomposition: find the days, the hours, minutes, and seconds; join the result.
    2) Pattern matching: the logic is similar to the convert_to_roman_numeral(positive_int) function above.
    3) Algorithms: seconds use integer division to divide by 86400 to find how many days are in the entered seconds.
        Calculate the remainder for hours calculation.
    4) Generalization: same calculation for hours, minutes.

    :param seconds: a positive integer
    :precondition: seconds must be a positive non-zero integer
    :postcondition: converts to the correct representation in days, hours, minutes, seconds orders
    :return: correctly converted  days, hours, minutes, seconds as a string

    >>> time_calculator(3000)
    '0 0 50 0'
    >>> time_calculator(12890)
    '0 3 34 50'
    >>> time_calculator(2)
    '0 0 0 2'

    """

    # find days
    day = seconds // 86400
    seconds = seconds % 86400

    # find hours
    hour = seconds // 3600
    seconds = seconds % 3600

    # find minutes
    minute = seconds // 60
    seconds = seconds % 60

    # arrange the days, hours, minutes, seconds in a specific manner as the result
    result = str(day) + " " + str(hour) + " " + str(minute) + " " + str(seconds)

    # print result
    print(result)

    return result


def compound_interest(principal, interest, compound_times, years_to_grow):
    """
    A function to calculate the amount of money earned by compound interest.

    Computational Thinking:
    1) Decomposition: calculate the fraction form of annual interest,
        calculate the amount of money in the account after the specified number of years
        round the results.
    2) Algorithms: use the compound interest math function as algorithms.

    :param principal: a positive float
    :param interest: a positive float
    :param compound_times: a positive integer
    :param years_to_grow: a positive integer
    :precondition: the numbers passed to the function will be positive float or integer
    :postcondition: calculates the correct amount of money in the account after the specified of years
    :return: correctly calculated the amount of money in the account after the elapsed time as a float

    >>> compound_interest(10000, 12, 1, 5)
    17623.42
    >>> compound_interest(10, 10, 2, 10)
    26.53
    >>> compound_interest(15432, 2, 5, 6)
    17395.37


    """
    # convert annual interest into a fraction form
    interest = interest / 100

    #  calculate the amount of money in the account after the specified number of years
    result = principal * ((1 + (interest / compound_times)) ** (compound_times * years_to_grow))

    # round result to two decimal places
    amount_of_money = round(result, 2)
    return amount_of_money


def rock_paper_scissors():
    """
    Rock, paper, scissors game simulators.
    A function allow the user to play one round of rock, paper, scissors with the computer,
    print the computer's choice and print the game result.

    Computational Thinking:
    1) Decomposition: computer makes a random choice; user makes a choice; use the choices between
        computer and user to find the corresponding game result.
    2）Patten matching: similar logic to colour_mixer() above
    3) Algorithms: use list to sort data;
        use a series of decision making events to find the result of different outputs.


    :precondition: the user must input a valid string of "rock" or "paper" or "scissors"
    :postconditon: display the choice that computer made and the result of the game
    :return: none, there is no return value


    """

    index_list = [0, 1, 2]
    index_value = ["rock", "paper", "scissors"]
    computer_win_condition = [["paper", "rock"], ["rock", "scissors"], ["scissors", "paper"]]

    # random generate a number form the index list
    # use this index number to find the corresponding rock, paper, scissors choices
    # in the index_value list
    computer_index = random.choice(index_list)
    computer = index_value[computer_index]

    # clean the user input to correct form
    man = input("Pls Enter: rock, paper, scissors ").strip().lower()

    # decision making: does the user enter something other than rock/paper/scissors?
    if man not in index_value:
        print("Error, wrong input, should enter rock/paper/scissors")
    # decision making: is it a tie situation?
    elif computer == man:
        print("computer: ", computer)
        print("It's a tie")
    # decision making: computer winning situation?
    elif [computer, man] in computer_win_condition:
        print("computer: ", computer)
        print("Computer win")
    else:
        print("computer: ", computer)
        print("you WIN!")


def number_generator():
    """
    A function generate a lottery ticket.
    This function  generate a lottery ticket containing a list of 6 unique numbers in range [1, 49].
    return a list that contains these numbers sorted from lowest to highest.

    Computational Thinking:
    1) Decomposition: random generated six unique numbers in range [1,  49] as a list;
        sort the numbers from lowest to highest.
    2) Algorithms: use random.sample() to generated six unique numbers,
        use sort() to sort the list from lowest to highest

    precondition: none
    postconditon: generate a list containing six random numbers from 1 to 49  and sorted from lowest to highest
    :return: a correctly generated list of six unique numbers in range [1, 49]
            that are sorted from lowest to highest as a string

    """

    # random generate a list of six unique numbers from 1 to 49
    list_number = random.sample(range(1, 50), 6)

    # sort the list from the lowest number to the highest number
    result = sorted(list_number)
    return result


def number_translator():
    """
    A function translate a telephone number that contains alphabetical letters into the numerical equivalent

    Computational Thinking:
    1) Decomposition: convert the input telephone number into a list;
        find the index location of the alphabetical letter and change it to the corresponding number;
        generate a new list containing the translated telephone number;
    2）Patten matching: similar logic to convert_to_roman_numeral() above,
        make 8 lists that contain each number's corresponding letter in the keypad.
    3) Algorithms: use the properties of the list, find the index location of letter A/B/C in the number_list;
        substitute them to the corresponding number, 2.
    4) Generalization：use the same approach to convert letters to 3-9.

    :precondition: must enter a 10-character (number or letter) telephone number in the format XXX-XXX- XXXX
    :postcondition translates into a correct 10-number telephone number in the format XXX-XXX- XXXX
    :return: a correctly  translated 10-number telephone number in the format XXX-XXX- XXXX as a string

    """

    # make eight lists from number 2-9, each contains the corresponding letters
    list2 = ["A", "B", "C"]
    list3 = ["D", "E", "F"]
    list4 = ["G", "H", "I"]
    list5 = ["J", "K", "L"]
    list6 = ["M", "N", "O"]
    list7 = ["P", "Q", "R", "S"]
    list8 = ["T", "U", "V"]
    list9 = ["W", "X", "Y", "Z"]

    # clean the format the entered number
    number_input = input("Please input a telephone number: ex)XXX-XXX-XXXX ")
    # convert input telephone number into a list called number_list
    number_list = list(number_input.upper().strip())

    # for each item in the number list
    for i in number_list:
        if i in list2:  # ex) decision making: list2 contains these letters?
            number_list[number_list.index(i)] = "2"  # replace the letters with 2
        elif i in list3:
            number_list[number_list.index(i)] = "3"
        elif i in list4:
            number_list[number_list.index(i)] = "4"
        elif i in list5:
            number_list[number_list.index(i)] = "5"
        elif i in list6:
            number_list[number_list.index(i)] = "6"
        elif i in list7:
            number_list[number_list.index(i)] = "7"
        elif i in list8:
            number_list[number_list.index(i)] = "8"
        elif i in list9:
            number_list[number_list.index(i)] = "9"

    # joining the list
    new_list = "".join(number_list)
    return new_list


def main():
    """
    Test the functions in this module.

    :return: the result of doctests
    """
    doctest.testmod()


if __name__ == "__main__":
    main()
