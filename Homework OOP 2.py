"""ПчёлоСлон
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
● trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● eat(meal, value) – может принимать в meal только ”nectar”
или “grass”. Если съедает нектар, то value вычитается из
части слона, пчеле добавляется. Иначе – наоборот. Не
может увеличиваться больше 100 и уменьшаться меньше 0."""
from itertools import product

# class BeeElephant:
#     def __init__(self, bee, elephant):
#         self.bee = bee
#         self.elephant = elephant
#
#     def fly(self):
#         if self.bee >= self.elephant:
#             return True
#         return False
#
#     def trumpet(self):
#         if self.bee <= self.elephant:
#             return 'tu-tu-doo-doo!'
#         return 'wzzzzz'
#
#     def eat(self, meal, value):
#         if meal == 'nectar':
#             self.bee += value
#             self.elephant -= value
#         elif meal == 'grass':
#             self.bee -= value
#             self.elephant += value
#         if self.elephant > 100:
#             self.elephant = 100
#         elif self.elephant < 0:
#             self.elephant = 0
#         if self.bee > 100:
#             self.bee = 100
#         elif self.bee < 0:
#             self.bee = 0
#
#     def get_parts(self):
#         return (self.bee, self.elephant)


"""Класс «Автобус». Класс содержит свойства:
● скорость
● максимальное количество посадочных мест
● максимальная скорость
● список фамилий пассажиров
● флаг наличия свободных мест
● словарь мест в автобусе
Методы:
● посадка и высадка одного или нескольких пассажиров
● увеличение и уменьшение скорости на заданное значение
● операции in, += и -= (посадка и высадка пассажира по
фамилии)"""

# class Bus:
#     def __init__(self, speed, number_of_seats, max_speed, list_of_surnames=[], available_seats=0, list_of_seats=[]):
#         self.speed = speed
#         self.number_of_seats = number_of_seats
#         self.max_speed = max_speed
#         self.list_of_surnames = list_of_surnames
#         self.available_seats = available_seats
#         self.list_of_seats = list_of_seats
#
#     def get_speed(self):
#         return self.speed
#
#     def get_number_of_seats(self):
#         return self.number_of_seats
#
#     def get_max_speed(self):
#         return self.max_speed
#
#     def get_list_of_surnames(self):
#         return self.list_of_surnames
#
#     def get_available_seats(self):
#         return self.available_seats
#
#     def get_list_of_seats(self):
#         return self.list_of_seats
#
#     def board_passenger(self):
#         if self.available_seats < self.number_of_seats:
#             self.available_seats += 1
#             self.list_of_seats.append(self.available_seats)
#             return self.list_of_seats
#         else:
#             return None
#
#     def leave_passenger(self):
#         if self.available_seats > 0:
#             self.available_seats -= 1
#             self.list_of_seats.pop()
#             return self.list_of_seats
#         else:
#             return None
#
#     def set_speed(self, value):
#         if value <= self.max_speed:
#             self.speed = value
#             return self.speed
#         else:
#             return None
#
#     def increase_speed(self, value):
#         if self.speed + value <= self.max_speed:
#             self.speed += value
#             return self.speed
#         else:
#             return None
#
#     def decrease_speed(self, value):
#         if self.speed - value >= 0:
#             self.speed -= value
#             return self.speed
#         else:
#             return None
#
#
# bus = Bus(60, 20, 90)
# print(bus.get_speed())
# print(bus.get_number_of_seats())
# print(bus.get_max_speed())
# print(bus.get_list_of_surnames())
# print(bus.get_available_seats())
# print(bus.board_passenger())
# print(bus.leave_passenger())
# print(bus.get_list_of_seats())

""" Класс «Товар» содержит следующие закрытые поля:
● название товара
● название магазина, в котором подаётся товар
● стоимость товара в рублях """


from dataclasses import dataclass


@dataclass
class Product:
    name_product: str
    name_magazine: str
    cost: float


print(Product("Кроссовки", "спортмастер", 856))





