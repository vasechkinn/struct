import pytest
from queue import Queue

@pytest.fixture
def queue():
    return Queue()

def test_is_empty_peeK_dequeue(queue):
    assert queue.is_empty() == True, f"expected: {True}, result = {queue.is_empty()}"
    assert queue.peek() is None, f"expected: {None}, result = {queue.peek()}"
    assert queue.dequeue() is None, f"expected: {None}, result = {queue.dequeue()}"
    assert queue.count() == 0, f"expected: {0}, result = {queue.count()}"

def test_enqueue_peek_count(queue):
    queue.enqueue(2)
    assert queue.is_empty() == False, f"expected: {False}, result = {queue.is_empty()}"
    assert queue.peek() == 2, f"expected: {2}, result = {queue.peek()}"
    assert queue.count() == 1, f"expected: {1}, result = {queue.count()}"

def test_peek_dequeue(queue):
    queue.enqueue(2)
    assert queue.dequeue() == 2, f"expected: {2}, result = {queue.dequeue()}"
    assert queue.is_empty() == True, f"expected: {True}, result = {queue.is_empty()}"
    assert queue.count() == 0, f"expected: {0}, result = {queue.count()}"
    """
    FIFO
    """
    queue.enqueue(2)
    queue.enqueue(1)
    assert queue.dequeue() == 2, f"expected: {2}, result = {queue.dequeue()}"
    assert queue.is_empty() == False, f"expected: {False}, result = {queue.is_empty()}"
    assert queue.count() == 1, f"expected: {0}, result = {queue.count()}"

def test_negative(queue):
    assert queue.peek() is None, f"expected: {None}, result = {queue.peek()}"
    assert queue.dequeue() is None, f"expected: {None}, result = {queue.dequeue()}"