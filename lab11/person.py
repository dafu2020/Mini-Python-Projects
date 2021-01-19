class Person:

    # construct a new person
    def __init__(self, prob_infection: float, prob_recovery: float, initial_hp: int, role: str) -> None:
        """
        Initialize a new Person

        :param prob_infection: a float
        :param prob_recovery:  a float
        :param initial_hp: an integer
        :param role: a string
        :precondition: prob_infection must be a float representing the chance of a person getting infected;
                       prob_recovery must be a float representing the chance of a person will recover;
                       initial_hp must be an positive integer representing the initial HP of a person;
                       role must be a string representing the occupational role of a person.
        :postcondition: initialized Person as an object
        """
        # make sure person's initial HP is a positive number
        if initial_hp > 0:
            self.__hp = initial_hp
        raise ValueError("Person HP have to be bigger than zero!!")

        # set the probability of this person getting infected with the virus
        self.__prob_recovery = prob_recovery
        self.__prob_infection = prob_infection

        # set the occupational role of this person
        self.__role = role

        # the default states of a person
        self.__infected = False  # not infected
        self.__recovered = False  # not recovered because this person has not caught the virus yet
        self.__medical_assist = False
        self.__ppe = False
        self.__deceased = False

        # include getters and setters for all variables(object attributes)

# def is_infected()
# returns true if infected, else false

# def is_recovered()
# returns true if recovered, else false

# def set_infected()
# sets infected attribute - if already infected, do nothing, else change to True

# ... add more getters/setters
