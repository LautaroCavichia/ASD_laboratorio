class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, key):
        self.root = Node(key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self.recursive_insert(self.root, key)

    def recursive_insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self.recursive_insert(node.left, key)
            node.left.parent = node
        elif key > node.key:
            node.right = self.recursive_insert(node.right, key)
            node.right.parent = node
        return node

    def inorder_tree_walk_until(self, node, result, i):
        if node is not None and len(result) < i:
            self.inorder_tree_walk_until(node.left, result, i)
            if len(result) < i:
                result.append(node.key)
                self.inorder_tree_walk_until(node.right, result, i)

    def inorder_tree_walk(self, node, result):
        if node is not None:
            self.inorder_tree_walk(node.left, result)
            result.append(node.key)
            self.inorder_tree_walk(node.right, result)

    def os_select(self, i):
        result = []
        self.inorder_tree_walk_until(self.root, result, i)
        if i <= 0 or i > len(result):
            return None
        return result[i-1]

    def os_rank(self, key):
        result = []
        self.inorder_tree_walk(self.root, result,)
        rank = 1
        for k in result:
            if k == key:
                return rank
            rank += 1
        return None

