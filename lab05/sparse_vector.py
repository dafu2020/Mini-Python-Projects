"""
Demonstrate how to calculate the sum and the dot product of two sparse vectors as dictionaries
"""


# store vector as dictionary
def vector_to_dictionary(sparse_vector=list) -> dict:
    length_vector = len(sparse_vector)
    my_dic = {}
    for keys, values in enumerate(sparse_vector):
        my_dic[keys] = values
        if my_dic[keys] == 0:
            my_dic.pop(keys)
    my_dic['length'] = length_vector
    return my_dic


# add the vector dictionaries
def sparse_add(vector_one=dict, vector_two=dict) -> dict:
    if vector_one['length'] == vector_two['length']:
        add_dic = {'length': vector_one['length']}
        for key_one in vector_one:
            if key_one not in vector_two:
                add_dic[key_one] = vector_one[key_one]
            elif key_one in vector_one and key_one != 'length':
                add_dic[key_one] = vector_one[key_one] + vector_two[key_one]
                if add_dic[key_one] == 0:
                    add_dic.pop(key_one)
        for key_two in vector_two:
            if key_two not in vector_one:
                add_dic[key_two] = vector_two[key_two]
    return add_dic


# sum the element-wise products of their elements
def sparse_dot_product(vector_one=dict, vector_two=dict) -> dict:
    if vector_one['length'] == vector_two['length']:
        product_dic = {'length': vector_one['length']}
        for key_one in vector_one:
            if key_one not in vector_two:
                product_dic[key_one] = vector_one[key_one]
            elif key_one in vector_one and key_one != 'length':
                product_dic[key_one] = vector_one[key_one] * vector_two[key_one]
                if product_dic[key_one] == 0:
                    product_dic.pop(key_one)
        for key_two in vector_two:
            if key_two not in vector_one:
                product_dic[key_two] = vector_two[key_two]
    return product_dic


# vec_1 = [1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 4]
# vec_2 = [1, 0, 1, 0, 2, 0, 1, 0, 0, 1, 0]

dic1 = {0: 1, 2: 1, 4: 2, 6: 1, 9: 1, 'length': 11}
dic2 = {0: -1, 3: 2, 7: 3, 10: 4, 'length': 11}

print(sparse_dot_product(dic2, dic1))
