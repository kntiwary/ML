
def get_index(text):
    if text:
        yield 0
    for index, letter in enumerate(text, 1):
        if letter == ' ':
            yield index


def index_words(text):
    return [i for i in get_index(text)]


print(index_words("Solved it finally "))
