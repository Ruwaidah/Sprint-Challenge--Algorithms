'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    print(word)
    count = 0

    index = word.find('th')
    print("index", index, "word", word)
    if index != -1:
        count = count + 1 + count_th(word[index+2:])
    return count


print(count_th("wefwefwfwthethethe"))
