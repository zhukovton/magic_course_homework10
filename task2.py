# Создайте класс User с полями username и password.
# Реализуйте собственные исключения:

# UsernameTooShortException — выбрасывается,
# если длина username меньше 5 символов.

# PasswordTooWeakException — выбрасывается,
# если пароль не соответствует заданным требованиям (например,
# меньше 8 символов или не содержит цифр).

# Создайте метод validate_user(), который проверяет
# корректность username и password и выбрасывает исключения
# при необходимости.
class UsernameTooShortException(Exception):
    def __str__(self):
        return f"username менее 5 символов"


class PasswordTooWeakException(Exception):
    def __str__(self):
        return f"password меньше 8 символов или не содержит цифр"


class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password

    def __repr__(self):
        return f"{self.__username} {self.__password}"

    def validate_user(self):
        expected_symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        if len(self.__password) < 8 and expected_symbols not in self.__password:
            raise PasswordTooWeakException
        if len(self.__username) < 5:
            raise UsernameTooShortException
        return f"Валидация прошла успешно"


if __name__ == "__main__":
    user = User("Alexx", "f43433ff")
    print(user.validate_user())


