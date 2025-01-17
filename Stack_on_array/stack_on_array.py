from typing import Any

class Stack:
    def __init__(self) -> None:
        self.items : list = []
        self.size : int = 0

    """метод добавления элемента в стек"""
    def push(self, val : Any) -> None:
        if val is None:
            return
        self.items.append(val)
        self.size += 1
    
    """метод удаления элемента из стека"""
    def pop(self) -> None:
        if self.size == 0:
            return
        self.items.pop()
        self.size -= 1

    """метод получения значения верхнего элемента"""
    def check_top(self) -> Any | None:
        if self.size == 0:
            return
        return self.items[-1]

    """метод получения количества элементов в стеке"""
    def get_size(self) -> int:
        return self.size
