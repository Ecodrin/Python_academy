import pandas as pd


def update(in_journal: pd.DataFrame):
    new_journal = in_journal.copy()
    new_journal["average"] = (new_journal["maths"] + new_journal["physics"] + new_journal["computer science"]) / 3
    new_journal = new_journal.sort_values(["average", "name"], ascending=(False, True))
    return new_journal


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)