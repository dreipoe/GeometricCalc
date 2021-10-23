import unittest

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
        self.assertEqual(round(self.circle.square(), 3), 16.619)


class TestRectangle(TestCase):

    def test_rectangle_with_one_negative_side(self):
        with self.assertRaises(AttributeError):
            rect = Rectangle(-1.1, 4.0)

    def test_rectangle_with_negative_sides(self):
        with self.assertRaises(AttributeError):
            rect = Rectangle(-1.1, -4.0)

    def test_rectangle_with_one_zero_side(self):
        with self.assertRaises(AttributeError):
            rect = Rectangle(0.0, 4.0)

    def test_rectangle_with_zero_sides(self):
        with self.assertRaises(AttributeError):
            rect = Rectangle(0.0, 0.0)

    def test_rectangle_perimeter(self):
        rect = Rectangle(2.3, 1.2)
        self.assertEqual(round(rect.perimeter(), 10), 7.0)

    def test_rectangle_square(self):
        rect = Rectangle(2.3, 1.2)
        self.assertEqual(round(rect.square(), 10), 2.76)

    def test_rectangle_diagonal_length(self):
        rect = Rectangle(2.3, 1.2)
        self.assertEqual(round(rect.diagonal_length(), 10), 2.76)


class TestSquare(TestCase):

    def test_square_with_a_negative_side(self):
        with self.assertRaises(AttributeError):
            square = Square(-1.1)

    def test_square_with_one_zero_side(self):
        with self.assertRaises(AttributeError):
            square = Square(0.0)

    def test_square_perimeter(self):
        square = Square(1.1)
        self.assertEqual(round(square.perimeter(), 10), 4.4)

    def test_square_square(self):
        square = Square(1.1)
        self.assertEqual(round(square.square(), 10), 1.21)

    def test_square_diagonal_length(self):
        square = Square(1.1)
        self.assertEqual(round(square.diagonal_length(), 10), 1.55563485)


class TestRhombus(TestCase):

    def test_rhombus_with_a_negative_side(self):
        with self.assertRaises(AttributeError):
            rhombus = Rhombus(-1.1, pi / 3)

    def test_rhombus_with_a_negative_angle(self):
        with self.assertRaises(AttributeError):
            rhombus = Rhombus(1.1, -pi / 3)
