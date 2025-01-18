from random import randint
from rb_tree import Red_black_tree

"""тест вставки в дерево"""
def test_add_items() -> None:
    rb_tree : Red_black_tree = Red_black_tree()
    list_items : list = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        rb_tree.add_item(item)
        list_items.append(item)
    list_items = list(set(list_items))
    tree_items = rb_tree.get_sorted_items()
    assert sorted(list_items)[::-1] == tree_items
    assert len(list_items) == len(tree_items)

"""тест удаления в дереве"""
def test_delete_items() -> None:
    rb_tree : Red_black_tree = Red_black_tree()
    list_items : list = []
    for _ in range(5*10**4):
        item = randint(-10**4, 10**4)
        rb_tree.add_item(item)
        list_items.append(item)
    list_items = list(set(list_items))
    for idx in range(len(list_items) // 2):
        item = list_items[idx]
        rb_tree.delete_item(item)
        list_items.pop(idx)
    tree_items = rb_tree.get_sorted_items()
    assert sorted(list_items)[::-1] == tree_items
    assert len(list_items) == len(tree_items)

"""тест поиска в дереве"""
def test_search_items() -> None:
    rb_tree : Red_black_tree = Red_black_tree()
    list_items : list = []
    for _ in range(5*10**4):
        item = randint(-10**4, 10**4)
        rb_tree.add_item(item)
        list_items.append(item)
    list_items = list(set(list_items))
    for idx in range(len(list_items) // 2):
        item = list_items[idx]
        assert item == rb_tree.find_item(item)
