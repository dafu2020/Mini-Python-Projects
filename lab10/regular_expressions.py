import doctest
import re


def is_email(address: str) -> bool:
    """Check weather a string is an email address

    :param address: a string
    :precondition: address must be a string
    :postcondition: validate if a string is an email address
    :return: if a string is an email address return True, else return False

    >>> email_address = "jane@hotmail.com"
    >>> is_email(email_address)
    True

    >>> email_address = "jane.doe@hotmail.com"
    >>> is_email(email_address)
    False
    """
    # username: 1+ characters->  lowercase and uppercase letters, numbers, or an underscore
    # @
    # domain: 1+ lowercase and uppercase letters, numbers
    # .
    # anything between two and four characters

    email_regex = re.compile(r'(^([\w+-])+@([a-zA-Z0-9-+])+\.(\w{2,4})$)')
    match_object = email_regex.search(address)
    if match_object:
        return True
    return False


def is_nakamoto(name: str) -> bool:
    """ Check if a name has a last name of Nakamoto

    :param name: a string
    :precondition: name must be a string
    :postcondition: validate if a name string has a last name of Nakamoto
    :return: if a name string has a last name of Nakamoto return True, else return False

    >>> my_name = 'Satoshi Nakamoto'
    >>> is_nakamoto(my_name)
    True

    >>> my_name = 'Sato_shi Nakamoto'
    >>> is_nakamoto(my_name)
    False
    """
    nakamoto_regex = re.compile(r'^[A-Z]([a-z])* Nakamoto$')
    match_object = nakamoto_regex.search(name)
    if match_object:
        return True
    return False


def is_poker(hand: str) -> bool:
    """Validate a poker hand

    :param hand: a string
    :precondition: hand must be a five character string
    :postcondition: validate a poker hand
    :return: if a poker hand is valid return True, else return False

    >>> is_poker('aaaaa')
    False
    >>> is_poker('kkkkq')
    True
    """
    # chris says no Joker
    # can find invalid pattern and return False, else return True
    poker_regex = re.compile(r'\w{6,}'  # card set cannot be more than 5 cards
                             r'|^\w{,4}$'  # card set cannot be less than 5 cards
                             r'|[^2-9akqt]'  # card set cannot contain invalid cards other than 2-9, a, k, q, t
                             r'|a{5}'   # if same card more than 5 is also consider invalid
                             r'|k{5}'
                             r'|q{5}'
                             r'|t{5}'
                             r'|2{5}'
                             r'|3{5}'
                             r'|4{5}'
                             r'|5{5}'
                             r'|6{5}'
                             r'|7{5}'
                             r'|8{5}'
                             r'|9{5}', re.I)    # case in-sensitive
    match_object = poker_regex.search(hand)
    if match_object:
        return False
    return True


def main():
    """
    Drive the program
    """
    doctest.testmod
    # print(is_poker('qqqqj'))


if __name__ == "__main__":
    main()
