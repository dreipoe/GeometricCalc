from math import pi, sin


class Shape:
	"""Базовый класс, от которого наследуются все другие классы модуля Shapes"""
	def area(self) -> float:
		"""
		Метод, предназначенный для вычисления площади.
		:return: NaN
		"""
		return float('NaN')


class FlatShape(Shape):
	"""Класс, представляющие собой плоские фигуры"""
	pass


class Circle(FlatShape):
	"""Класс, представляющий собой круг."""
	def __init__(self, r: float):
		"""
		:param r: Радиус круга.
		:raises AttributeError:
		"""
		if r <= 0:
			raise AttributeError("Величина радиуса не положительна")

		self._r = r

	def perimeter(self) -> float:
		"""Периметр круга"""
		return 2 * pi * self._r

	def diameter(self) -> float:
		"""Диаметр круга"""
		return 2 * self._r

	def area(self) -> float:
		"""Площадь круга"""
		return pi * self._r ** 2


class Rectangle(FlatShape):
	"""Класс, представляющий собой прямоугольник"""
	def __init__(self, a: float, b: float):
		"""
		Длина и ширина прямоугольника должны быть положительными.

		:param a: Длина
		:param b: Ширина
		:raises AttributeError:
		"""
		if a <= 0 or b <= 0:
			raise AttributeError("Величина длины или ширины не положительна")

		self._a, self._b = a, b

	def perimeter(self) -> float:
		"""Периметр прямоугольника"""
		return 2 * (self._a + self._b)

	def diagonal_length(self) -> float:
		"""Длина диагонали прямоугольника"""
		return (self._a ** 2 + self._b ** 2) ** 0.5

	def area(self) -> float:
		"""Площадь прямоугольника"""
		return self._a * self._b


class Square(FlatShape):
	"""Класс, представляющий собой квадрат."""
	def __init__(self, a: float):
		"""
		:param a: Длина стороны квадрата
		:raises AttributeError:
		"""
		if a <= 0:
			raise AttributeError("Величина стороны не положительна")

		self._a = a

	def perimeter(self) -> float:
		"""Периметр квадрата"""
		return 4 * self._a

	def diagonal_length(self) -> float:
		"""Длина диагонали квадрата"""
		return (2 * self._a ** 2) ** 0.5

	def area(self) -> float:
		"""Площадь квадрата"""
		return self._a ** 2


class Rhombus(FlatShape):
	"""Класс, представляющий собой ромб"""
	def __init__(self, a: float, alpha: float):
		"""
		:param a: Длина стороны ромба
		:param alpha: Величина одного из углов ромба в радианах
		:raises AttributeError:
		"""
		if any((a <= 0, alpha <= 0)):
			raise AttributeError("Величина стороны или угла не положительна")

		if alpha >= 90:
			raise AttributeError("Угол больше 90 градусов")

		self._a, self._alpha = a, alpha * pi / 180

	def perimeter(self) -> float:
		"""Периметр ромба"""
		return 4 * self._a

	def area(self) -> float:
		"""Площадь ромба"""
		return self._a ** 2 * sin(self._alpha)


class Triangle(FlatShape):
	"""Класс, представляющий собой треугольник"""
	@staticmethod
	def _check_triangle_sides(a: float, b: float, c: float):
		"""
		Проверяет, возможно ли построить треугольник с заданными углами. Треугольник возможно построить, если каждая её
		сторона меньше, чем сумма длин двух других сторон
		"""
		return all((a + b > c, a + c > b, b + c > a))

	def __init__(self, a: float, b: float, c: float):
		"""
		:param a: Сторона a
		:param b: Сторона b
		:param c: Сторона c
		:raises AttributeError:
		"""
		if not self._check_triangle_sides(a, b, c):
			raise AttributeError("Невозможно собрать треугольник с такими сторонами")

		if any((a <= 0, b <= 0, c <= 0)):
			raise AttributeError("Величина одной или более сторон не положительна")

		self._a, self._b, self._c = a, b, c

	def perimeter(self) -> float:
		"""Периметр треугольника"""
		return self._a + self._b + self._c

	def area(self) -> float:
		"""Площадь треугольника, вычисляемая по формуле Герона"""
		p = self.perimeter() / 2
		return (p * (p - self._a) * (p - self._b) * (p - self._c)) ** 0.5


class VolumetricShape(Shape):
	"""Базовый класс для объёмных фигур. Включает в себя метод `volume()`, вычисляющий объём"""
	def volume(self):
		"""
		Метод, предназначенный для вычисления объёма.
		:return: NaN
		"""
		return float('NaN')


class Sphere(VolumetricShape):
	"""Класс, представляющий собой сферу"""
	def __init__(self, r: float):
		"""
		:param r: Радиус сферы
		:raises AttributeError:
		"""
		if r <= 0:
			raise AttributeError("Величина радиуса не положительна")

		self._r = r

	def area(self) -> float:
		"""Площадь поверхности сферы"""
		return 4 * pi * (self._r ** 2)

	def diameter(self) -> float:
		"""Диаметр сферы"""
		return 2 * self._r

	def volume(self) -> float:
		"""Объём сферы"""
		return 4 * pi * (self._r ** 3) / 3


class Parallelepiped(VolumetricShape):
	"""Класс, представляющий собой параллелепипед"""
	def __init__(self, a: float, b: float, h: float):
		"""
		:param a: Длина
		:param b: Ширина
		:param h: Высота
		:raises AttributeError:
		"""
		if any((a <= 0, b <= 0, h <= 0)):
			raise AttributeError("Величина длины, ширины или высоты не положительна")

		self._a, self._b, self._h = a, b, h

	def area(self) -> float:
		"""Площадь поверхности параллелепипеда"""
		return 2 * (self._a * self._b + self._a * self._h + self._b * self._h)

	def volume(self) -> float:
		"""Объём параллелепипеда"""
		return self._a * self._b * self._h


class Pyramid(VolumetricShape):
	"""Класс, представляющий собой пирамиду"""
	def __init__(self, base: FlatShape, h: float):
		"""
		:param base: Фигура, служащая основанием пирамиды
		:param h: Высота пирамиды
		:raises AttributeError:
		"""
		if h <= 0:
			raise AttributeError("Величина высоты не положительна")

		self._base, self._h = base, h

	def volume(self) -> float:
		"""Объём пирамиды"""
		return self._base.area() * self._h / 3


class Cone(Pyramid):
	"""Класс, представляющий собой конус - пирамиду с основанием в виде круга"""
	def __init__(self, r: float, h: float):
		"""
		:param r: Радиус основания
		:param h: Высота конуса
		:raises AttributeError:
		"""
		if h <= 0:
			raise AttributeError("Величина высоты не положительна")

		super().__init__(Circle(r), h)
		self._r = r

	def area(self) -> float:
		"""Полная площадь поверхности конуса"""
		le = (self._r ** 2 + self._h ** 2) ** 0.5
		return pi * self._r * (le + self._r)


class Cylinder(VolumetricShape):
	"""Класс, представляющий собой цилиндр"""
	def __init__(self, r: float, h: float):
		if any((r <= 0, h <= 0)):
			raise AttributeError("Величина радиуса или высоты цилиндра не положительна")

		self._r, self._h = r, h

	def area(self) -> float:
		"""Площадь цилиндра"""
		return 2 * pi * self._r * (self._r + self._h)

	def volume(self) -> float:
		"""Объём цилиндра"""
		return pi * self._r ** 2 * self._h
