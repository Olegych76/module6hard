from math import pi, sqrt


class Figure:
    sides_count = 0
    filled = False

    def __init__(self, __color, __sides):
        self.__color = __color
        self.__sides = __sides

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        r = self.__color[0]
        g = self.__color[1]
        b = self.__color[2]
        return [r, g, b]

    def __is_valid_sides(self, *sides):
        for side in sides:
            if side <= 0:
                return False
        if len(sides) == len(self.get_sides()):
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        # Вычисляем периметр фигуры сложением всех сторон
        p = 0
        for side in self.__sides:
            p += side
        return p


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        if len(side) != 1:
            side = [1]
        super().__init__(color, side)
        # Вычисляем радиус круга по единственной стороне
        self.__radius = side[0] / (2 * pi)

    def get_radius(self):
        # Вычисляем радиус круга
        return round(self.__radius, 2)

    def get_square(self):
        # Вычисляем площадь круга
        return round(self.get_radius() ** 2 * pi, 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        sides = sides if len(sides) == 3 else [1] * 3
        super().__init__(color, sides)

    def get_square(self):
        # Вычисляем площадь треугольника
        a, b, c = self.get_sides()
        # Вычисляем полу-периметр
        p = (a + b + c) / 2
        # Вычисляем площадь треугольника по формуле Герона
        area = sqrt(p * (p - a) * (p - b) * (p - c))
        return area


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *side):
        if len(side) != 1:
            side = [1]
        super().__init__(color, list(side) * 12)  # Создаем список из 12 одинаковых сторон
        self.side_length = side[0]

    def get_volume(self):
        # Вычисляем объем куба
        return self.side_length ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
#
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# Проверка объёма (куба):
print(cube1.get_volume())
