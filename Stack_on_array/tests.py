from stack_on_array import Stack
from random import randint

"""тест добавления элементов в стек"""
def test_push_items() -> None:
    stack = Stack()
    items_list = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        stack.push(item)
        items_list.append(item)
    assert len(items_list) == stack.get_size()
    assert items_list[-1] == stack.check_top()

"""тест удаления элементов в стеке"""
def test_pop_items() -> None:
    stack = Stack()
    items_list = []
    for _ in range(10**4):
        item = randint(-10**4, 10**4)
        stack.push(item)
        items_list.append(item)
    for _ in range(2*10**3):
        stack.pop()
        items_list.pop()
    assert len(items_list) == stack.get_size()
    assert items_list[-1] == stack.check_top()
