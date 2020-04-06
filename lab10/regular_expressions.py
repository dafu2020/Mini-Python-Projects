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
    """Check if a name has a last name of Nakamoto

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
    :return: if a poker hand is invalid return False, else return True

    >>> is_poker('aaaaa')
    False
    >>> is_poker('kkkkq')
    True
    """
    # can find invalid pattern and return False, else return True
    poker_regex = re.compile(r'\w{6,}'  # card set cannot be more than 5 cards
                             r'|^\w{,4}$'  # card set cannot be less than 5 cards
                             r'|[^2-9akqjt]'  # card set cannot contain invalid cards other than 2-9, a, k, q, t
                             r'|([2-9akqjt])\1{4}', re.I)  # if same card more than 5 is also consider invalid
    # case in-sensitive
    match_object = poker_regex.search(hand)
    if match_object:
        return False
    return True


def main():
    """
    Drive the program
    """
    doctest.testmod()

    # check email
    user_email = 'jane_doe@gmail.com'
    print('check email: ', is_email(user_email))

    # check name
    user_name = 'Alice Nakamoto'
    print('check name: ', is_nakamoto(user_name))

    # check poker
    poker_hand = 'aaa88'
    print('check poker: ', is_poker(poker_hand))


if __name__ == "__main__":
    main()
