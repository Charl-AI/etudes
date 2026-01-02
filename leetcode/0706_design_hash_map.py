"""Design a HashMap without using any built-in hash table libraries."""


class MyHashMap:
    def __init__(self):
        # only 1 million possible keys as per problem definition
        self.arr: list[int] = [-1 for _ in range(int(1e6) + 1)]

    def put(self, key: int, value: int):
        self.arr[key] = value

    def get(self, key: int) -> int:
        return self.arr[key]

    def remove(self, key: int):
        self.arr[key] = -1
