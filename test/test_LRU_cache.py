from main.LRU_cache import LRUCache

cache = LRUCache(3)
def test_put_01():
    cache.put(1, 30)
    cache.put(3, 50)
    assert cache.get(3) == 50

def test_put_02():
    cache.put(1, 30)
    cache.put(3, 50)
    cache.put(4, 90)
    cache.put(6, 25)
    assert cache.get(1) == -1