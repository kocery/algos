class BasicNode:
    def __init__(self, priority: int = None, value: int = None, parent=None, children=None):
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
        self.trees = trees if trees else [BasicNode()]

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
        out = self.peek_min()
        self.trees[out.size()] = None
        if not self.trees[-1]:
            del self.trees[-1]

        if out.children:
            self.merge(BinaryHeap(out.children))

        out.parent = None
        out.children = []
        return out

    def merge(self, other):
        frm, to = sorted((self.trees, other.trees), key=lambda node: len(node)) # ничего не получается по схеме
        print(frm, to)
        r = [None] * len(to)
        carry = None
        for i, (f, t) in enumerate(zip(frm, to)):
            if f and t and carry:
                r[i] = carry
                carry = f.merge(t)
            elif f and t:
                carry = f.merge(t)
                r[i] = None
            elif f and carry:
                carry = f.merge(carry)
                r[i] = None
            elif t and carry:
                carry = carry.merge(t)
                r[i] = None
            elif f:
                r[i] = f
            elif t:
                r[i] = t
            else:
                r[i] = carry
                carry = None
        self.trees = carry


from random import randint

b = BinaryHeap()
x = set([randint(0, 50) for _ in range(15)])
print(x)
for i in x:
    b.insert(i, 0)
print(b)
print(b.extract_min())
print(b.extract_min())
