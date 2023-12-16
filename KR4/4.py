def rindex(text):
    for i in sorted(set(text)):
        if i.isalpha():
            yield i, text.rindex(i)


text = "Мама мыла раму"
for letter, i in rindex(text):
    print(f"{letter}: {i}")