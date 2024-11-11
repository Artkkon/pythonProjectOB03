# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

# 2. Реализуйте наследование, создав подклассы `Bird`,
# `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты
# и переопределите методы, если требуется (например, различный звук для `make_sound()`).

class Bird(Animal):
    def __init__(self, name, age, wing_length):
        super().__init__(name, age)
        self.wing_length = wing_length

    def make_sound(self):
        return "Tweet Tweet"

    def eat(self):
        return "I eat insects"

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Meow Meow"

    def eat(self):
        return "I eat grass"

class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        return "Hiss Hiss"

    def eat(self):
        return "I eat insects"

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

cow = Mammal("Cow", 5, "White")
crow = Bird("Crow", 50, 20)
snake = Reptile("Snake", 2, "Green")

animals = [cow, crow, snake]

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

animal_sound(animals)

# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о
# животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)



    def add_employee(self, employee):
        self.employees.append(employee)

# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class ZooKeeper:
    def feed_animal(self, animal):
        print(f"{animal.name} is fed")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"{animal.name} is healed")



