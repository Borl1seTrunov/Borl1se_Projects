from random import randint
from avl_tree import Avl_tree

"""тест вставки в дерево"""
def test_insert() -> None:
    avl_tree : Avl_tree = Avl_tree()
    list_items : list = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        avl_tree.insert(item)
        list_items.append(item)
    tree_items = avl_tree.get_sorted_items()
    assert tree_items[::-1] == sorted(list_items)
    assert len(tree_items) == len(list_items)
    
"""тест удаления из дерева"""
def test_delete() -> None:
    avl_tree : Avl_tree = Avl_tree()
    list_items : list = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        avl_tree.insert(item)
        list_items.append(item)
    for idx in range(5*10**3):
        item = list_items[idx]
        avl_tree.delete_value(item)
        list_items.pop(idx)
    tree_items = avl_tree.get_sorted_items()
    assert tree_items[::-1] == sorted(list_items)
    assert len(tree_items) == len(list_items)
    
