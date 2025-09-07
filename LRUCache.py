class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.di = dict()
        self.size = 0
        self.least_used_key = None
        self.least_used_key_times = float("inf")

    def get(self, key: int) -> int:
        if key in self.di:
            self.size += 1
            self.di[key][1] += 1
            if self.di[key][1] < self.least_used_key_times:
                self.least_used_key_times = self.di[key][1]
                self.least_used_key = key
            return self.di[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.size == self.capacity:
            # 删除最少使用的一个。
            self.di.remove(key)
        else:
            self.least_used_key_times = 0
            self.least_used_key = key
            self.di[key] = [value, 0]