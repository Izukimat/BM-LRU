from collections import OrderedDict

class LRUCache(object):
    def __init__(self, max_items):
        self.max_items = max_items
        self.cache = OrderedDict()

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.max_items:
            self.cache.popitem(False)
        self.cache[key] = value

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        else:
            return None #TODO add error handling

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
        else:
            pass

    def reset(self):
        self.cache.clear()
