from math import pi, sin


class Shape:

	def area(self):
		return float('NaN')


class FlatShape(Shape):
	pass


class Circle(FlatShape):

	def __init__(self, r: float):
		if r <= 0:
			raise AttributeError("Radius is not positive")

		self._r = r

	def perimeter(self) -> float:
		return 2 * pi * self._r

	def diameter(self) -> float:
		return 2 * self._r

	def area(self) -> float:
		return pi * self._r ** 2


class Rectangle(FlatShape):

	def __init__(self, a: float, b: float):
		if a <= 0 or b <= 0:
			raise AttributeError("One or mode sides aren't positive")

		self._a, self._b = a, b

	def perimeter(self) -> float:
		return 2 * (self._a + self._b)

	def diagonal_length(self) -> float:
		return (self._a ** 2 + self._b ** 2) ** 0.5

	def area(self) -> float:
		return self._a * self._b


class Square(Rectangle):

	def __init__(self, a: float):
		super().__init__(a, a)

	def perimeter(self) -> float:
		return 4 * self._a

	def diagonal_length(self) -> float:
		return (2 * self._a ** 2) ** 0.5

	def area(self) -> float:
		return self._a ** 2


class Rhombus(FlatShape):

	def __init__(self, a: float, alpha: float):
		if any((a <= 0, alpha <= 0)):
			raise AttributeError("Side or angle isn't positive")

		if alpha >= pi / 2:
			raise AttributeError("Angle is too big")

		self._a, self._alpha = a, alpha

	def perimeter(self) -> float:
		return 4 * self._a

	def area(self) -> float:
		return self._a ** 2 * sin(self._alpha)


class Triangle(FlatShape):

	@staticmethod
	def _check_triangle_sides(a: float, b: float, c: float):
		return all((a + b > c, a + c > b, b + c > a))

	def __init__(self, a: float, b: float, c: float):
		if not self._check_triangle_sides(a, b, c):
			raise AttributeError("Cannot build a triangle with such sides")

		if any((a <= 0, b <= 0, c <= 0)):
			raise AttributeError("One or mode sides aren't positive")

		self._a, self._b, self._c = a, b, c

	def perimeter(self) -> float:
		return self._a + self._b + self._c

	def area(self) -> float:
		# формула Герона
		p = self.perimeter() / 2
		return (p * (p - self._a) * (p - self._b) * (p - self._c)) ** 0.5


class VolumetricShape(Shape):

	def volume(self):
		return float('NaN')


class Sphere(VolumetricShape):

	def __init__(self, r: float):
		if r <= 0:
			raise AttributeError("Radius is not positive")

		self._r = r

	def area(self) -> float:
		return 4 * pi * (self._r ** 2)

	def diameter(self) -> float:
		return 2 * self._r

	def volume(self) -> float:
		return 4 * pi * (self._r ** 3) / 3


class Parallelepiped(VolumetricShape):

	def __init__(self, a: float, b: float, h: float):
		if any((a <= 0, b <= 0, h <= 0)):
			raise AttributeError("One or mode sides aren't positive")

		self._a, self._b, self._h = a, b, h

	def area(self) -> float:
		return 2 * (self._a * self._b + self._a * self._h + self._b * self._h)

	def volume(self) -> float:
		return self._a * self._b * self._h


class Pyramid(VolumetricShape):

	def __init__(self, base: FlatShape, h: float):
		if h <= 0:
			raise AttributeError("Height isn't positive")

		self._base, self._h = base, h

	def volume(self) -> float:
		return self._base.area() * self._h / 3


class Cone(VolumetricShape):

	def __init__(self, r: float, h: float):
		if any((r <= 0, h <= 0)):
			raise AttributeError("One or mode sides aren't positive")

		self._r, self._h = r, h

	def area(self) -> float:
		le = (self._r ** 2 + self._h ** 2) ** 0.5
		return pi * self._r * (le + self._r)

	def volume(self) -> float:
		return pi * self._r ** 2 * self._h / 3


class Cylinder(VolumetricShape):

	def __init__(self, r: float, h: float):
		if any((r <= 0, h <= 0)):
			raise AttributeError("One or mode sides aren't positive")

		self._r, self._h = r, h

	def area(self) -> float:
		return 2 * pi * self._r * (self._r + self._h)

	def volume(self) -> float:
		return pi * self._r ** 2 * self._h
