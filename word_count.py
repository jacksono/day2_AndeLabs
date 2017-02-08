
def words(arg):
    '''Count word and number occurences
    Args:
        arg is a string containing words and numbers
    Returns:
        Returns a dictionaryof the word and number occurences

    '''
    output = {}
    word_list = arg.split()
    for word in word_list:
        if word.isdigit(): #to capture the numbers in the string
            output[int(word)] = word_list.count(word)
        else:
            output[word] = word_list.count(word)
    return output