from double_linked_list import Double_linked_list
from random import randint

"""тест вставки в конец списка"""
def test_push_back() -> None:
    dllist = Double_linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        dllist.push_back(item)
        items_list.append(item)
    assert dllist.get_items_array() == items_list

"""тест вставки в начало списка"""
def test_push_front() -> None:
    dllist = Double_linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        dllist.push_front(item)
        items_list.insert(0,item)
    assert dllist.get_items_array() == items_list

"""тест удаления элементов с конца"""
def test_pop_back() -> None:
    dllist = Double_linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        dllist.push_back(item)
        items_list.append(item)
    for _ in range(10**3):
        dllist.pop_back()
        items_list.pop()
    assert dllist.get_items_array() == items_list
    assert dllist.get_size() == 9*10**3

"""тест удаления элементов с начала"""
def test_pop_front() -> None:
    dllist = Double_linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        dllist.push_back(item)
        items_list.append(item)
    for _ in range(5*10**3):
        dllist.pop_front()
        items_list.pop(0)
    assert dllist.get_items_array() == items_list
    assert dllist.get_size() == 5*10**3

"""тест вставки элементов в случайное место"""
def test_insert_item() -> None:
    dllist = Double_linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        dllist.push_back(item)
        items_list.append(item)
    for _ in range(10**4):
        item = randint(0, 10**4)
        idx = randint(0, 10**4)
        dllist.insert(idx, item)
        items_list.insert(idx, item)
    assert dllist.get_items_array() == items_list

"""тест удаления элемента по индексу"""
def test_pop_by_idx_item() -> None:
    dllist = Double_linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        dllist.push_back(item)
        items_list.append(item)
    for _ in range(5*10**3):
        idx = randint(0, 5*10**3)
        dllist.pop(idx)
        items_list.pop(idx)
    assert dllist.get_items_array() == items_list
    assert dllist.get_size() == 5*10**3

"""тест получения элемента по индексу"""
def test_get_item_by_idx() -> None:
    dllist = Double_linked_list()
    items_list = []
    for _ in range(10**4):
        item = randint(0, 10**4)
        dllist.push_back(item)
        items_list.append(item)
    for _ in range(10**3):
        random_idx = randint(0,10**4)
        item_in_dllist = dllist.get_item_by_idx(random_idx).get_value()
        item_in_items_list = items_list[random_idx]
        assert item_in_dllist == item_in_items_list
