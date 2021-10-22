#!/usr/bin/python3
""" LIFOCache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching """

    def __init__(self):
        super().__init__()
        self.last = ""

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                print("DISCARD: {}".format(self.last))
                del self.cache_data[self.last]

            self.last = key

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
