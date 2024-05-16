from __future__ import annotations

from dataclasses import dataclass
from typing import (
    Generic,
    NamedTuple,
    TypeVar,
)


@dataclass
class Animal:
    name: str = "dog"


@dataclass
class Person:
    name: str = "bobo"


@dataclass
class Trees:
    name: str = "my_tree"


class Point(NamedTuple):
    x: float
    y: float


TFriend1 = TypeVar("TFriend1", Animal, Person)


@dataclass
class Student(Generic[TFriend1]):
    name: str
    age: int
    position: Point
    friends_type1: list[TFriend1]


point2d = Point(1.0, 2.0)
other_student: Student[Animal] = Student(
    age=25, name="bla", position=point2d, friends_type1=[Animal()]
)
# student: Student[Student] = {
#     "name": "ouss",
#     "age": 25,
#     "position": point2d,
#     "friends": [other_student],
# }
# student_that_only_like_anaimals: Student[Animal] = {
#     "name": "ouss",
#     "age": 25,
#     "position": point2d,
#     "friends": [Animal()],
# }
print(other_student)


# # Point = namedtuple("Point", ["x", "y"])
# point2d = Point(1.0, 2.0)

# print(point2d)
# print(type(point2d))
# print(point2d[0])


# TAddableEnity = TypeVar("TAddableEnity", int, str, list, float, tuple)
# TException = TypeVar("TException", bound=Exception)


# def make_list_of_addable_enity(a: TAddableEnity, b: TAddableEnity) -> list[TAddableEnity]:
#     return [a, b]


# def add(a: TAddableEnity, b: TAddableEnity) -> TAddableEnity:
#     return a + b


# print(add(1, 2))
# print(add("ouss", "miss"))
# print(add([1, 2], [3, 4]))


# def raise_exception(err: TException):
#     raise err


# raise_exception(ValueError("I am an error"))
