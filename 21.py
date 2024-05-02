class BasicNode:
    def __init__(self, priority: int = None, value: int = None, parent=None, children=None):
        self.priority = priority
        self.value = value
        self._parent = parent
        self._children = children if children else []

    def __str__(self):
        return f"(priority, value) -> {self.priority, self.value}"

    def add_children(self, new_children):
        self._children.append(new_children)

    def size(self):
        return len(self._children)

    def _merge_nodes(self, f, s):
        to, frm = sorted((f, s), key=lambda n: n.priority)
        to.merge(self._children_frm_node(frm))
        frm._parent = to
        return to

    @staticmethod
    def _children_frm_node(frm):
        new = [None] * (frm.size() + 1)
        new[-1] = frm
        return new

    def merge(self, other):
        to, frm = self._children, other[::]
        if len(to) > len(frm):
            frm.extend([None] * (len(to) - len(frm)))
        else:
            to.extend([None] * (len(frm) - len(to)))
        carry = None
        for i, (f, t) in enumerate(zip(frm, to)):
            if f and t:
                to[i] = carry
                carry = self._merge_nodes(t, f)
            elif carry and ((e := f) or (e := t)):
                to[i] = None
                carry = self._merge_nodes(carry, e)
            elif carry:
                to[i] = carry
                carry = None
            elif f:
                to[i] = f
        if carry:
            to.append(carry)


class BinominalHeap:
    def __init__(self, trees=None):
        self.root_node = BasicNode(children=trees)
        self.trees = self.root_node._children

    def __move_up(self, node: BasicNode):
        to_swap = None
        while node._parent and node._parent.priority > node.priority:
            to_swap = node._parent
            for i, child in enumerate(to_swap._children):
                if node == child:
                    to_swap._children[i] = to_swap
                    break
            if to_swap._parent:
                for i, child in enumerate(to_swap._parent._children):
                    if to_swap == child:
                        to_swap._parent._children[i] = node
                        break
            to_swap._children, node._children = node._children, to_swap._children
            node._parent, to_swap._parent = to_swap._parent, node

        if not to_swap:
            return

        for i, child in enumerate(self.trees):
            if child == to_swap:
                self.trees[i] = node

    def decrease_priority(self, node, new_priority):
        node.priority = new_priority
        self.__move_up(node)

    def peek_min(self):
        res = min(self.trees, key=lambda tree: tree.priority if tree else float("inf"))
        if not res:
            raise Exception("Cannot peek min")
        return res

    def delete(self, node):
        self.decrease_priority(node, -float("inf"))
        self.extract_min()

    def empty(self):
        return not self.trees

    def insert(self, priority: int, value: int):
        self.merge(BinominalHeap([BasicNode(priority, value)]))

    def extract_min(self):
        out = self.peek_min()
        self.trees[out.size()] = None
        if not self.trees[-1]:
            del self.trees[-1]

        for child in out._children:
            if child:
                child._parent = None

        if out._children:
            self.merge(BinominalHeap(out._children))

        out._parent = None
        out._children = []
        return out

    def merge(self, other):
        self.root_node.merge(other.trees)

    def __str__(self):
        return str([i.__str__() for i in self.trees])


from random import randint

b = BinominalHeap()
x = set([randint(0, 50) for _ in range(13)])
print(x)
for i in x:
    b.insert(i, 0)
print(b)
print(b.extract_min())
print(b.extract_min())
