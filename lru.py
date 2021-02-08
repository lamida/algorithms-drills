class LRUCache:

    def __init__(self, capacity: int):
        self.d = [None] * capacity

    def get(self, key: int) -> int:
        print(self.d)
        for i in range(len(self.d)):
            if self.d[i] is not None and self.d[i][0] == key:
                val = self.d[i][1]
                self.d.remove((key, val))
                self.d = [(key, val)] + self.d
                return val
        return -1


     def put(self, key: int, value: int) -> None:
        for i in range(len(self.d)):
            if self.d[i] is not None and self.d[i][0] == key:
                self.d[i] = (key, value)
                self.d.remove((key, value))
                self.d = [(key, value)] + self.d
                print(f"after put {key}, {value}. Data: {self.d}")
                return None
            
        vacant = len(list(filter(lambda x: x is None, self.d)))
        if vacant == 0:
            self.d[-1] = None
            
        self.d = [(key, value)] + self.d
        self.d.remove(None)
        return None

if __name__ == "__main__":
    c = LRUCache(2)
    c.put(2, 1)
    c.put(1,1)
    c.put(2,3)
    c.put(4,1)
    print(c.get(1))
    print(c.get(2))
