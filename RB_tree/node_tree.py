from __future__ import annotations
from typing import Any

class Node_tree:
    def __init__(self, value : Any | None) -> None:
        self.value : Any |None = value
        self.parent: Node_tree | None = None
        self.left: Node_tree | None = None
        self.right: Node_tree | None = None
        self.height: int = 1
        self.color: bool = True

    """метод получения значения узла"""
    def get_value(self) -> Any:
        return self.value

    """метод получения высоты узла"""
    @staticmethod
    def get_height(node_tree : Node_tree | None) -> int:
        return node_tree.height if Node_tree is not None else 0

    """метод возвращающий черный лист"""
    @staticmethod
    def get_nill() -> Node_tree:
        node_tree = Node_tree(None)
        node_tree.set_black()
        return node_tree

    """метод перекраски узла в черный цвет"""
    def set_black(self) -> None:
        self.color = False

    """метод перекраски узла в красный цвет"""
    def set_red(self) -> None:
        self.color = True

    """метод проверки узла на черный цвет"""
    def is_black(self) -> bool:
        return not self.color

    """метод проверки узла на красный цвет"""
    def is_red(self) -> bool:
        return self.color

    """метод починки высоты узла"""
    def fix_height(self) -> None:
        left_height : int = Node_tree.get_height(self.left)
        right_height : int = Node_tree.get_height(self.right)
        self.height = max(left_height, right_height) + 1
