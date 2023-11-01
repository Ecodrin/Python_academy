import pandas as pd


def best(in_journal: pd.DataFrame):
    return in_journal[(in_journal["maths"] > 3) &
                      (in_journal["physics"] > 3) &
                      (in_journal["computer science"] > 3)]


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = best(journal)
print(journal)
print(filtered)
