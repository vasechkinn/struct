import pytest
from deq import Deq

@pytest.fixture
def deq():
    return Deq()

def test_enqueue_peek_pop(deq):
    deq.enqueue(3)
    assert deq.is_empty() == False, f"expected: {False}, result: {deq.is_empty()}"

    assert deq.peek() == 3, f"expected: {3}, result: {deq.peek()}"
    assert deq.peek_last() == 3, f"expected: {3}, result: {deq.peek_last()}"

    assert deq.count() == 1, f"expected: {1}, result: {deq.count()}"

def test_enqueue_first_peek_peek_last(deq):
    deq.enqueue(2)
    deq.enqueue_first(3)
    assert deq.peek() == 3, f"expected: {3}, result: {deq.peek()}"
    assert deq.peek_last() == 2, f"expected: {2}, result: {deq.peek_last()}"
    assert deq.count() == 2, f"expected: {2}, result: {deq.count()}"

def test_negative(deq):
    assert deq.is_empty() == True, f"expected: {True}, result: {deq.is_empty()}"

    assert deq.peek() is None, f"expected: {None}, result: {deq.peek()}"
    assert deq.peek_last() is None, f"expected: {None}, result: {deq.peek_last()}"

    assert deq.dequeue_tail() is None, f"expected: {None}, result: {deq.dequeue_tail()}"
    assert deq.dequeue() is None, f"expected: {None}, result: {deq.dequeue()}"

    assert deq.count() == 0, f"expected: {0}, result: {deq.count()}"

def test_dequeue_dequeue_tail(deq):
    deq.enqueue(2)
    deq.enqueue(1)
    deq.enqueue_first(3)
    """
    1. [2]
    2. [1, 2]
    3. [1, 2, 3]
    """
    assert deq.count() == 3, f"expected: {3}, result: {deq.count()}"
    assert deq.dequeue_tail() == 1, f"expected: {1}, result: {deq.dequeue_tail()}"
    assert deq.count() == 2, f"expected: {2}, result: {deq.count()}"

    assert deq.dequeue() == 3, f"expected: {3}, result: {deq.dequeue()}"
    assert deq.count() == 1, f"expected: {1}, result: {deq.count()}"

    assert deq.peek() == 2, f"expected: {2}, result: {deq.peek()}"