def add_word(word):
    global s
    s.append(word)


def get_work():

    return f"{', '.join(s)}. ({len(s)})"


s = []
add_word("мама")
add_word("мыла")
print(get_work())
add_word("раму")
print(get_work())