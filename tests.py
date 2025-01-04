from linked_list import Linked_list
from random import randint

"""тест вставки в конец списка"""
def test_push_back() -> None:
    llist = Linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        llist.push_back(item)
        items_list.append(item)
    assert llist.get_items_array() == items_list

"""тест вставки в начало списка"""
def test_push_front() -> None:
    llist = Linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        llist.push_front(item)
        items_list.insert(0,item)
    assert llist.get_items_array() == items_list

"""тест удаления элементов с конца"""
def test_pop_back() -> None:
    llist = Linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        llist.push_back(item)
        items_list.append(item)
    for _ in range(10**3):
        llist.pop_back()
        items_list.pop()
    assert llist.get_items_array() == items_list
    assert llist.get_size() == 9*10**3

"""тест удаления элементов с начала"""
def test_pop_front() -> None:
    llist = Linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        llist.push_back(item)
        items_list.append(item)
    for _ in range(5*10**3):
        llist.pop_front()
        items_list.pop(0)
    assert llist.get_items_array() == items_list
    assert llist.get_size() == 5*10**3

"""тест вставки элементов в случайное место"""
def test_insert_item() -> None:
    llist = Linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        llist.push_back(item)
        items_list.append(item)
    for _ in range(10**4):
        item = randint(0, 10**4)
        idx = randint(0, 10**4)
        llist.insert(idx, item)
        items_list.insert(idx, item)
    assert llist.get_items_array() == items_list

"""тест удаления элемента по индексу"""
def test_pop_by_idx_item() -> None:
    llist = Linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        llist.push_back(item)
        items_list.append(item)
    for _ in range(5*10**3):
        idx = randint(0, 5*10**3)
        llist.pop(idx)
        items_list.pop(idx)
    assert llist.get_items_array() == items_list
    assert llist.get_size() == 5*10**3