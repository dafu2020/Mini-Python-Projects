# start with a empty dict?
# both input in main?
def add_calories_dictionary(new_food: str) -> dict:
    """Build a dictionary for food and it's calories

    :param new_food: a string
    :precondition: new_food must be a string
    :postcondition: update the calories_dictionary with new food and the corresponding calories
    :return: the updated calories_dictionary as a dictionary
    """
    try:
        calories_dict = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
                         "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
                         "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102
                         }
        new_calories = int(input(f'Please enter the calorie of the {new_food}: '))
        calories_dict[new_food] = new_calories
    except ValueError:
        print('Please enter a integer for calorie')

    return calories_dict


def food_name_list(food_dict: dict) -> list:
    """Create a list containing food names

    :param food_dict: must be a dict
    :precondition: food_dict must be a dict
    :postcondition: store all the name of the food in the dictionary in a list
    :return: a list containing all food names from the food dictionary

    >>> food_dict_1 = {'peach':10, 'apple':20}
    >>> food_name_list(food_dict_1)
    ['apple', 'peach']

    >>> food_dict_2 = {"carrot": 5, "apple": 5, "bread": 5}
    >>> food_name_list(food_dict_2)
    ['apple', 'bread', 'carrot']
    """
    food_list = [item for item in food_dict]
    return sorted(food_list)


def calculate_total_calorie(food_dict: dict) -> int:
    """Calculate total calories

    :param food_dict: a dict
    :precondition: food_dict must be a dictionary
    :postcondition: calculate the total calorie of a food dictionary
    :return: the calculated total calorie as an integer

    >>> food_dict_1 = {'peach':10, 'apple':20}
    >>> calculate_total_calorie(food_dict_1)
    30

    >>> food_dict_2 = {"carrot": 5, "apple": 5, "bread": 5}
    >>> calculate_total_calorie(food_dict_2)
    15

    """
    total_calories = 0
    for item in food_dict:
        total_calories += food_dict[item]
    return total_calories


def calculate_calorie_average(food_dict: dict) -> int:
    """Calculate the average calorie

    :param food_dict: a dict
    :precondition: food_dict must be a dictionary
    :postcondition: calculate the average calorie of a food dictionary
    :return: the calculated average calorie as an integer

    >>> food_dict_1 = {'peach':10, 'apple':20}
    >>> calculate_calorie_average(food_dict_1)
    15.0

    >>> food_dict_2 = {"carrot": 5, "apple": 5, "bread": 5}
    >>> calculate_calorie_average(food_dict_2)
    5.0
    """
    total_calories = calculate_total_calorie(food_dict)
    average_calories = total_calories / len(food_dict)
    return average_calories


def main():
    """
    Drive the program.
    """
    doctest.testmode()

    while True:
        user_input = input("Enter food item to add, or 'q' to exit: ").lower().strip()
        if user_input == 'q':
            return False
        user_food_dict = add_calories_dictionary(user_input)
        print("\nFood Items:", food_name_list(user_food_dict))
        print("Total Calories:", calculate_total_calorie(user_food_dict),
              "Average Calories: %0.1f\n" % calculate_calorie_average(user_food_dict))


if __name__ == '__main__':
    main()
