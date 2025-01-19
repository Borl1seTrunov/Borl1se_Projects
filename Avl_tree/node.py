from typing import Any

class Node:
    def __init__(self, val : Any, left = None, right = None) -> None:
        self.val : Any = val
        self.left : Node | None = left
        self.right : Node | None = right
        self.height : int = 1
