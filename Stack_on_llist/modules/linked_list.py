"""Односвязный список на python3"""
from typing import Any
from dataclasses import dataclass

"""Класс узла односвязного списка"""
@dataclass
class Node:
    def __init__(self, val : Any) -> None:
        self.value = val
        self.next = None
    
    def get_value(self) -> Any:
        return self.value

"""Класс односвязного списка"""
class Linked_list:
    def __init__(self) -> None:
        self.root : Node = None
        self.size : int = 0
    
    """метод добавление в начало списка"""
    def push_front(self, value : Any) -> None:
        if value is None:
            return
        new_node = Node(value)
        new_node.next = self.root
        self.root = new_node
        self.size += 1
    
    """метод добавления в конец списка"""
    def push_back(self, value : Any) -> None:
        if value is None:
            return
        new_node = Node(value)
        self.size += 1
        if self.root is None:
            self.root = new_node
            return
        root = self.root
        while root.next is not None:
            root = root.next
        root.next = new_node

    """метод вставки элемента по индексу"""
    def insert(self, idx : int ,value : Any) -> None:
        if value is None:
            return
        new_node = Node(value)
        llist_size = self.size
        if idx >= llist_size:
            return
        if idx == llist_size - 1:
            self.push_back(value)
            return
        if idx == 0:
            self.push_front(value)
            return
        root = self.root
        for _ in range(idx - 1):
            root = root.next
        new_node.next = root.next
        root.next = new_node
        self.size += 1
        
    """метод удаления из начала списка"""
    def pop_front(self) -> None:
        if self.root is None:
            return
        self.root = self.root.next
        self.size -= 1

    """метод удаления из конца списка"""
    def pop_back(self) -> None:
        if self.root is None:
            return
        if self.root.next is None:
            self.root = None
            self.size = 0
            return
        root = self.root
        while root.next.next is not None:
            root = root.next
        root.next = None
        self.size -= 1

    """метод удаления элемента по индексу"""
    def pop(self, idx : int) -> None:
        if idx == 0:
            self.pop_front()
            return
        llist_size = self.size
        if idx == llist_size - 1:
            self.pop_back()
            return
        if idx >= llist_size:
            return
        root = self.root
        for _ in range(idx - 1):
            root = root.next
        root.next = root.next.next
        self.size -= 1

    """метод получения элемента по индексу"""
    def get_item_by_idx(self, idx : int) -> Node | None:
        if idx >= self.size:
            return
        root = self.root
        for _ in range(idx):
            root = root.next
        return root

    """метод поиска элемента в списке"""
    def find(self, item : Any) -> Any:
        root = self.root
        while root:
            if root.value == item:
                return item
            root = root.next
        return None

    """метод получения размера списка"""
    def get_size(self) -> int:
        return self.size

    """метод вывода элементов списка"""
    def print_items(self) -> None:
        root = self.root
        def list_traversal(node : Node | None):
            if node is None:
                return
            print(node.get_value(), end = " ")
            return list_traversal(node.next)
        list_traversal(root)
    
    """метод получения массива из элементов списка"""
    def get_items_array(self) -> list:
        root = self.root
        items = []
        while root is not None:
            items.append(root.get_value())
            root = root.next
        return items
