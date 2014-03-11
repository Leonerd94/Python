# ex 2

def find_longest_word(words):
    max = words[0]
    for x in words:
        if(len(x) > max):
            max = len(x)
    return max

def filter_long_words(list, n):
    i = 0
    words = []
    for x in list:
        if(len(x) > n):
            words.append(x)
            i = i+1
    return words



#test method

print 'Test find_longest_word'

print find_longest_word(['ciao', 'hey'])

print 'Test filter_long_words'

print filter_long_words(['ciao', 'hey'], 3)