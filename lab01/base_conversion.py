def base_conversion():
    base_destination = int(input("Pls enter the destination base (between 2-9):"))
    maximum_value = int(base_destination ** 4 - 1)
    print("the maximum value you can enter is:", maximum_value)
    # print("the maximum value you can enter is %d" % maximum_value)

    value_entered = int(input("Pls enter a base 10 number for base conversion(less or equal than maximum_value):"))

    first_quotient = value_entered // base_destination
    first_remainder = value_entered % base_destination

    second_quotient = first_quotient // base_destination
    second_remainder = first_quotient % base_destination

    third_quotient = second_quotient // base_destination
    third_remainder = second_quotient % base_destination

    forth_quotient = third_quotient // base_destination
    forth_remainder = third_quotient % base_destination

    combine_remainder = (str(forth_remainder) + str(third_remainder) + str(second_remainder) + str(first_remainder))
    result = int(combine_remainder)

    print("result is", result, " base", base_destination)
    return result


def main():
    base_conversion()


if __name__ == "__main__":
    main()
