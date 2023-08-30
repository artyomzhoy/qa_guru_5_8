# import enum
from enum import Enum
from dataclasses import dataclass


class UserStatus(Enum):  # enum - список допустимых значений
    Student = "student"
    Worker = "worker"


@dataclass  # декоратор, реализует __init__ вместо нас
class User:
    name: str
    age: int
    status: UserStatus
    items: list[str]

    # def __init__(self, name, age, status, items):  # self - переменная по создаваемому экземпляру класса
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items

    # метод самого класса
    @classmethod
    def from_csv(cls, user_dict):  # cls - класс, то же самое, если бы использовали User
        return cls(name=user_dict["name"],
                   age=int(user_dict["age"]),
                   status=UserStatus["status"],
                   items=user_dict["items"])

    # метод экземпляра класса
    def is_adult(self) -> bool:
        return self.age >= 18


class Worker(User):  # наследуем от User

    def __init__(self, name, age, items):
        super().__init__(name=name, age=age, status=UserStatus.Worker, items=items)  # super - инициализация родительского класса

    @classmethod
    def from_user(cls, user: User):
        assert user.status == UserStatus.Worker
        return cls(name=user.name, age=user.age, items=user.items)

    def do_work(self):
        pass


if __name__ == '__main__':
    oleg = User(name="Oleg", age=17, status=UserStatus("student"), items=[])
    assert oleg.is_adult() is False
    assert not oleg.is_adult()
    # assert oleg.status == "student"

    olga = User(name="Olga", age=20, status=UserStatus("student"), items=[])
    assert olga.is_adult()

    w = Worker(name="worker", age=20, items=[])
    print()
