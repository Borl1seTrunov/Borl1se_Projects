from random import randint
from queue import Queue

"""тест вставки в очередь"""
def test_push_in_queue() -> None:
    queue : Queue = Queue()
    list_items : list[Any] = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        queue.push(item)
        list_items.append(item)
    assert queue.get_size() == len(list_items)
    assert queue.get_items() == list_items
    assert queue.check_top() == list_items[0]
    assert queue.check_bottom() == list_items[-1]

"""тест удаления из очереди"""
def test_pop_in_queue() -> None:
    queue : Queue = Queue()
    list_items : list[Any] = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        queue.push(item)
        list_items.append(item)
    for _ in range(5*10**3):
        queue.pop()
        list_items.pop(0)
    assert queue.get_size() == len(list_items)
    assert queue.get_items() == list_items
    assert queue.check_top() == list_items[0]
    assert queue.check_bottom() == list_items[-1]
