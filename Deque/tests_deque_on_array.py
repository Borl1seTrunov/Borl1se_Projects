from deque_on_array import Deque
from random import randint

"""тест добавления в начало деки"""
def test_push_front() -> None:
    deque = Deque()
    items_list = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        deque.push_front(item)
        items_list.insert(0, item)
    assert len(items_list) == deque.get_size()
    assert items_list[0] == deque.check_front()

"""тест добавления в конец деки"""
def test_push_back() -> None:
    deque = Deque()
    items_list = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        deque.push_back(item)
        items_list.append(item)
    assert len(items_list) == deque.get_size()
    assert items_list[-1] == deque.check_back()

"""тест удаления из конца деки"""
def test_pop_back() -> None:
    deque = Deque()
    items_list = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        deque.push_back(item)
        items_list.append(item)
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        deque.push_front(item)
        items_list.insert(0, item)
    for _ in range(5*10**3):
        deque.pop_back()
        items_list.pop()
    assert len(items_list) == deque.get_size()
    assert items_list[-1] == deque.check_back()
    assert items_list[0] == deque.check_front()

"""тест удаления из начала деки"""
def test_pop_front() -> None:
    deque = Deque()
    items_list = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        deque.push_back(item)
        items_list.append(item)
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        deque.push_front(item)
        items_list.insert(0, item)
    for _ in range(5*10**3):
        deque.pop_front()
        items_list.pop(0)
    assert len(items_list) == deque.get_size()
    assert items_list[-1] == deque.check_back()
    assert items_list[0] == deque.check_front()
