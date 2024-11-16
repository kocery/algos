import random


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.priority = random.randint(1, 10 ** 9)
        self.size = 1
        self.sum = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"key: {self.key}, value: {self.value}, priority: {self.priority}"


class ImplicitTreap:
    def __init__(self):
        self.root = None

    @staticmethod
    def _get_size(node):
        return node.size if node else 0

    @staticmethod
    def _get_sum(node):
        return node.sum if node else 0

    def _update(self, node):
        if node:
            node.size = 1 + self._get_size(node.left) + self._get_size(node.right)
            node.sum = node.value + self._get_sum(node.left) + self._get_sum(node.right)

    def _split(self, node, key):
        if not node:
            return None, None

        if self._get_size(node.left) >= key:
            left, node.left = self._split(node.left, key)
            self._update(node)
            return left, node
        else:
            node.right, right = self._split(node.right, key - self._get_size(node.left) - 1)
            self._update(node)
            return node, right

    def _merge(self, left, right):
        if not left or not right:
            return left or right

        if left.priority > right.priority:
            left.right = self._merge(left.right, right)
            self._update(left)
            return left
        else:
            right.left = self._merge(left, right.left)
            self._update(right)
            return right

    def insert(self, pos, value):
        new_node = Node(pos, value)
        left, right = self._split(self.root, pos)
        self.root = self._merge(self._merge(left, new_node), right)

    def erase(self, pos):
        left, mid = self._split(self.root, pos)
        mid, right = self._split(mid, 1)
        self.root = self._merge(left, right)

    def erase_range(self, pos, count):
        left, mid = self._split(self.root, pos)
        mid, right = self._split(mid, count)
        self.root = self._merge(left, right)

    def sum(self, l, r):
        left, mid = self._split(self.root, l)
        mid, right = self._split(mid, r - l + 1)
        result = self._get_sum(mid)
        self.root = self._merge(self._merge(left, mid), right)
        return result


# Тестирование
if __name__ == "__main__":
    treap = ImplicitTreap()

    treap.insert(0, 10)
    treap.insert(1, 20)
    treap.insert(2, 30)
    treap.insert(3, 40)

    # Проверяем суммы
    assert treap.sum(0, 3) == 100  # Сумма всех элементов
    assert treap.sum(1, 2) == 50  # Сумма [20, 30]

    # Удаление элемента
    treap.erase(2)  # Удаляем элемент с позиции 2
    assert treap.sum(0, 2) == 70  # Остались [10, 20, 40]

    # Удаление элемента
    treap.erase_range(0, 2)  # Удаляем элементы с 0 по 2
    assert treap.sum(0, 2) == 40  # Осталось [40]
    print("Все тесты пройдены!")
