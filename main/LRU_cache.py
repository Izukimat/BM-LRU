from collections import OrderedDict

class LRUCache:
    def __init__(self, size: int) -> None:
        """
        :type size: int
        """
        if size < 1:
            raise ValueError('Cache size cannot be less than 1')
        if type(size) is not int:
            raise ValueError('Cache size must be an integer')

        self.size = size
        self.cache = OrderedDict()

    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if type(key) is not int:
            raise ValueError('Key must be an integer')
        if type(value) is not int:
            raise ValueError('Value must be an integer')

        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.size:
            self.cache.popitem(False)
        self.cache[key] = value

    def get(self, key: int) -> int:
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        else:
            return -1

    def delete(self, key: int) -> None:
        """
        :type key: int
        :rtype: void
        """
        if key in self.cache:
            del self.cache[key]
        else:
            pass

    def reset(self) -> None:
        """
        :type: void
        :rtype: void
        """
        self.cache.clear()
