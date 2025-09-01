import pytest
from hash_map import HashMap

@pytest.fixture
def hashmap():
    return HashMap()

def test_add_count(hashmap):
    assert hashmap.count() == 0, f"expected: {0}, res: {hashmap.count()}"
    hashmap.add('1', '1')

    assert hashmap.count() == 1, f"expected: {1}, res: {hashmap.count()}"

    hashmap.add('1', '2')
    assert hashmap.count() == 1, f"expected: {1}, res: {hashmap.count()}"

def test_remove_count(hashmap):
    assert hashmap.count() == 0, f"expected: {0}, res: {hashmap.count()}"
    assert hashmap.remove('1') is None, f"expected: {None}, res: {hashmap.remove('1')}"
    assert hashmap.count() == 0, f"expected: {0}, res: {hashmap.count()}"

    hashmap.add('1', '2')
    assert hashmap.count() == 1, f"expected: {1}, res: {hashmap.count()}"
    hashmap.remove('1')
    assert hashmap.count() == 0, f"expected: {0}, res: {hashmap.count()}"

def test_get_count(hashmap):
    assert hashmap.count() == 0, f"expected: {0}, res: {hashmap.count()}"
    assert hashmap.get('1') is None, f"expected: {None}, res: {hashmap.get('1')}"
    assert hashmap.count() == 0, f"expected: {0}, res: {hashmap.count()}"

    hashmap.add('1', '2')
    assert hashmap.count() == 1, f"expected: {1}, res: {hashmap.count()}"
    
    assert hashmap.get('1') == '2', f"expected: {'2'}, res: {hashmap.get('1')}"
    assert hashmap.get('2') is None, f"expected: {None}, res: {hashmap.get('1')}"
    assert hashmap.count() == 1, f"expected: {1}, res: {hashmap.count()}"
