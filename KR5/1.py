


class File:
    def __init__(self, name: str, date: str, text: str):
        self.name: str = name
        self.date: str = date
        self.text: str = text

    def get_name(self) -> str:
        return self.name

    def get_creation_datetime(self) -> str:
        return self.date

    def get_content(self) -> str:
        return self.text


def main():
    pass


if __name__ == '__main__':
    main()
