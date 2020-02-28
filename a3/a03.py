# GAME MAP
"""
  0    1   2   3   4
_____________________
|   |   |   |   |    |0
_____________________
|   |   |   |   |    |1
_____________________
|   |   |   |   |    |2
_____________________
|   |   |   |   |    |3
_____________________
|   |   |   |   |    |4
_____________________
"""
area_name = ''
description = 'description'
examination = 'examine'
solved = False
north = 'north'
south = 'south'
east = 'east'
west = 'west'

solved_places = {'00': False, '01': False, '02': False, '03': False, '04': False,
                 '10': False, '11': False, '12': False, '13': False, '14': False,
                 '20': False, '21': False, '22': False, '23': False, '24': False,
                 '30': False, '31': False, '32': False, '33': False, '34': False,
                 '40': False, '41': False, '42': False, '43': False, '44': False}
game_map = {
    '00': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '',
        south: '10',
        east: '01',
        west: ''
    },
    '01': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '',
        south: '11',
        east: '02',
        west: '00'
    },
    '02': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '',
        south: '12',
        east: '03',
        west: '01'
    },
    '03': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '',
        south: '13',
        east: '04',
        west: '02'
    },
    '04': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '',
        south: '14',
        east: '',
        west: '03'
    },
    '10': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '00',
        south: '20',
        east: '11',
        west: ''
    },
    '11': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '01',
        south: '21',
        east: '12',
        west: '10'
    },
    '12': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '02',
        south: '22',
        east: '13',
        west: '11'
    },
    '13': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '03',
        south: '23',
        east: '14',
        west: '12'
    },
    '14': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '04',
        south: '24',
        east: '',
        west: '13'
    },
    '20': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '10',
        south: '30',
        east: '21',
        west: ''
    },
    '21': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '11',
        south: '31',
        east: '22',
        west: '20'
    },
    '22': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '12',
        south: '32',
        east: '23',
        west: '21'
    },
    '23': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '13',
        south: '33',
        east: '24',
        west: '22'
    },
    '24': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '14',
        south: '34',
        east: '',
        west: '23'
    },
    '30': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '20',
        south: '40',
        east: '31',
        west: ''
    },
    '31': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '21',
        south: '41',
        east: '32',
        west: '30'
    },
    '32': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '22',
        south: '42',
        east: '33',
        west: '31'
    },
    '33': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '23',
        south: '43',
        east: '34',
        west: '32'
    },
    '34': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '24',
        south: '44',
        east: '',
        west: '33'
    },
    '40': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '30',
        south: '',
        east: '41',
        west: ''
    },
    '41': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '31',
        south: '',
        east: '42',
        west: '40'
    },
    '42': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '32',
        south: '',
        east: '43',
        west: '41'
    },
    '43': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '33',
        south: '',
        east: '44',
        west: '42'
    },
    '44': {
        area_name: '',
        description: '',
        examination: '',
        solved: False,
        north: '34',
        south: '',
        east: '',
        west: '43'
    }
}
