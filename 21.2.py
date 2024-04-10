class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def __str__(self):
        return str(self.key)


class BinomialHeap:
    def __init__(self):
        self.trees = []

    def insert(self, key):
        self.merge([BinomialTree(key)])

    def get_min(self):
        if not self.trees:
            return None
        min_key = self.trees[0].key
        for tree in self.trees:
            if tree.key < min_key:
                min_key = tree.key
        return min_key

    def merge(self, other_trees):
        self.trees += other_trees
        self.trees.sort(key=lambda tree: len(tree.children))
        i = 0
        while i < len(self.trees) - 1:
            if len(self.trees[i].children) == len(self.trees[i + 1].children):
                merged_tree = BinomialTree(min(self.trees[i].key, self.trees[i + 1].key))
                if self.trees[i].key < self.trees[i + 1].key:
                    merged_tree.add_child(self.trees[i + 1])
                    merged_tree.children += self.trees[i].children
                else:
                    merged_tree.add_child(self.trees[i])
                    merged_tree.children += self.trees[i + 1].children
                self.trees.pop(i)
                self.trees.pop(i)
                self.trees.insert(i, merged_tree)
            else:
                i += 1

    def find_min_tree_index(self):
        min_tree_index = None
        for i, tree in enumerate(self.trees):
            if min_tree_index is None or tree.key < self.trees[min_tree_index].key:
                min_tree_index = i
        return min_tree_index

    def extract_min(self):
        min_tree_index = self.find_min_tree_index()
        if min_tree_index is None:
            return None
        min_tree = self.trees.pop(min_tree_index)
        self.merge(min_tree.children[::-1])
        return min_tree.key

    def decrease_key(self, tree, old_key, new_key):
        if tree.key != old_key:
            for child in tree.children:
                self.decrease_key(child, old_key, new_key)
        elif tree.key == old_key:
            tree.key = new_key
            while tree.parent and tree.key < tree.parent.key:
                tree.key, tree.parent.key = tree.parent.key, tree.key
                tree = tree.parent

    def _find_node(self, trees, key):
        for tree in trees:
            if tree.key == key:
                return tree
            found_in_children = self._find_node(tree.children, key)
            if found_in_children:
                return found_in_children
        return None

    def delete(self, key):
        node_to_delete = self._find_node(self.trees, key)
        if node_to_delete:
            self.decrease_key(node_to_delete, key, float('-inf'))
            self.extract_min()


heap = BinomialHeap()
heap.insert(10)
heap.insert(1)
heap.insert(5)
heap.insert(6)
heap.insert(11)
heap.insert(45)
heap.insert(2)
heap.insert(23)
print(heap.get_min())
heap.delete(1)
print(heap.get_min())
heap.delete(2)
heap.delete(10)
print(heap.get_min())
heap.delete(5)
heap.delete(6)
print(heap.get_min())
heap.delete(11)
heap.delete(45)
print(heap.get_min())
