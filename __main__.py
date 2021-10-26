from shapes import *

nan = float('NaN')


def try_parse_float(s: str) -> float:
    try:
        return float(s)
    except ValueError:
        return nan


def mass_float_input(msgs: tuple):
    res = []
    for msg in msgs:
        while True:
            add = input(msg)
            if add == 'q':
                return None
            add = try_parse_float(add)
            if add is not nan:
                res.append(add)
                break
            else:
                print("Необходимо ввести число")
    return res


def circle_menu():
    while True:
        r = mass_float_input(('Введите радиус круга (q - выход): ',))
        if r is None:
            break
        try:
            circle = Circle(r[0])
            print(f"Периметр круга: {round(circle.perimeter(), 8)}")
            print(f"Диаметр круга: {round(circle.diameter(), 8)}")
            print(f"Площадь круга: {round(circle.area(), 8)}")
        except AttributeError as e:
            print(e.name)


def rectangle_menu():
    while True:
        args = mass_float_input((
            'Введите длину прямоугольника (q - выход): ',
            'Введите ширину прямоугольника (q - выход): '
        ))
        if args is None:
            break
        try:
            rectangle = Rectangle(args[0], args[1])
            print(f"Периметр прямоугольника: {round(rectangle.perimeter(), 8)}")
            print(f"Длина диагонали прямоугольника: {round(rectangle.diagonal_length(), 8)}")
            print(f"Площадь прямоугольника: {round(rectangle.area(), 8)}")
        except AttributeError as e:
            print(e.name)


def square_menu():
    while True:
        args = mass_float_input(('Введите длину стороны квадрата (q - выход): ',))
        if args is None:
            break
        try:
            square = Square(args[0])
            print(f"Периметр квадрата: {round(square.perimeter(), 8)}")
            print(f"Длина диагонали квадрата: {round(square.diagonal_length(), 8)}")
            print(f"Площадь квадрата: {round(square.area(), 8)}")
        except AttributeError as e:
            print(e.name)


def rhombus_menu():
    while True:
        args = mass_float_input((
            'Введите длину стороны ромба (q - выход): ',
            'Введите величину одного из углов ромба в градусах: '
        ))
        if args is None:
            break
        try:
            rhombus = Rhombus(args[0], args[1])
            print(f"Периметр ромба: {round(rhombus.perimeter(), 8)}")
            print(f"Площадь ромба: {round(rhombus.area(), 8)}")
        except AttributeError as e:
            print(e.name)


def triangle_menu():
    while True:
        args = mass_float_input((
            'Введите длину первой стороны треугольника: ',
            'Введите длину второй стороны треугольника: ',
            'Введите длину третьей стороны треугольника: '
        ))
        if args is None:
            break
        try:
            triangle = Triangle(args[0], args[1], args[2])
            print(f"Периметр треугольника: {round(triangle.perimeter(), 8)}")
            print(f"Площадь треугольника: {round(triangle.area(), 8)}")
        except AttributeError as e:
            print(e.name)


def flat_shapes_menu():
    key = ''
    while key != '0':
        print('1. Круг')
        print('2. Прямоугольник')
        print('3. Квадрат')
        print('4. Ромб')
        print('5. Треугольник')
        print('0. Назад')
        key = input('> ')

        if key == '1':
            circle_menu()
        elif key == '2':
            rectangle_menu()
        elif key == '3':
            square_menu()
        elif key == '4':
            rhombus_menu()
        elif key == '5':
            triangle_menu()
        elif key == '0':
            break
        else:
            print('Нет такого пункта меню')


def sphere_menu():
    while True:
        r = mass_float_input(('Введите радиус сферы: ',))
        if r is None:
            break
        try:
            sphere = Sphere(r[0])
            print(f"Диаметр сферы: {round(sphere.diameter(), 8)}")
            print(f"Площадь поверхности сферы: {round(sphere.area(), 8)}")
            print(f"Объём сферы: {round(sphere.area(), 8)}")
        except AttributeError as e:
            print(e.name)


def parallelepiped_menu():
    while True:
        args = mass_float_input((
            'Введите длину параллелепипеда: ',
            'Введите ширину параллелепипеда: ',
            'Введите высоту параллелепипеда: ',
        ))
        if args is None:
            break
        try:
            parallelepiped = Parallelepiped(args[0], args[1], args[2])
            print(f"Площадь поверхности параллелепипеда: {round(parallelepiped.area(), 8)}")
            print(f"Объём параллелепипеда: {round(parallelepiped.area(), 8)}")
        except AttributeError as e:
            print(e.name)


def cone_menu():
    while True:
        args = mass_float_input((
            'Введите радиус основания конуса: ',
            'Введите высоту конуса: ',
        ))
        if args is None:
            break
        try:
            cone = Cone(args[0], args[1])
            print(f"Площадь поверхности параллелепипеда: {round(cone.area(), 8)}")
            print(f"Объём параллелепипеда: {round(cone.area(), 8)}")
        except AttributeError as e:
            print(e.name)


def cylinder_menu():
    while True:
        args = mass_float_input((
            'Введите радиус цилиндра: ',
            'Введите высоту цилиндра: ',
        ))
        if args is None:
            break
        try:
            cone = Cone(args[0], args[1])
            print(f"Площадь поверхности цилиндра: {round(cone.area(), 8)}")
            print(f"Объём цилиндра: {round(cone.area(), 8)}")
        except AttributeError as e:
            print(e.name)


def volumetric_shapes_menu():
    key = ''
    while key != '0':
        print('1. Сфера')
        print('2. Параллелепипед')
        print('4. Конус')
        print('5. Цилиндр')
        print('0. Назад')
        key = input('> ')

        if key == '1':
            sphere_menu()
        elif key == '2':
            parallelepiped_menu()
        elif key == '4':
            cone_menu()
        elif key == '5':
            cylinder_menu()
        elif key == '0':
            break
        else:
            print('Нет такого пункта меню')


if __name__ == "__main__":
    print('Добро пожаловать в программу GeometricCalc!')
    print('© Dreipoe & Co. 2021')

    key = ''
    while key != '0':
        print('1. Плоские фигуры')
        print('2. Объёмные фигуры')
        print('0. Выход')
        key = input('> ')

        if key == '1':
            flat_shapes_menu()
        elif key == '2':
            volumetric_shapes_menu()
        elif key == '0':
            break
        else:
            print('Нет такого пункта меню')
