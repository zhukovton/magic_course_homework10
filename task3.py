# Для класса Triangle сделать контроль создания,
# значения должны быть положительны
# и треугольник должен существовать,
# иначе вызвать ошибку ValueError.
class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}"

    def validate_triangle(self):
        conditions = [self.a + self.b > self.c,
                      self.a + self.c > self.b,
                      self.b + self.c > self.a]

        valid_length = [self.a < 1,
                        self.b < 1,
                        self.c < 1]

        if any(valid_length):  # any() делает or между элементами списка
            raise ValueError
        if not all(conditions):  # all() делает and между элементами списка
            raise ValueError
        return f"Валидация"


tr = Triangle(3, 2, 2)
# print(tr)
print(tr.validate_triangle())
