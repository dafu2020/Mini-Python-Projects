def base_conversion():
    """Convert base.
    One algorithm for converting a base 10 number to another base.
    """

    base_destination = int(input("Pls enter the destination base (between 2-9):"))
    if 2 <= base_destination <= 9 :
        maximum_value = int(base_destination ** 4 - 1)
        print("the maximum value you can enter is:", maximum_value)
        # print("the maximum value you can enter is %d" % maximum_value)

        value_entered = int(input("Pls enter a base 10 number for base conversion(less or equal than maximum_value):"))

        def remainder_calculation(value, base):
            first_quotient = value // base
            first_remainder = value % base

            second_quotient = first_quotient // base
            second_remainder = first_quotient % base

            third_quotient = second_quotient // base
            third_remainder = second_quotient % base

            forth_quotient = third_quotient // base
            forth_remainder = third_quotient % base

            return int(str(forth_remainder) + str(third_remainder) + str(second_remainder) + str(first_remainder))

        result = remainder_calculation(value_entered, base_destination)
        print("Ur result is: ", result)
        return result

    else:
        print("error:please enter the correct base")
        quit()



def main():
    base_conversion()


if __name__ == "__main__":
    main()
