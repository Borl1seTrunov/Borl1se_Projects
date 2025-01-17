from modules.linked_list import Linked_list
from modules.linked_list import Node
from typing import Any

class Stack:
    def __init__(self) -> None:
        self.items : Linked_list = Linked_list()
        self.size : int = 0

    """метод добавления в стек"""
    def push(self, val : Any) -> None:
        if val is None:
            return
        self.items.push_front(val)
        self.size += 1
        
    """метод удаление элемента из стека"""
    def pop(self) -> None:
        if self.size == 0:
            return
        self.items.pop_front()
        self.size -= 1

    """метод получения значения верхнего элемента"""
    def check_top(self) -> Any | None:
        if self.size == 0:
            return
        item : Node = self.items.get_item_by_idx(0)
        return item.get_value()

    """метод получения количества элементов в стеке"""
    def get_size(self) -> int:
        return self.size
