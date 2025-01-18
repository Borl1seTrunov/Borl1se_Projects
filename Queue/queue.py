from typing import Any

class Queue:
    def __init__(self) -> None:
        self.items : list[Any] = []
        self.size : int = 0

    """метод получения размера очереди"""
    def get_size(self) -> int:
        return self.size

    """метод добавления в очередь"""
    def push(self, val : Any) -> None:
        if val is None:
            return
        self.items.append(val)
        self.size += 1

    """метод удаления из очереди"""
    def pop(self) -> None:
        if self.size == 0:
            return
        self.items.pop(0)
        self.size -= 1

    """метод получения первого значения в очереди"""
    def check_top(self) -> Any | None:
        if self.size == 0:
            return
        return self.items[0]

    """метод получения последнего значения в очереди"""
    def check_bottom(self) -> Any | None:
        if self.size == 0:
            return
        return self.items[-1]

    """метод получения элементов очереди"""
    def get_items(self) -> list[Any] | None:
        if self.size == 0:
            return
        return self.items
