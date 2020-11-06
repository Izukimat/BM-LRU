from collections import OrderedDict

class LRUCache(object):
    def __init__(self, max_items):
        self.max_items = max_items
        self.dict = OrderedDict()

    def put(self, key, value):
        if key in self.dict:
            del self.dict[key]
        elif len(self.dict) == self.max_items:
            self.dict.popitem(False)
        self.dict[key] = value
        
    def get(self, key):
        if key in self.dict:
            value = self.dict[key]
            del self.dict[key]
            self.dict[key] = value
            return value
        else:
            return None #TODO add error handling

    def delete(self, key):
        pass

    def reset(self):
        pass
