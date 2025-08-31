import pytest
from stack import Stack

@pytest.fixture
def stack():
    return Stack()

def test_is_empty_peek_pop(stack):
    assert stack.is_empty() == True, f"expected: {True}, result = {stack.is_empty()}"
    assert stack.peek() is None, f"expected: {True}, result = {stack.peek()}"
    assert stack.pop() is None, f"expected: {True}, result = {stack.pop()}"
    assert stack.count() == 0, f"expected: {True}, result = {stack.count()}"

def test_add_peek_count(stack):
    stack.push(1)
    assert stack.peek() == 1, f"expected: {1}, result = {stack.peek()}"
    assert stack.count() == 1, f"expected: {1}, result = {stack.count()}"
    assert stack.is_empty() == False, f"expected: {False}, result = {stack.is_empty()}"

    stack.push(2)
    assert stack.peek() == 2, f"expected: {2}, result = {stack.peek()}"
    assert stack.count() == 2, f"expected: {2}, result = {stack.count()}"
    assert stack.is_empty() == False, f"expected: {False}, result = {stack.is_empty()}"

def test_push_pop_count(stack):
    stack.push(1)
    assert stack.pop()== 1, f"expected: {1}, result = {stack.pop()}"
    assert stack.count() == 0, f"expected: {0}, result = {stack.count()}"
    assert stack.is_empty() == True, f"expected: {True}, result = {stack.is_empty()}"


    stack.push(1)
    stack.push(2)
    assert stack.pop()== 2, f"expected: {2}, result = {stack.pop()}"
    assert stack.count() == 1, f"expected: {1}, result = {stack.count()}"
    assert stack.is_empty() == False, f"expected: {False}, result = {stack.is_empty()}"


def test_negative(stack):
    assert stack.pop() is None, f"expected: {None}, result = {stack.pop()}"
    assert stack.peek() is None, f"expected: {None}, result = {stack.peek()}"