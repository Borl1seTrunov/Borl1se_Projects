"""Двусвязный список на python3"""
from typing import Any
from dataclasses import dataclass

"""Класс узла двусвязного списка"""
@dataclass
class Node:
    def __init__(self, val : Any) -> None:
        self.value = val
        self.next = None
        self.prev = None
    
    def get_value(self) -> Any:
        return self.value

"""Класс двусвязного списка"""
class Double_linked_list:
    def __init__(self) -> None:
        self.root : Node = None
        self.size : int = 0
    
    """метод вставки элемента в начало двусвязного списка"""
    def push_front(self, value : Any) -> None:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.size += 1
            return
        new_node.next = self.root
        self.root.prev = new_node
        self.root = new_node
        self.size += 1
    
    """метод вставки элемента в конец двусвязного списка"""
    def push_back(self, value : Any) -> None:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.size += 1
            return
        root = self.root 
        while root.next is not None:
            root = root.next
        root.next = new_node
        new_node.prev = root
        self.size += 1
    
    """метод вставки элемента в список по индексу"""
    def insert(self, idx : int, value : Any) -> None:
        if idx >= self.size:
            return  
        if idx == 0:
            self.push_front(value)
            return
        if idx == self.size - 1:
            self.push_back(value)
            return
        new_node = Node(value)
        root = self.root
        for _ in range(idx):
            root = root.next
        root.prev.next = new_node
        new_node.prev = root.prev
        new_node.next = root
        root.prev = new_node
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
        root = self.root
        while root.next is not None:
            root = root.next
        root.prev.next = None
        self.size -= 1

    """метод удаления элемента по индексу"""
    def pop(self, idx : int) -> None:
        if idx >= self.size:
            return
        if idx == 0:
            self.pop_front()
            return
        if idx == self.size - 1:
            self.pop_back()
            return
        root = self.root
        for _ in range(idx):
            root = root.next
        root.prev.next = root.next
        root.next.prev = root.prev
        self.size -= 1

    """метод поиска элемента в списке"""
    def find(self, item : Any) -> Any:
        root = self.root
        while root:
            if root.value == item:
                return item
            root = root.next
        return None

    """метод получения количества элементов в списке"""
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
