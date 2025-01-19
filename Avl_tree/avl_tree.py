from typing import Any
from node import Node

class Avl_tree:
    def __init__(self) -> None:
        self.root: Node | None = None

    """метод получения высоты узла дерева"""
    @staticmethod
    def _get_height(node: Node | None) -> int:
        return node.height if node else 0

    """метод получения разницы узла"""
    def diff(self, root: Node | None) -> int:
        if root is None:
            return float("inf")
        ans = []
        if root.left is not None:
            ans.append(abs(root.left.val - root.val))
        if root.right is not None:
            ans.append(abs(root.right.val - root.val))
        return min(ans + [self.diff(root.left), self.diff(root.right)])

    """метод обновления высоты в узле"""
    def update_height(self, node: Node | None) -> None:
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

    """метод получения сбалансированности дерева"""
    def _get_balance(self, node: Node | None) -> int:
        return self._get_height(node.right) - self._get_height(node.left) if node else 0

    """метод правого поворота узла"""
    def right_rotate(self, node: Node) -> Node:
        left_child = node.left
        buffer = left_child.right
        left_child.right = node
        node.left = buffer
        self.update_height(node)
        self.update_height(left_child)
        return left_child

    """метод левого поворота узла"""
    def left_rotate(self, node: Node) -> Node:
        right_child = node.right
        buffer = right_child.left
        right_child.left = node
        node.right = buffer
        self.update_height(node)
        self.update_height(right_child)
        return right_child

    """метод балансировки узла"""
    def balance(self, node: Node) -> Node:
        self.update_height(node)
        cur_balance = self._get_balance(node)
        if cur_balance < -1:
            if self._get_balance(node.left) > 0:
                node.left = self.left_rotate(node.left)
            node = self.right_rotate(node)
        elif cur_balance > 1:
            if self._get_balance(node.right) < 0:
                node.right = self.right_rotate(node.right)
            node = self.left_rotate(node)
        return node

    """вспомогательный метод вставки узла"""
    def _insert(self, val: int, node: Node | None) -> Node:
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self._insert(val, node.left)
        else:
            node.right = self._insert(val, node.right)
        return self.balance(node)

    """метод вставки значения в дерево"""
    def insert(self, val: int) -> None:
        self.root = self._insert(val, self.root)

    """метод получения минимального значения узла"""
    def get_min(self, node: Node | None = None) -> Node:
        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        return node

    """метод получения максимального значения узла"""
    def get_max(self, node: Node | None = None) -> Node:
        if node is None:
            node = self.root
        while node.right is not None:
            node = node.right
        return node

    """метод удаления значения узла"""
    def delete_value(self, val: int) -> None:
        self.root = self._delete(self.root, val)

    """вспомогательный метод удаления значения узла"""
    def _delete(self, node: Node | None, val: int) -> Node | None:
        if node is None:
            return node
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        elif node.left is not None and node.right is not None:
            right_min = node.right
            while right_min.left is not None:
                right_min = right_min.left
            node.val = right_min.val
            node.right = self._delete(node.right, node.val)
        elif node.left is not None:
            node = node.left
        elif node.right is not None:
            node = node.right
        else:
            node = None
        return self.balance(node) if node else None

    """метод удаления минимального значения узла"""
    def delete_min(self, node: Node | None) -> Node | None:
        if node is None:
            return None
        if node.left:
            node.left = self.delete_min(node.left)
        else:
            return node.right

        return self.balance(node)

    """метод удаления максимального значения узла"""
    def delete_max(self, node: Node | None) -> Node | None:
        if node is None:
            return None
        if node.right:
            node.right = self.delete_max(node.right)
        else:
            return node.left

        return self.balance(node)

    """метод получения отсортированного списка элементов"""
    def get_sorted_items(self) -> list:
        values = []
        def traversal(root: Node | None) -> None:
            if root is None:
                return
            traversal(root.right)
            values.append(root.val)
            traversal(root.left)
        traversal(self.root)
        return values

    """метод поиска элемента в дереве"""
    def find_item(self, val : Any) -> Any | None:
        def get_item_by_node(val : Any, current_node : Node_tree) -> Any | None:
            if current_node is None:
                return
            node_value : Any = current_node.get_value()
            if node_value == val:
                return val
            if node_value > val:
                return get_item_by_node(val, current_node.left)
            return get_item_by_node(val, current_node.right)
        return get_item_by_node(val, self.root)
