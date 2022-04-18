from __future__ import annotations


class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def send_message(self, user: User, message: str) -> None:
        pass

    def post(self, message: str) -> None:
        pass

    def info(self) -> str:
        return ''

    def describe(self) -> None:
        print(f'{self.name} {self.info()}')
        

class Person(User):
    def __init__(self, name: str, date: str) -> None:
        self.name = name
        self.date_of_birth = date

    def info(self) -> str:
        return f'Дата рождения: {self.date_of_birth}'

    def subscribe(self, user: User) -> None:
        pass


class Community(User):
    def __init__(self, name: str, short_description: str) -> None:
        self.name = name
        self.short_description = short_description

    def info(self) -> str:
        return f'Описание: {self.short_description}'

