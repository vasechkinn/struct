import pytest
from linkedlist import LinkedList

@pytest.fixture
def linkedlist():
    return LinkedList()

def test_is_empty_count(linkedlist):
    assert linkedlist.is_empty() == True, f"expected: {True}, result = {linkedlist.is_empty()}"
    assert linkedlist.count() == 0, f"expected: {0}, result = {linkedlist.count()}"

def test_add_find(linkedlist):
    linkedlist.add(3)
    assert linkedlist.find(3) == (3, None), f"expected: {(3, None)}, result = {linkedlist.find(3)}"
    assert linkedlist.count()== 1, f"expected: {1}, result = {linkedlist.count()}"
    assert linkedlist.is_empty() == False, f"expected: {False}, result = {linkedlist.is_empty()}"

def test_add_first_find(linkedlist):
    for i in [2, 3]:
        linkedlist.add_first(i)

    assert linkedlist.find(3) == (3, (2, None)), f"expected: {(3, (2, None))}, result = {linkedlist.find(3)}"    
    assert linkedlist.count()== 2, f"expected: {2}, result = {linkedlist.count()}"
    assert linkedlist.is_empty() == False, f"expected: {False}, result = {linkedlist.is_empty()}"

def test_add_remove_last_first(linkedlist):
    for i in [2, 3]:
        linkedlist.add(i)

    assert linkedlist.count()== 2, f"expected: {2}, result = {linkedlist.count()}"

    linkedlist.remove_first()
    assert linkedlist.find(3) == (3, None), f"expected: {(3, None)}, result = {linkedlist.find(3)}"
    assert linkedlist.count()== 1, f"expected: {1}, result = {linkedlist.count()}"

    linkedlist.remove_last()
    assert linkedlist.is_empty() == True, f"expected: {True}, result = {linkedlist.is_empty()}"
    assert linkedlist.count()== 0, f"expected: {0}, result = {linkedlist.count()}"

def test_remove_add(linkedlist):
    for i in [3, 3]:
        linkedlist.add(i)

    assert linkedlist.count()== 2, f"expected: {2}, result = {linkedlist.count()}"

    linkedlist.remove(3)
    assert linkedlist.find(3) == (3, None), f"expected: {(3, None)}, result = {linkedlist.find(3)}"
    assert linkedlist.count()== 1, f"expected: {1}, result = {linkedlist.count()}"

def test_clear(linkedlist):
    for i in [3, 3]:
        linkedlist.add(i)

    assert linkedlist.count()== 2, f"expected: {2}, result = {linkedlist.count()}"

    linkedlist.clear()
    assert linkedlist.count()== 0, f"expected: {0}, result = {linkedlist.count()}"
