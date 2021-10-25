from shapes import *
from unittest import TestCase


class TestCircle(TestCase):

    def test_circle_with_negative_radius(self):
        with self.assertRaises(AttributeError):
            circle = Circle(-1.1)

    def test_circle_with_zero_radius(self):
        with self.assertRaises(AttributeError):
            circle = Circle(0)

    def test_circle_with_positive_radius(self):
        self.circle = Circle(89.3)

    def test_circle_perimeter(self):
        self.circle = Circle(2.3)
        self.assertEqual(round(self.circle.perimeter(), 3), 14.451)

    def test_circle_diameter(self):
        self.circle = Circle(2.3)
        self.assertEqual(round(self.circle.diameter(), 3), 4.6)

    def test_circle_square(self):
        self.circle = Circle(2.3)
        self.assertEqual(round(self.circle.area(), 3), 16.619)


class TestRectangle(TestCase):

    def test_rectangle_with_negative_sides(self):
        with self.assertRaises(AttributeError):
            rect = Rectangle(-1.1, 4.0)

        with self.assertRaises(AttributeError):
            rect = Rectangle(1.1, -4.0)

        with self.assertRaises(AttributeError):
            rect = Rectangle(-1.1, -4.0)

    def test_rectangle_with_zero_sides(self):
        with self.assertRaises(AttributeError):
            rect = Rectangle(0.0, 4.0)

        with self.assertRaises(AttributeError):
            rect = Rectangle(1.1, 0.0)

        with self.assertRaises(AttributeError):
            rect = Rectangle(0.0, 0.0)

    def test_rectangle_perimeter(self):
        rect = Rectangle(2.3, 1.2)
        self.assertEqual(round(rect.perimeter(), 3), 7.0)

    def test_rectangle_square(self):
        rect = Rectangle(2.3, 1.2)
        self.assertEqual(round(rect.area(), 3), 2.76)

    def test_rectangle_diagonal_length(self):
        rect = Rectangle(2.3, 1.2)
        self.assertEqual(round(rect.diagonal_length(), 3), 2.594)


class TestSquare(TestCase):

    def test_square_with_a_negative_side(self):
        with self.assertRaises(AttributeError):
            square = Square(-1.1)

    def test_square_with_one_zero_side(self):
        with self.assertRaises(AttributeError):
            square = Square(0.0)

    def test_square_perimeter(self):
        square = Square(1.1)
        self.assertAlmostEqual(square.perimeter(), 4.4, 3)

    def test_square_square(self):
        square = Square(1.1)
        self.assertAlmostEqual(square.area(), 1.21, 3)

    def test_square_diagonal_length(self):
        square = Square(1.1)
        self.assertAlmostEqual(square.diagonal_length(), 1.556, 3)


class TestRhombus(TestCase):

    def test_rhombus_with_a_negative_side(self):
        with self.assertRaises(AttributeError):
            rhombus = Rhombus(-1.1, pi / 3)

    def test_rhombus_with_a_negative_angle(self):
        with self.assertRaises(AttributeError):
            rhombus = Rhombus(1.1, -pi / 3)

    def test_rhombus_perimeter(self):
        rhombus = Rhombus(1.1, pi / 3)
        self.assertAlmostEqual(rhombus.perimeter(), 4.4, 3)

    def test_rhombus_square(self):
        rhombus = Rhombus(1.1, pi / 3)
        self.assertAlmostEqual(rhombus.area(), 1.048, 3)


class TestTriangle(TestCase):

    def test_triangle_with_negative_sides(self):
        with self.assertRaises(AttributeError):
            triangle = Triangle(-3.0, 4.0, 5.0)

        with self.assertRaises(AttributeError):
            triangle = Triangle(3.0, -4.0, 5.0)

        with self.assertRaises(AttributeError):
            triangle = Triangle(3.0, 4.0, -5.0)

    def test_triangle_with_zero_sides(self):
        with self.assertRaises(AttributeError):
            triangle = Triangle(0.0, 4.0, 5.0)

        with self.assertRaises(AttributeError):
            triangle = Triangle(3.0, 0.0, 5.0)

        with self.assertRaises(AttributeError):
            triangle = Triangle(3.0, 4.0, 0.0)

    def test_impossible_triangles(self):
        with self.assertRaises(AttributeError):
            triangle = Triangle(10.0, 4.0, 5.0)

        with self.assertRaises(AttributeError):
            triangle = Triangle(3.0, 9.0, 5.0)

        with self.assertRaises(AttributeError):
            triangle = Triangle(3.0, 4.0, 8.0)

    def test_triangle_perimeter(self):
        triangle = Triangle(3.0, 4.0, 5.0)
        self.assertAlmostEqual(triangle.perimeter(), 12.0, 3)

    def test_triangle_square_case_1(self):
        triangle = Triangle(3.0, 4.0, 5.0)
        self.assertAlmostEqual(triangle.area(), 6.0, 3)

    def test_triangle_square_case_2(self):
        triangle = Triangle(6.0, 8.0, 7.0)
        self.assertAlmostEqual(triangle.area(), 20.333, 3)


class TestSphere(TestCase):

    def test_sphere_with_negative_radius(self):
        with self.assertRaises(AttributeError):
            sphere = Sphere(-1.1)

    def test_sphere_with_zero_radius(self):
        with self.assertRaises(AttributeError):
            sphere = Sphere(0.0)

    def test_sphere_diameter(self):
        sphere = Sphere(1.1)
        self.assertAlmostEqual(sphere.diameter(), 2.2, 3)

    def test_sphere_square(self):
        sphere = Sphere(1.1)
        self.assertAlmostEqual(sphere.area(), 15.205, 3)

    def test_sphere_volume(self):
        sphere = Sphere(1.1)
        self.assertAlmostEqual(sphere.volume(), 5.575, 3)


class TestParallelepiped(TestCase):

    def test_parallelepiped_with_negative_sides(self):
        with self.assertRaises(AttributeError):
            parallelepiped = Parallelepiped(-3.0, 4.0, 5.0)

        with self.assertRaises(AttributeError):
            parallelepiped = Parallelepiped(3.0, -4.0, 5.0)

        with self.assertRaises(AttributeError):
            parallelepiped = Parallelepiped(3.0, 4.0, -5.0)

    def test_parallelepiped_square(self):
        parallelepiped = Parallelepiped(3.0, 4.0, 5.0)
        self.assertAlmostEqual(parallelepiped.area(), 94.0, 3)

    def test_parallelepiped_volume(self):
        parallelepiped = Parallelepiped(3.0, 4.0, 5.0)
        self.assertAlmostEqual(parallelepiped.volume(), 60.0, 3)


class TestPyramid(TestCase):

    def setUp(self):
        self.base = Triangle(3.0, 4.0, 5.0)

    def test_pyramid_with_negative_height(self):
        with self.assertRaises(AttributeError):
            pyramid = Pyramid(self.base, -1.0)

        self.base = Triangle(6.0, 4.0, 5.0)

    def test_pyramid_volume(self):
        pyramid = Pyramid(self.base, 6.0)
        self.assertAlmostEqual(pyramid.volume(), 12.0, 3)


class TestCone(TestCase):

    def test_cone_with_negative_args(self):
        with self.assertRaises(AttributeError):
            cone = Cone(r=-1.1, h=1.3)

        with self.assertRaises(AttributeError):
            cone = Cone(r=-1.1, h=1.3)

    def test_cone_square(self):
        cone = Cone(r=1.1, h=1.3)
        self.assertAlmostEqual(cone.area(), 9.686, 3)

    def test_cone_volume(self):
        cone = Cone(r=1.1, h=1.3)
        self.assertAlmostEqual(cone.volume(), 1.647, 3)


class TestCylinder(TestCase):

    def test_cylinder_with_negative_args(self):
        with self.assertRaises(AttributeError):
            cylinder = Cylinder(r=-1.1, h=1.3)

        with self.assertRaises(AttributeError):
            cylinder = Cylinder(r=-1.1, h=1.3)

    def test_cylinder_square(self):
        cylinder = Cylinder(r=1.1, h=1.3)
        self.assertAlmostEqual(cylinder.area(), 16.588, 3)

    def test_cylinder_volume(self):
        cylinder = Cylinder(r=1.1, h=1.3)
        self.assertAlmostEqual(cylinder.volume(), 4.942, 3)
