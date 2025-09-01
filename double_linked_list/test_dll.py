import pytest
from double_ll import DoubleLinkedList

@pytest.fixture
def dll():
    return DoubleLinkedList()

def test_add_is_empty_find(dll):
    assert dll.is_empty() == True, f"expected: {True}, result: {dll.is_empty()}"
    assert dll.count() == 0, f"expected: {0}, result: {dll.count()}"

    dll.add(3)
    assert dll.is_empty() == False, f"expected: {False}, result: {dll.is_empty()}"
    assert dll.count() == 1, f"expected: {1}, result: {dll.count()}"

    assert dll.find(3) == (3, None, None), f"expected: {(3, None, None)}, result: {dll.find(3)}"

def test_add_add_first(dll):
    assert dll.is_empty() == True, f"expected: {True}, result: {dll.is_empty()}"
    assert dll.count() == 0, f"expected: {0}, result: {dll.count()}"

    dll.add(3)
    assert dll.is_empty() == False, f"expected: {False}, result: {dll.is_empty()}"
    assert dll.count() == 1, f"expected: {1}, result: {dll.count()}"

    dll.add_first(4)
    assert dll.is_empty() == False, f"expected: {False}, result: {dll.is_empty()}"
    assert dll.count() == 2, f"expected: {1}, result: {dll.count()}"

    """
    1. [3]
    2. [4, 3]
    """

def test_insert_add(dll):
    assert dll.is_empty() == True, f"expected: {True}, result: {dll.is_empty()}"
    assert dll.count() == 0, f"expected: {0}, result: {dll.count()}"

    dll.insert(1, 2)
    assert dll.is_empty() == False, f"expected: {False}, result: {dll.is_empty()}"
    assert dll.count() == 1, f"expected: {1}, result: {dll.count()}"

    dll.insert(2, 3)
    assert dll.is_empty() == False, f"expected: {False}, result: {dll.is_empty()}"
    assert dll.count() == 2, f"expected: {2}, result: {dll.count()}"

def test_negative_insert(dll):
    dll.add(1)

    with pytest.raises(ValueError):
        dll.insert(0)

    with pytest.raises(ValueError):
        dll.insert(10)

def test_removes(dll):
    assert dll.is_empty() == True, f"expected: {True}, result: {dll.is_empty()}"
    assert dll.count() == 0, f"expected: {0}, result: {dll.count()}"

    for i in [1, 2, 3]:
        dll.add(i)
        """
        1. [1]
        2. [1, 2]
        3. [1, 2, 3]
        """

    assert dll.is_empty() == False, f"expected: {False}, result: {dll.is_empty()}"
    assert dll.count() == 3, f"expected: {3}, result: {dll.count()}"

    dll.remove(3)
    """
    [1, 2]
    """
    assert dll.is_empty() == False, f"expected: {False}, result: {dll.is_empty()}"
    assert dll.count() == 2, f"expected: {2}, result: {dll.count()}"

    dll.remove_first()
    """
    [2]
    """
    assert dll.is_empty() == False, f"expected: {False}, result: {dll.is_empty()}"
    assert dll.count() == 1, f"expected: {1}, result: {dll.count()}"

    dll.remove_last()
    assert dll.is_empty() == True, f"expected: {True}, result: {dll.is_empty()}"
    assert dll.count() == 0, f"expected: {0}, result: {dll.count()}"

def test_clear(dll):
    dll.add(1)
    assert dll.is_empty() == False, f"expected: {False}, result: {dll.is_empty()}"
    assert dll.count() == 1, f"expected: {1}, result: {dll.count()}"

    dll.clear()
    assert dll.is_empty() == True, f"expected: {True}, result: {dll.is_empty()}"
    assert dll.count() == 0, f"expected: {0}, result: {dll.count()}"