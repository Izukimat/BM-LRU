from main.LRU_cache import LRUCache

cache = LRUCache(1)
def test_put_01():
    assert cache.put(None, None) == "test"