class Profile:
    def __init__(self, title) -> None:
        self.title = title

    def info(self) -> str:
        return ''

    def describe(self) -> None:
        print(self.info())


class Vacancy(Profile):
    def __init__(self, title, pay) -> None:
        super().__init__(title)
        self.pay = pay

    def info(self):
        return f'Предлагаемая зарплата: {self.pay}'


class Resume(Profile):
    def __init__(self, title, length_of_service) -> None:
        super().__init__(title)
        self.length_of_service = length_of_service

    def info(self) -> str:
        return f'Стаж работы: {self.length_of_service}'
