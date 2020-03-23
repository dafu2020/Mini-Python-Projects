class Name:
    def __init__(self, first_name,  middle_name='', last_name=''):
        name_list = [first_name, middle_name, last_name]
        if len(name_list) == 1:
            self.first_name = first_name.title()
        elif len(name_list) == 2:
            self.first_name = first_name.title()
            self.last_name = last_name.title()
            self.last_name = middle_name.title()
        else:
            self.first_name = first_name.title()
            self.middle_name = middle_name.title()
            self.last_name = last_name.title()

    def get_name(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def length(self):
        return len(self.first_name) + len(self.middle_name) + len(self.last_name)

    def change_first_name(self, first_name):
        self.first_name = first_name.title()

    def change_middle_name(self, middle_name):
        self.middle_name = middle_name.title()

    def change_last_name(self, last_name):
        self.last_name = last_name.title()

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def __repr__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


def main():
    xindi = Name('Xindi', 'Lu')
    xindi_middle_name = Name('Xindi', 'middle', 'lu')

    print(xindi)
    print(xindi_middle_name)

    # print name
    print(xindi.get_name())
    print(xindi_middle_name.get_name())

    # change first name
    xindi.change_first_name('cindy')
    print(xindi)

    # change last name
    xindi.change_last_name('Sun')
    print(xindi)

    # name length
    print(xindi.length())

    print(repr(xindi_middle_name))


if __name__ == "__main__":
    main()
