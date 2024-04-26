from datetime import datetime


class FileTypeError(TypeError):
    pass


class FileRecursionError(RecursionError):
    pass


class File:
    def __init__(self, name: str, date: str, text: str):
        if not all([isinstance(name, str), isinstance(date, str), isinstance(text, str)]):
            raise TypeError
        if not datetime.strptime(date, '%d-%m-%Y %H:%M'):
            raise ValueError
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
        if any([not isinstance(file, File), not isinstance(file, ZipFile)]):
            raise FileTypeError
        file.extract()
        a = self.zip_name
        while a is not None:
            if a == file:
                raise FileRecursionError
            a = a.zip_name
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


try:
    a = File(123, '01-01-1970 00:00', 'test')
except TypeError:
    print('TypeError raised')
try:
    a = File('test.txt', '32-01-1970 00:00', 'test')
except ValueError:
    print('ValueError raised')
try:
    a = ZipFile('a.zip', '01-01-1970 00:00')
    b = ZipFile('b.zip', '01-01-1970 00:00')
    c = ZipFile('c.zip', '01-01-1970 00:00')
    a <<= b
    b <<= c
    c <<= a
except FileRecursionError:
    print('FileRecursionError raised')