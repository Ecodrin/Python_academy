class File:
    def __init__(self, name: str, date: str, text: str):
        self.name: str = name
        self.date: str = date
        self.text: str = text
        self.published: bool = False
        self.edited: bool = False
        self.zip_name = None

    def get_name(self) -> str:
        return self.name

    def get_creation_datetime(self) -> str:
        return self.date

    def get_content(self) -> str:
        return self.text

    def publish(self) -> None:
        self.published = True

    def is_published(self) -> bool:
        return self.published

    def edit(self, content) -> None:
        self.text = content
        self.edited = True
        self.published = False

    def is_edited(self) -> bool:
        return self.edited

    def __lt__(self, other) -> bool:
        return self in self.zip_name.zip

    def extract(self):
        if self.zip_name is not None:
            self.zip_name.zip.remove(self)
            self.zip_name = None

    def __str__(self) -> str:
        return f'[{self.name} ({self.date})]\n{self.text}\n'

    def __repr__(self) -> str:
        return f'File({self.name}, {self.date}, {repr(self.zip_name)})'


class ZipFile(File):
    def __init__(self, name: str, date: str) -> None:
        super().__init__(name, date, '')
        self.zip = []

    def __lt__(self, other):
        return other in self.zip

    def wrap(self, file) -> None:
        file.extract()
        self.zip.append(file)
        file.zip_name = self

    def get_files(self) -> list:
        return self.zip

    def __ilshift__(self, other):
        if other not in self.zip:
            self.wrap(other)
            return self

    def __repr__(self):
        return f'ZipFile({self.name}, {self.date})'


a = File('hello.txt', '01-06-2023 12:03', 'Hello, world!')
print(repr(a))
b = ZipFile('hello.zip', '02-06-2023 10:50')
b <<= a
c = File('hello2.txt', '02-06-2023 10:53', 'Привет, мир!')
b.wrap(c)
print(b.get_files())
a.extract()
print(b.get_files())
print(repr(b))
d = ZipFile('hello2.zip', '02-06-2023 11:07')
d <<= b
print(c < d, c > d, d < c, d > c)
d.wrap(c)
print(b.get_files(), d.get_files())
