class BasicNode:
    def __init__(self, priority: int, value: int, parent=None, children=None):
        self.priority = priority
        self.value = value
        self.parent = parent
        self.children = children if children else []

    def __str__(self):
        return f"(priority, value) -> {self.priority, self.value}"

    def size(self):
        return len(self.children)

    def add_children(self, new_children):
        self.children.append(new_children)

    def merge(self, other):
        _, other = sorted((self, other), key=lambda n: n.priority)
        self.children.append(other)
        other.parent = self
        return self


class BinaryHeap:
    def __init__(self, trees=None):
        self.trees = trees if trees else []

    @staticmethod
    def __move_up(node):
        while node.parent and node.parent.priority > node.priority:
            node.parent.children, node.children = node.children, node.parent.children
            node.parent, node.parent.parent = node.parent.parent, node.parent

    def decrease_priority(self, node, new_priority):
        node.priority = new_priority
        self.__move_up(node)

    def peek_min(self):
        res = min(self.trees, key=lambda tree: tree.priority if tree else float("inf"))
        if not res:
            raise IndexError()
        return res

    def delete(self, node):
        self.decrease_priority(node, -float("inf"))
        self.extract_min()

    def empty(self):
        return not self.trees

    def insert(self, priority: int, value: int):
        self.merge(BinaryHeap([BasicNode(priority, value)]))

    def extract_min(self):
        pass

    def merge(self, other):
        pass
