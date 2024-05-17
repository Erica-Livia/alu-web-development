#!/usr/bin/env python3


class BaseCaching:
    """"
    BaseCaching
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize the class """
        self.cache_data = {}


class BasicCache(BaseCaching):
    """ BasicCache """

    def put(self, key, item):
        """
        Add an item in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by Key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
