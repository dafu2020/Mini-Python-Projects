def add_calories_dictionary(user_input: str) -> dict:
    """Build a dictionary for food and it's calories.

    :param user_input: a string
    :precondition:
    :postcondition:
    :return:
    """
    calories_dict = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
                     "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
                     "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102
                     }
    new_food = user_input
    new_calories = int(input(f'Please enter the calorie of the {new_food}: '))
    calories_dict[new_food] = new_calories
    return calories_dict


def food_name_list(food_dict: dict) -> list:
    """

    :param food_dict:
    :return:
    """
    food_list = []
    for key in food_dict:
        food_list.append(key)
    return sorted(food_list)


def calculate_total_calorie(food_dict: dict) -> int:
    """

    :param food_dict:
    :return:
    """
    total_calories = 0
    for item in food_dict:
        total_calories += food_dict[item]
    return total_calories


def calculate_calorie_average(food_dict: dict) -> int:
    """Calculate the average calorie

    :param food_dict:
    :return:
    """
    total_calories = calculate_total_calorie(food_dict)
    average_calories = total_calories / len(food_dict)
    return average_calories


def main():
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
