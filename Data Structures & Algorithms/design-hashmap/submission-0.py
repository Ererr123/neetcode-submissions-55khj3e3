class MyHashMap:

    def __init__(self):
        self.container = {}   

    def put(self, key: int, value: int) -> None:

        self.container[key] = value

    def get(self, key: int) -> int:
        return self.container.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.container:
             del self.container[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)