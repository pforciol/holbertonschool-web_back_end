#!/usr/bin/python3
""" LRUCache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """

    def __init__(self):
        super().__init__()
        self.history = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                toDelete = self.history[0]
                print("DISCARD: {}".format(toDelete))
                del self.cache_data[toDelete]
                self.history.pop(0)

            self.updateHistory(key)

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            self.updateHistory(key)
            return self.cache_data.get(key)
        return None

    def updateHistory(self, key):
        """ Updates cache history """
        if key in self.history:
            self.history.remove(key)
        self.history.append(key)
