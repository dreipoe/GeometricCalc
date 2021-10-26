from shapes import *
from unittest import TestCase


class TestCircle(TestCase):
    """Набор тестов для круга"""
    def test_circle_with_negative_radius(self):
        """Тест с отрицательным радиусом"""
        with self.assertRaises(AttributeError):
            Circle(-1.1)

    def test_circle_with_zero_radius(self):
        """Тест с нулевым радиусом"""
        with self.assertRaises(AttributeError):
            Circle(0.0)

    def test_circle_perimeter(self):
        """Тест на вычисление периметра круга"""
        circle = Circle(2.3)
        self.assertEqual(round(circle.perimeter(), 3), 14.451)

    def test_circle_diameter(self):
        """Тест на вычисление диаметра круга"""
        circle = Circle(2.3)
        self.assertEqual(round(circle.diameter(), 3), 4.6)

    def test_circle_area(self):
        """Тест на вычисление площадь круга"""
        circle = Circle(2.3)
        self.assertEqual(round(circle.area(), 3), 16.619)


class TestRectangle(TestCase):
    """Набор тестов для прямоугольника"""
    def test_rectangle_with_negative_sides(self):
        """Тест с отрицательными сторонами"""
        with self.assertRaises(AttributeError):
            Rectangle(-1.1, 4.0)

        with self.assertRaises(AttributeError):
            Rectangle(1.1, -4.0)

        with self.assertRaises(AttributeError):
            Rectangle(-1.1, -4.0)

    def test_rectangle_with_zero_sides(self):
        """Тест с нулевыми сторонами"""
        with self.assertRaises(AttributeError):
            Rectangle(0.0, 4.0)

        with self.assertRaises(AttributeError):
            Rectangle(1.1, 0.0)

        with self.assertRaises(AttributeError):
            Rectangle(0.0, 0.0)

    def test_rectangle_perimeter(self):
        """Тест на вычисление периметра прямоугольника"""
        rect = Rectangle(2.3, 1.2)
        self.assertEqual(round(rect.perimeter(), 3), 7.0)

    def test_rectangle_area(self):
        """Тест на вычисление площади прямоугольника"""
        rect = Rectangle(2.3, 1.2)
        self.assertEqual(round(rect.area(), 3), 2.76)

    def test_rectangle_diagonal_length(self):
        """Тест на вычисление диагонали прямоугольника"""
        rect = Rectangle(2.3, 1.2)
        self.assertEqual(round(rect.diagonal_length(), 3), 2.594)


class TestSquare(TestCase):
    """Набор тестов для квадрата"""
    def test_square_with_a_negative_side(self):
        """Тест с отрицательными сторонами"""
        with self.assertRaises(AttributeError):
            Square(-1.1)

    def test_square_with_one_zero_side(self):
        """Тест с нулевыми сторонами"""
        with self.assertRaises(AttributeError):
            Square(0.0)

    def test_square_perimeter(self):
        """Тест на вычисление периметра квадрата"""
        square = Square(1.1)
        self.assertAlmostEqual(square.perimeter(), 4.4, 3)

    def test_square_area(self):
        """Тест на вычисление площади квадрата"""
        square = Square(1.1)
        self.assertAlmostEqual(square.area(), 1.21, 3)

    def test_square_diagonal_length(self):
        """Тест на вычисление диагонали квадрата"""
        square = Square(1.1)
        self.assertAlmostEqual(square.diagonal_length(), 1.556, 3)


class TestRhombus(TestCase):
    """Набор тестов для ромба"""
    def test_rhombus_with_a_negative_side(self):
        """Тест с отрицательной стороной"""
        with self.assertRaises(AttributeError):
            Rhombus(-1.1, 60)

    def test_rhombus_with_a_negative_angle(self):
        """Тест с отрицательным углом"""
        with self.assertRaises(AttributeError):
            Rhombus(1.1, -60)

    def test_rhombus_perimeter(self):
        """Тест на вычисление периметра ромба"""
        rhombus = Rhombus(1.1, 60)
        self.assertAlmostEqual(rhombus.perimeter(), 4.4, 3)

    def test_rhombus_area(self):
        """Тест на вычисление площади ромба"""
        rhombus = Rhombus(1.1, 60)
        self.assertAlmostEqual(rhombus.area(), 1.048, 3)


class TestTriangle(TestCase):
    """Набор тестов для треугольника"""
    def test_triangle_with_negative_sides(self):
        """Тест с отрицательными сторонами"""
        with self.assertRaises(AttributeError):
            Triangle(-3.0, 4.0, 5.0)

        with self.assertRaises(AttributeError):
            Triangle(3.0, -4.0, 5.0)

        with self.assertRaises(AttributeError):
            Triangle(3.0, 4.0, -5.0)

    def test_triangle_with_zero_sides(self):
        """Тест с нулевыми сторонами"""
        with self.assertRaises(AttributeError):
            Triangle(0.0, 4.0, 5.0)

        with self.assertRaises(AttributeError):
            Triangle(3.0, 0.0, 5.0)

        with self.assertRaises(AttributeError):
            Triangle(3.0, 4.0, 0.0)

    def test_impossible_triangles(self):
        """Тест со сторонами, из которых нельзя построить треугольник"""
        with self.assertRaises(AttributeError):
            Triangle(10.0, 4.0, 5.0)

        with self.assertRaises(AttributeError):
            Triangle(3.0, 9.0, 5.0)

        with self.assertRaises(AttributeError):
            Triangle(3.0, 4.0, 8.0)

    def test_triangle_perimeter(self):
        """Тест на вычисление периметра треугольника"""
        triangle = Triangle(3.0, 4.0, 5.0)
        self.assertAlmostEqual(triangle.perimeter(), 12.0, 3)

    def test_triangle_area_case_1(self):
        """Тест на вычисление площади прямоугольного треугольника"""
        triangle = Triangle(3.0, 4.0, 5.0)
        self.assertAlmostEqual(triangle.area(), 6.0, 3)

    def test_triangle_area_case_2(self):
        """Тест на вычисление площади произвольного треугольника"""
        triangle = Triangle(6.0, 8.0, 7.0)
        self.assertAlmostEqual(triangle.area(), 20.333, 3)


class TestSphere(TestCase):
    """Набор тестов для сферы"""
    def test_sphere_with_negative_radius(self):
        """Тест с отрицательным радиусом"""
        with self.assertRaises(AttributeError):
            Sphere(-1.1)

    def test_sphere_with_zero_radius(self):
        """Тест с нулевым радиусом"""
        with self.assertRaises(AttributeError):
            Sphere(0.0)

    def test_sphere_diameter(self):
        """Тест на вычисление диаметра сферы"""
        sphere = Sphere(1.1)
        self.assertAlmostEqual(sphere.diameter(), 2.2, 3)

    def test_sphere_area(self):
        """Тест на вычисление площади поверхности сферы"""
        sphere = Sphere(1.1)
        self.assertAlmostEqual(sphere.area(), 15.205, 3)

    def test_sphere_volume(self):
        """Тест на вычисление объёма сферы"""
        sphere = Sphere(1.1)
        self.assertAlmostEqual(sphere.volume(), 5.575, 3)


class TestParallelepiped(TestCase):
    """Набор тестов для параллелепипеда"""
    def test_parallelepiped_with_negative_sides(self):
        """Тест с отрицательными параметрами"""
        with self.assertRaises(AttributeError):
            Parallelepiped(-3.0, 4.0, 5.0)

        with self.assertRaises(AttributeError):
            Parallelepiped(3.0, -4.0, 5.0)

        with self.assertRaises(AttributeError):
            Parallelepiped(3.0, 4.0, -5.0)

    def test_parallelepiped_with_zero_sides(self):
        """Тест с нулевыми параметрами"""
        with self.assertRaises(AttributeError):
            Parallelepiped(0.0, 4.0, 5.0)

        with self.assertRaises(AttributeError):
            Parallelepiped(3.0, 0.0, 5.0)

        with self.assertRaises(AttributeError):
            Parallelepiped(3.0, 4.0, 0.0)

    def test_parallelepiped_area(self):
        """Тест на вычисление площади поверхности параллелепипеда"""
        parallelepiped = Parallelepiped(3.0, 4.0, 5.0)
        self.assertAlmostEqual(parallelepiped.area(), 94.0, 3)

    def test_parallelepiped_volume(self):
        """Тест на вычисление объёма параллелепипеда"""
        parallelepiped = Parallelepiped(3.0, 4.0, 5.0)
        self.assertAlmostEqual(parallelepiped.volume(), 60.0, 3)


class TestPyramid(TestCase):
    """Набор тестов для пирамиды"""
    def setUp(self):
        self.base = Triangle(3.0, 4.0, 5.0)

    def test_pyramid_with_negative_height(self):
        """Тест с отрицательной высотой"""
        with self.assertRaises(AttributeError):
            Pyramid(self.base, -1.0)

    def test_pyramid_with_zero_height(self):
        """Тест с нулевой высотой"""
        with self.assertRaises(AttributeError):
            Pyramid(self.base, 0.0)

    def test_pyramid_volume(self):
        """Тест на вычисление объёма пирамиды"""
        pyramid = Pyramid(self.base, 6.0)
        self.assertAlmostEqual(pyramid.volume(), 12.0, 3)


class TestCone(TestCase):
    """Набор тестов для конуса"""
    def test_cone_with_negative_args(self):
        """Тест с отрицательными параметрами"""
        with self.assertRaises(AttributeError):
            Cone(r=-1.1, h=1.3)

        with self.assertRaises(AttributeError):
            Cone(r=1.1, h=-1.3)

    def test_cone_with_zero_args(self):
        """Тест с нулевыми параметрами"""
        with self.assertRaises(AttributeError):
            Cone(r=0.0, h=1.3)

        with self.assertRaises(AttributeError):
            Cone(r=-1.1, h=0.0)

    def test_cone_area(self):
        """Тест на вычисление полной площади конуса"""
        cone = Cone(r=1.1, h=1.3)
        self.assertAlmostEqual(cone.area(), 9.686, 3)

    def test_cone_volume(self):
        """Тест на вычисление полной площади конуса"""
        cone = Cone(r=1.1, h=1.3)
        self.assertAlmostEqual(cone.volume(), 1.647, 3)


class TestCylinder(TestCase):
    """Набор тестов для цилиндра"""
    def test_cylinder_with_negative_args(self):
        """Тест с отрицательными параметрами"""
        with self.assertRaises(AttributeError):
            Cylinder(r=-1.1, h=1.3)

        with self.assertRaises(AttributeError):
            Cylinder(r=1.1, h=-1.3)

    def test_cylinder_with_zero_args(self):
        """Тест с нулевыми параметрами"""
        with self.assertRaises(AttributeError):
            Cylinder(r=0.0, h=1.3)

        with self.assertRaises(AttributeError):
            Cylinder(r=1.1, h=0.0)

    def test_cylinder_area(self):
        """Тест на вычисление полной площади цилиндра"""
        cylinder = Cylinder(r=1.1, h=1.3)
        self.assertAlmostEqual(cylinder.area(), 16.588, 3)

    def test_cylinder_volume(self):
        """Тест на вычисление объёма цилиндра"""
        cylinder = Cylinder(r=1.1, h=1.3)
        self.assertAlmostEqual(cylinder.volume(), 4.942, 3)
