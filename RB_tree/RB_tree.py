from __future__ import annotations
from typing import Any
from .node_tree import Node_tree
import pygraphviz

class Red_black_tree:
    def __init__(self) -> None:
        self.nill = Node_tree(None).get_nill()
        self.root = self.nill

    """метод получения отсортированных элементов дерева"""
    def get_sorted_items(self) -> list:
        values = []
        def traversal(root: Node_tree | None) -> None:
            if root.value is None:
                return
            traversal(root.right)
            values.append(root.value)
            traversal(root.left)
        traversal(self.root)
        return values

    """метод добавления элемента в дерево"""
    def add_item(self, value : Any) -> None:
        node_tree = Node_tree(value)
        node_tree.left = self.nill
        node_tree.right = self.nill
        node_tree.set_red()
        y = None
        x = self.root
        while x.value is not None:
            y = x
            if node_tree.value < x.value: x = x.left
            elif node_tree.value > x.value: x = x.right
            else: return
        node_tree.parent = y
        if y is None: self.root = node_tree
        elif node_tree.value < y.value: y.left = node_tree
        else: y.right = node_tree
        if node_tree.parent is None:
            node_tree.set_black()
            return
        if node_tree.parent.parent is None: return
        self.__fix_add_item(node_tree)

    """метод удаления элемента из дерева по значению"""
    def delete_item(self, value : Any) -> None:
        z = self.nill
        Node_tree = self.root
        while Node_tree.value is not None:
            if Node_tree.value == value:
                z = Node_tree
                break
            if Node_tree.value < value: Node_tree = Node_tree.right
            else: Node_tree = Node_tree.left
        if z.value is None: return
        y = z
        y_original_color = y.color
        if z.left.value is None:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right.value is None):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.__get_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z: x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if not y_original_color:
            self.__fix_delete_item(x)

    """метод пересадки узлов"""
    def __rb_transplant(self, u: Node_tree, v: Node_tree) -> None:
        if u.parent is None: self.root = v
        elif u == u.parent.left: u.parent.left = v
        else: u.parent.right = v
        v.parent = u.parent

    """метод получения узла с минимальным значением"""
    def __get_minimum(self, Node_tree : Node_tree = None) -> Node_tree:
        if Node_tree is None: Node_tree = self.root
        if Node_tree.value is None: return self.nill
        while Node_tree.left.value is not None:
            Node_tree = Node_tree.left
        return Node_tree

    """метод правого поворота дерева"""
    def __right_rotate(self, x: Node_tree) -> None:
        y = x.left
        x.left = y.right
        if y.right.value is not None: y.right.parent = x
        y.parent = x.parent
        if x.parent is None: self.root = y
        elif x == x.parent.right: x.parent.right = y
        else: x.parent.left = y
        y.right = x
        x.parent = y
        
    """метод левого поворота дерева"""
    def __left_rotate(self, x: Node_tree) -> None:
        y = x.right
        x.right = y.left
        if y.left.value is not None: y.left.parent = x
        y.parent = x.parent
        if x.parent is None: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x
        x.parent = y

    """вспомогающий метод сохранения балансировки при вставки"""
    def __fix_add_item(self, Node_tree: Node_tree) -> None:
        while Node_tree.parent.is_red():
            if Node_tree.parent == Node_tree.parent.parent.right:
                uncle = Node_tree.parent.parent.left
                if uncle.is_red():
                    uncle.set_black()
                    Node_tree.parent.set_black()
                    Node_tree.parent.parent.set_red()
                    Node_tree = Node_tree.parent.parent
                else:
                    if Node_tree == Node_tree.parent.left:
                        Node_tree = Node_tree.parent
                        self.__right_rotate(Node_tree)
                    Node_tree.parent.set_black()
                    Node_tree.parent.parent.set_red()
                    self.__left_rotate(Node_tree.parent.parent)
            else:
                uncle = Node_tree.parent.parent.right
                if uncle.is_red():
                    uncle.set_black()
                    Node_tree.parent.set_black()
                    Node_tree.parent.parent.set_red()
                    Node_tree = Node_tree.parent.parent
                else:
                    if Node_tree == Node_tree.parent.right:
                        Node_tree = Node_tree.parent
                        self.__left_rotate(Node_tree)
                    Node_tree.parent.set_black()
                    Node_tree.parent.parent.set_red()
                    self.__right_rotate(Node_tree.parent.parent)
            if Node_tree == self.root:
                break
        self.root.set_black()

    """метод добавления узлов в график"""
    def __add_Node_trees_graph(self, graph : object, Node_tree: Node_tree):
        Node_tree_id = Node_tree.value
        graph.add_node(
            Node_tree_id,
            label=str(Node_tree.value),
            fillcolor="red" if Node_tree.is_red() else "black",
            fontcolor="white",
            style="filled"
        )
        if Node_tree.left and Node_tree.left.value is not None:
            graph.add_edge(Node_tree.value, Node_tree.left.value)
            self.__add_Node_trees_graph(graph, Node_tree.left)
        if Node_tree.right and Node_tree.right.value is not None:
            graph.add_edge(Node_tree.value, Node_tree.right.value)
            self.__add_Node_trees_graph(graph, Node_tree.right)

    """метод получения графика дерева"""
    def get_graph(self, filename: str | None = "tree") -> bytes | None:
        graph = pygraphviz.AGraph(strict=True, directed=True)
        if self.root != self.nill: self.__add_Node_trees_graph(graph, self.root)
        graph.layout(prog="dot")
        return graph.draw(filename)

    """вспомогающий метод сохранения балансировки при удалении"""
    def __fix_delete_item(self, x: Node_tree) -> None:
        while x != self.root and x.is_black():
            if x == x.parent.left:
                s = x.parent.right
                if s.is_red():
                    s.set_black()
                    x.parent.set_red()
                    self.__left_rotate(x.parent)
                    s = x.parent.right
                if s.left.is_black() and s.right.is_black():
                    s.set_red()
                    x = x.parent
                else:
                    if s.right.is_black():
                        s.left.set_black()
                        s.set_red()
                        self.__right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.set_black()
                    s.right.set_black()
                    self.__left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.is_red():
                    s.set_black()
                    x.parent.set_red()
                    self.__right_rotate(x.parent)
                    s = x.parent.left
                if s.left.is_black() and s.right.is_black():
                    s.set_red()
                    x = x.parent
                else:
                    if s.left.is_black():
                        s.right.set_black()
                        s.set_red()
                        self.__left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.set_black()
                    s.left.set_black()
                    self.__right_rotate(x.parent)
                    x = self.root
        x.set_black()
