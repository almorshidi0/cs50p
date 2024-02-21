class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("overflow")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("underflow")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity is not a non-negative int")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError("overflow")
        elif size < 0:
            raise ValueError("underflow")
        self._size = size
