from PyQt5 import QtWidgets
import random


class Category(str):

    def __init__(self, name, parent=None):
        self.id = random.random()
        self._parent = parent  # type: Category
        self.name = name
        self._children = dict()

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    def add_child(self, c):
        if not isinstance(c, Category):
            c = Category(c, parent=self)
        assert c._parent is None, "If category has already a parent, " \
                                 "use change_parent instead of add_child"
        c._parent = self
        self._children[c.id] = c

    def remove_child(self, c):
        c._parent = None
        self._children.pop(c.id)

    def change_parent(self, parent):  # type: (Category, Category) -> None
        if self._parent is not None:
            self._parent.remove_child(self)
        if parent is not None:
            parent.add_child(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        if self._children:
            child_repr = f' [{len(self._children)} children]'
        else:
            child_repr = ''
        return f'<Category {self.name}' + child_repr + '>'

    @property
    def full_name(self):
        if self._parent is not None:
            str = self._parent.full_name + '>' + self.name
        else:
            str = self.name
        return str


class TimeData:
    pass


class TimeKeeper(QtWidgets.QWidget):
    pass


if __name__ == "__main__":

    x = Category('hello')
    print(x)
