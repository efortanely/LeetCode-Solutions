from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.items = 0
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:    
            self.items += 1
            if self.items > self.capacity:
                self.items -=1
                self.cache.popitem(last=False)
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
