При помощи ООП спроектировать и реализовать геометрический калькулятор для вычислений, производимых над фигурами.
Калькулятор должен поддерживать вычисления для плоских и объемных фигур. 

Плоские фигуры: круг, квадрат, прямоугольник, треугольник, трапеция, ромб.
Объемные фигуры: сфера, куб, параллелепипед, пирамида, цилиндр, конус.

Реализовать как минимум один общий метод вычисления для всех фигур и как минимум один специфичный для определенных фигур.
Например, площадь – общий метод для всех фигур, медиана – специфичный метод для ряда фигур.

Реализовать интерфейс программы для возможности взаимодействия пользователя с ней.
Интерфейс может быть консольным или графическим.

* (задание со звездочкой) Реализовать визуализацию фигур на плоскости и в пространстве.

1. При разработке программы придерживаться принципов SOLID.
2. Использовать уточнение типов (type hinting).
3. Для тестирования приложения разработать автотесты (unittest).
4. Для всех модулей, классов и методов написать документацию (reStructuredText).
5. При оформлении кода пользоваться стандартом PEP 8 (можно отформатировать код линтером).

SOLID:  
Single responsibility principle: Для каждого класса должно быть определено единственное назначение. Все ресурсы, необходимые для его осуществления, должны быть инкапсулированы в этот класс и подчинены только этой задаче.  
Open–closed principle: Программные сущности должны быть открыты для расширения, но закрыты для модификации.  
Liskov substitution principle: Производный класс должен быть взаимозаменяем с родительским классом. Экземпляры родительского класса должны быть заменимы на экземляры дочерних классов без изменения правильности выполнения программы.  
Interface segregation principle: много интерфейсов, специально предназначенных для клиентов, лучше, чем один интерфейс общего назначения.  
Dependency inversion principle: зависимость на абстракциях, а не на что-то конкретное  


