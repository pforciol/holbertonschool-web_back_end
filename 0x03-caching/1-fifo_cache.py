#!/usr/bin/python3
""" FIFOCache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching """

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                toDelete = sorted(self.cache_data)[0]
                print("DISCARD: {}".format(toDelete))
                del self.cache_data[toDelete]

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
