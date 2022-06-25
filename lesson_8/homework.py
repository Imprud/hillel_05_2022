from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("----\n|  |\n----\n")


class Circle(Shape):
    def draw(self):
        print("  --\n -  -\n  --\n")


class Triangle(Shape):
    def draw(self):
        print("  /\\\n /  \\\n/____\\\n")


def get_shape() -> Shape:
    options: list[Shape] = [Rectangle(), Circle(), Triangle()]
    return choice(options)


def main():
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
