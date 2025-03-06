"""Создайте класс Soda (газировка). Для инициализации
есть параметр, который определяет вкус газировки. При
инициализации этот параметр можно задавать, а можно и не
задавать. Реализовать метод строковой репрезентации,
который возвращает строку вроде «У вас газировка с
<клубничным> вкусом», если вкус задан. Если вкус не задан,
метод должен возвращать строку «У вас обычная газировка»."""



class GazWater:
    def print_tasty_water(self,tasty = "обычным"):
        self.tasty = tasty
        print(f"У вас газировка с {self.tasty} вкусом")


gaz_water = GazWater()
gaz_water.print_tasty_water("клубничным")


#  Задание 2
"""Напишите программу с классом Math. При
инициализации атрибутов нет. Реализовать методы addition,
subtraction, multiplication и division. При передаче в методы
двух числовых параметров нужно производить с
параметрами соответствующие действия и печатать ответ."""


class Math:
    def addition(self, a, b):
        c = a + b
        print(f"Результат сложения: {c}")

    def substraction(self, a, b):
        c = a - b
        print(f"Результат вычитания: {c}")

    def multiplication(self, a, b):
        c = a * b
        print(f"Результат умножения: {c}")

    def division(self, a, b):
        c = a / b
        print(f"Результат деления: {c}")


d = Math()
d.division(a = 8, b = 5)
d.addition(a = 8, b = 5)
d.substraction(a = 5, b = 8)
d.multiplication(a = 5, b = 5)


#  Задание 3
"""Программа с классом Car. При инициализации объекта
ему должны задаваться атрибуты color, type и year.
Реализовать пять методов. Запуск автомобиля – выводит
строку «Автомобиль заведён». Отключение автомобиля –
выводит строку «Автомобиль заглушен». Методы для
присвоения автомобилю года выпуска, типа и цвета."""

class Car:
    def __init__(self, type, color, year):
        self.type = type
        self.color = color
        self.year = year
        print(type, color, year)

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль остановлен")

    def type_car(self,type):
        self.type = type
        print(type)

    def color_car(self, color):
        self.color = color
        print(color)

    def year_car(self, year):
        self.year = year
        print(year)

a = Car("Audi", "красный", 1998)
a.start()
a.type_car("BMW")
print(a.type)
a.color_car("желтый")
a.stop()
print(a.color)
print(a.year)
a.year_car(2006)
print(a.year)
print(a.year, a.type, a.color)

