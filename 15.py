class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Индекс вне диапазона")

    def append(self, element):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = element
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Массив пуст, невозможно удалить элемент")
        popped_element = self.array[self.size - 1]
        self.size -= 1

        if self.size <= self.capacity // 4:
            self._shrink()

        return popped_element

    def _resize(self, new_capacity=None):
        new_capacity = self.capacity * 2 if new_capacity is None else new_capacity
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def _shrink(self):
        new_capacity = max(2, self.capacity // 2)
        self._resize(new_capacity)
