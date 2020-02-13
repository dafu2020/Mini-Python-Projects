from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import dnd


class Test(TestCase):
    @patch('builtins.input', side_effect=['-1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_nothing(self, mock_stdout, mock_inputs):
        actual = {
            'Name': 'lyli',
            'Strength': 10,
            'Intelligence': 5,
            'Wisdom': 100,
            'Dexterity': 9,
            'Constitution': 20,
            'Charisma': 9,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Elf',
            'HP': [20, 20]}
        dnd.choose_inventory(actual)
        print(actual)
        expected = 'Welcome to the Olde Tyme Merchant!\n \nHere is what we have for sale:\n \n1. sword\n2. dagger' \
                   '\n3. Iris(sword)\n4. a stack of cash from Rihanna\n5. Black Unicorn Relic Steel Sword' \
                   '\n6. Flamethrower\n7. W870 Shotgun\n8. mario‘s hat\n9. Silence Glaive\n10.Crystal Carillon\n' \
                   '{\'Name\': \'lyli\', \'Strength\': 10, \'Intelligence\': 5, \'Wisdom\': 100, \'Dexterity\': 9, ' \
                   '\'Constitution\': 20, \'Charisma\': 9, \'inventory\': [], \'experience points\': 0, ' \
                   '\'class\': \'sorcerer\', \'Race\': \'Elf\', \'HP\': [20, 20]}\n'

        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=['1', '-1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_one_thing(self, mock_stdout, mock_inputs):
        actual = {
            'Name': 'lyli',
            'Strength': 10,
            'Intelligence': 5,
            'Wisdom': 100,
            'Dexterity': 9,
            'Constitution': 20,
            'Charisma': 9,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Elf',
            'HP': [20, 20]}
        dnd.choose_inventory(actual)
        print(actual)
        expected = 'Welcome to the Olde Tyme Merchant!\n \nHere is what we have for sale:\n \n1. sword\n2. dagger' \
                   '\n3. Iris(sword)\n4. a stack of cash from Rihanna\n5. Black Unicorn Relic Steel Sword' \
                   '\n6. Flamethrower\n7. W870 Shotgun\n8. mario‘s hat\n9. Silence Glaive\n10.Crystal Carillon\n' \
                   'Welcome to the Olde Tyme Merchant!\n \nHere is what we have for sale:\n \n1. sword\n2. dagger' \
                   '\n3. Iris(sword)\n4. a stack of cash from Rihanna\n5. Black Unicorn Relic Steel Sword' \
                   '\n6. Flamethrower\n7. W870 Shotgun\n8. mario‘s hat\n9. Silence Glaive\n10.Crystal Carillon\n' \
                   '{\'Name\': \'lyli\', \'Strength\': 10, \'Intelligence\': 5, \'Wisdom\': 100, \'Dexterity\': 9, ' \
                   '\'Constitution\': 20, \'Charisma\': 9, \'inventory\': [\'sword\'], \'experience points\': 0, ' \
                   '\'class\': \'sorcerer\', \'Race\': \'Elf\', \'HP\': [20, 20]}\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

