text = 'Мама мыла раму!'
print({i: text.lower().count(i) for i in sorted(text.lower()) if i.lower().isalpha()})
