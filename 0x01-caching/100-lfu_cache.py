#!/usr/bin/env python3
""" LFU Caching module """

from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a Least Frequently Used (LFU) caching system """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = defaultdict(OrderedDict)
        self.key_freq = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.get(key)  # Update the frequency
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._evict()

        self.cache_data[key] = item
        self.key_freq[key] = 1
        self.frequency[1][key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        freq = self.key_freq[key]
        value = self.frequency[freq].pop(key)

        if not self.frequency[freq]:
            del self.frequency[freq]

        self.key_freq[key] += 1
        self.frequency[freq + 1][key] = value

        return self.cache_data[key]

    def _evict(self):
        """ Evict the least frequently used item """
        min_freq = min(self.frequency)
        key, _ = self.frequency[min_freq].popitem(last=False)

        if not self.frequency[min_freq]:
            del self.frequency[min_freq]

        del self.cache_data[key]
        del self.key_freq[key]
        print(f"DISCARD: {key}")

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")
