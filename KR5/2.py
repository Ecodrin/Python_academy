class File:
    def __init__(self, name: str, date: str, text: str):
        self.name: str = name
        self.date: str = date
        self.text: str = text
        self.published: bool = False
        self.edited: bool = False

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

    def __str__(self) -> str:
        return f'[{self.name} ({self.date})]\n{self.text}'
