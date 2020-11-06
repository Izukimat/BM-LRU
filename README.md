# Introduction
This is a short implementation of `LRUCache` class by Python3.8 for BM's assignment.

# Requirement
This code is confirmed to work on Python 3.8 environment.\
Install [pytest](https://docs.pytest.org/en/stable/index.html) for running unit test.

# Features
This LRU Cache has the following features.
1. `LRUCache` class is initialized with a **maximum size**.
2. It must be able to **put** the value of a key.
3. It must be able to **get** the value of a key.
4. It must be able to **delete** a key. Attempting to delete a key that doesn't exist is a no-op
5. It must be able to **reset** the cache, which will remove all items from the cache.
6. When adding new keys that cause the capacity to be exceeded, the "last recently used"\
   key needs to be identified and discarded.
  
# Config

#### *class* LRUCache
  **parameters**\
    `size (int)`: Maximum size of the cache. It should be positive integer.\
    \
  **methods**\
    `put (int, int)`: Set a value to a key in the cache. For the simplicity, `int` is\
     set to the type of both key and value.\
     \
    `get (int)`: Return a value of the corresponding key in the cache. If no key is found in the cache,\
     it returns `-1`.\
     \
    `delete (int)`: Delete a key and its value. If no key is found in the cache, there is no operation.\
    \
    `reset()`: Delete all items in the cache.
    
# Usage

example:
```
>>> cache = LRUCache(3)    # Initialize cache
>>> cache.put(1, 10)       # Set vaue 10 to key 1
>>> cache.get(1)
>>> 10

>>> cache.get(3)
>>> -1                     # Key 3 does not exist

>>> cache.delete(1)
>>> cache.get(1)
>>> -1                     # Key 1 does not exist anymore
```

# Test
Run `pytest` under the BM-LRU directory. 

# Implementation
This LRU Cache is implemented with `OrderedDict`, which is a dictionary subclass that remembers\
the order that keys were first inserted. It is implemented by hash map and doubly linked list.
Therefore computational speeds for each of the following operations are:
`put: O(1)`
`get: O(1)`
`delete: O(1)`.



