# Создайте класс ContactBook с методом add_contact().
# Реализуйте пользовательские исключения:

# DuplicateContactException — выбрасывается, если контакт
# с таким именем уже существует.

# InvalidPhoneNumberException — выбрасывается, если номер
# телефона не соответствует заданному формату
# (например, не содержит 10 цифр).

# P.s. Подумайте как хранить контакт. Я предлагаю вариант - в виде
# класса Contact
class InvalidPhoneNumberException(Exception):
    def __str__(self):
        return f"Телефон не содержит 10 цифр"


class DuplicateContactException(Exception):
    def __str__(self):
        return f"контакт с таким именем уже существует"


class ContactBook:
    def __init__(self):
        self.contact_book = []

    def add_contact(self, new_contact: "Contact"):
        if new_contact in self.contact_book:
            raise DuplicateContactException
        if len(new_contact.phone_number) < 10:
            raise InvalidPhoneNumberException
        self.contact_book.append(new_contact)
        return f"Контакт добавлен"

    def show_contact_book(self):
        return self.contact_book


class Contact:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return f"name: {self.name} phone_number: {self.phone_number}"


if __name__ == "__main__":
    contact = Contact("Alex", "89999999")
    contact1 = Contact("Vasiliy", "87777777777")
    contact2 = Contact("Alex", "89999999999")
    cb = ContactBook()

    print(cb.add_contact(contact))
    print(cb.add_contact(contact))
    print(cb.show_contact_book())
