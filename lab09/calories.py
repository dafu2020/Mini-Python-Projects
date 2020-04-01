import doctest


def add_calories_dictionary(new_food: str) -> dict:
    """Add a food and it's calories in the food dictionary

    :param new_food: a string
    :precondition: new_food must be a string
    :postcondition: update the calories_dictionary with new food and the corresponding calories
    :return: the updated calories_dictionary as a dictionary
    """
    # have the original calorie dictionary
    calories_dict = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
                     "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
                     "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102
                     }
    try:
        new_calories = int(input(f'Enter calories for {new_food}: '))
        # append the new food and new calories to the calorie dictionary
        calories_dict[new_food] = new_calories
    # make sure the new calorie is a number
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
    # using list comprehension to store all the name of the foods from the calorie dictionary
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
    # add all the calories together
    for item in food_dict:
        total_calories += food_dict[item]
    return total_calories


def calculate_calorie_average(food_dict: dict) -> float:
    """Calculate the average calorie

    :param food_dict: a dict
    :precondition: food_dict must be a dictionary
    :postcondition: calculate the average calorie of a food dictionary
    :return: the calculated average calorie as an float

    >>> food_dict_1 = {'peach':10, 'apple':20}
    >>> calculate_calorie_average(food_dict_1)
    15.0

    >>> food_dict_2 = {"carrot": 5, "apple": 5, "bread": 5}
    >>> calculate_calorie_average(food_dict_2)
    5.0
    """
    total_calories = calculate_total_calorie(food_dict)
    # calculate the average calorie from the total calorie
    average_calories = total_calories / len(food_dict)
    return average_calories


def print_calories(food_items: list, total_calories: int, average_calories: float) -> None:
    """Print the calories information of a list of food

    :param food_items: a list
    :param total_calories: an integer
    :param average_calories: a float
    :precondition: food_items must be a list containing foods;
                    total_calories must be an integer;
                    average_calories: must be a float
    :postcondition: print out the calorie information of a list of foods
    >>> foods = ['apple', 'Mapo Tofu', 'pear']
    >>> total_calories = 30
    >>> average_calories = 10.0
    >>> print_calories(foods, total_calories, average_calories)
    <BLANKLINE>
    Food Items: ['apple', 'Mapo Tofu', 'pear']
    Total Calories: 30 Average Calories: 10.0
    <BLANKLINE>

    >>> foods = ['orange', 'hot cocoa']
    >>> total_calories = 20
    >>> average_calories = 10.0
    >>> print_calories(foods, total_calories, average_calories)
    <BLANKLINE>
    Food Items: ['orange', 'hot cocoa']
    Total Calories: 20 Average Calories: 10.0
    <BLANKLINE>
    """
    print("\nFood Items:", food_items)
    print("Total Calories:", total_calories,
          "Average Calories: %0.1f\n" % average_calories)


def main():
    """
    Drive the program.
    """
    doctest.testmod()

    # create a while loop for inputting new food
    # user can enter 'q' to exit the program
    while True:
        user_input = input("Enter food item to add, or 'q' to exit: ").lower().strip()
        if user_input == 'q':
            return False
        user_food_dict = add_calories_dictionary(user_input)
        print_calories(food_items=food_name_list(user_food_dict),
                       total_calories=calculate_total_calorie(user_food_dict),
                       average_calories=calculate_calorie_average(user_food_dict))


if __name__ == '__main__':
    main()
