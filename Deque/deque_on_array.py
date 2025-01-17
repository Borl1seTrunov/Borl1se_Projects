from typing import Any

class Deque:
    def __init__(self) -> None:
        self.items : list = []
        self.size : int = 0

    """метод добавления в начало деки"""
    def push_front(self, val : Any) -> None:
        if val is None:
            return
        self.items.insert(0, val)
        self.size += 1

    """метод добавления в конец деки"""
    def push_back(self, val : Any) -> None:
        if val is None:
            return
        self.items.append(val)
        self.size += 1

    """метод удаления из начала деки"""
    def pop_front(self) -> None:
        if self.size == 0:
            return
        self.items.pop(0)
        self.size -= 1

    """метод удаления из конца деки"""
    def pop_back(self) -> None:
        if self.size == 0:
            return
        self.items.pop()
        self.size -= 1

    """метод получения верхнего элемента деки"""
    def check_back(self) -> Any | None:
        if self.size == 0:
            return
        return self.items[-1]

    """метод получения нижнего элемента деки"""
    def check_front(self) -> Any | None:
        if self.size == 0:
            return
        return self.items[0]

    """метод получения количества элементов деки"""
    def get_size(self) -> int:
        return self.size
