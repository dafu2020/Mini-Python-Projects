import re


def is_email(address: str) -> bool:
    """Check weather a string is an email address

    :param address: a string
    :precondition: address must be a string
    :postcondition: validate if a string is an email address
    :return: if a string is an email address return True, else return False
    """
    # username: 1+ characters->  lowercase and uppercase letters, numbers, or an underscore
    # @
    # domain: 1+ lowercase and uppercase letters, numbers
    # .
    # anything between two and four characters

    email_regex = re.compile(r'(^(\w)+@([a-zA-Z0-9])+\.(\w{2,4})$)')
    match_object = email_regex.search(address)
    if match_object:
        return True
    return False


def main():
    address = input('email: ')
    print(is_email(address))


if __name__ == "__main__":
    main()
