import pytest
from main.LRU_cache import LRUCache


def test_put_and_get():
    cache = LRUCache(3)
    cache.put(1, 30)
    cache.put(3, 50)
    assert cache.get(3) == 50

def test_size_maximum():
    cache = LRUCache(3)
    cache.put(1, 30)
    cache.put(3, 50)
    cache.put(4, 90)
    cache.put(6, 25)
    assert cache.get(1) == -1
    assert cache.get(6) == 25

def test_least_recently_used():
    cache = LRUCache(3)
    cache.put(1, 30)
    cache.put(3, 50)
    cache.put(4, 90)
    cache.get(1)
    cache.put(6, 25)
    assert cache.get(3) == -1
    assert cache.get(1) == 30
    assert cache.get(6) == 25

def test_delete():
    cache = LRUCache(3)
    cache.put(1, 30)
    assert cache.get(1) == 30
    cache.delete(1)
    assert cache.get(1) == -1

def test_reset():
    cache = LRUCache(3)
    cache.put(1, 30)
    cache.put(3, 50)
    cache.reset()
    assert cache.get(1) == -1
    assert cache.get(3) == -1

def test_size_error():
    with pytest.raises(ValueError):
        cache = LRUCache(0)

def test_invalid_key():
    with pytest.raises(ValueError):
        cache = LRUCache(3)
        cache.put(3.5, 10)

def test_invalid_value():
    with pytest.raises(ValueError):
        cache = LRUCache(3)
        cache.put(3, "value")