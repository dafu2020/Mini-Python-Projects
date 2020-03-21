def top_ten_words(file_name):
    text = open(file_name, 'r').read()
    # replace punctuation mark with ' '(space)
    for character in ',.~!@#$%^&*()_+-={}[]|/<>:\'\";':
        text = text.replace(character, '')
    text = text.lower()

    # get the individual words from the text
    word_in_text = text.split()

    # count the frequency of the text
    word_count = {}
    for word in word_in_text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # the sorted nested list = sorting the dictionary by value
    sorted_word_count = sorted([value, key] for (key, value) in word_count.items())

    # find the top ten
    new_list = []
    for i in reversed(list(range(-10, 0))):
        new_list.append(sorted_word_count[i])

    # convert the nested list to dictionary form for printing purpose
    final_dic = {}
    for i in new_list:
        for _ in i:
            dic_key = i[1]
            final_dic[dic_key] = i[0]

    # print the word - frequency
    for key, value in final_dic.items():
        print(key, "-", value)


top_ten_words('moby_dick.txt')
# different result then mike
# function name?
# how to do unittest? any text file?
# how to sort a dictionary by value
# reverse the sorted()
