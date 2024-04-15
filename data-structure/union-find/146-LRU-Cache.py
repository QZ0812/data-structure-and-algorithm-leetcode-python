class LRUCache:
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            self.dict[key] = self.dict.pop(key)
            return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        elif len(self.dict) >= self.max_capacity:
            self.dict.pop(next(iter(self.dict)))

        self.dict[key] = value
