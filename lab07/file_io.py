def getText(file_name):
    text = open(file_name, 'r').read()
    text = text.lower().strip()
    # replace punctuation mark with ' '(space)
    for character in ',.~!@#$%^&*()_+-={}[]|/<>:\'\";':
        text = text.replace(character, ' ')

    # get the individual words from the text
    word_in_text = text.split()
    # count the frequency of the text
    word_count = {}
    for word in word_in_text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count)

    # the sorted nested list = sorting the dictionary by value
    sorted_word_count = sorted([value, key] for (key, value) in word_count.items())
    print(sorted_word_count)

    # find the top ten
    new_list = sorted_word_count[-10:]
    print(new_list)

    # convert the nested list to dictionary form for printing purpose
    final_dic = {}
    for i in new_list:
        for x in i:
            dic_key = i[1]
            final_dic[dic_key] = i[0]
    print(final_dic)

    # print the word:frequency
    for key, value in final_dic.items():
        print(key, ": ", value)


getText('test_io.txt')
# how to do unittest? any text file?
# how to sort a dictionary by value
# reverse the sorted()

