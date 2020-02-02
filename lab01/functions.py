def format_name(first_name, last_name):
    """Inside functions.py, implement (create) a function called format_name. The format_name function
must accept two strings, a first name and a last name."""

    full_name = first_name.strip().capitalize() + " " + last_name.strip().capitalize()
    print(full_name)
    return full_name


def main():
    format_name(first_name=input("pls enter first name:"), last_name=input("pls enter last name:"))


if __name__ == "__main__":
    main()


def tripler(string):
    """(str)->str
    Implement a function called tripler. The tripler function must accept a parameter (type doesn’t
matter) and return a string that represents the parameter tripled."""
    string = str(input('Lets triple:'))
    string = string * 3
    print(string)
    return string


def this_year(now):
    new_year = int(10 * 9 * 8 + (7 + 6) * 5 * 4 * (3 + 2) * 1)
    print(new_year)
    return new_year

