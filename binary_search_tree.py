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

    def inorder_tree_walk(self, node, result):
        if node is not None:
            self.inorder_tree_walk(node.left, result)
            result.append(node.key)
            self.inorder_tree_walk(node.right, result)

    def os_select(self, i):
        result = []
        self.inorder_tree_walk(self.root, result)
        if i <= 0 or i > len(result):
            return None
        return result[i-1]

    def os_rank(self, key):
        result = []
        self.inorder_tree_walk(self.root, result)
        rank = 1
        for k in result:
            if k == key:
                return rank
            rank += 1
        return None


# we define also the AVL tree as a subclass of the BinarySearchTree with size attribute for os-rank and os-select
class AVLNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1

    def get_balance_factor(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height

    def update_height(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = max(left_height, right_height) + 1


class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self.size = 0

    def insert(self, key):  # we override the insert method to update the size attribute and to use the AVLNode class
        if self.root is None:
            self.root = AVLNode(key)
            self.size += 1
        else:
            self.root = self.recursive_insert(self.root, key)
            self.size += 1

    def balance(self, node):
        balance_factor = node.get_balance_factor()
        if balance_factor > 1:
            if node.left.get_balance_factor() < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance_factor < -1:
            if node.right.get_balance_factor() > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        node.update_height()
        return node

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.update_height()
        new_root.update_height()
        return new_root

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.update_height()
        new_root.update_height()
        return new_root

    def update_height(self, node):
        if node is not None:
            node.update_height()
            self.update_height(node.left)
            self.update_height(node.right)


def os_select(self, i): # we override the os_select method to use the size attribute and improve the time complexity
    r = self.left.size + 1
    if i == r:
        return self.key
    elif i < r:
        return self.left.os_select(i)
    else:
        return self.right.os_select(i - r)


def os_rank(self, key):  # we override the os_rank method to use the size attribute and improve the time complexity
    r = key.left.size + 1 if key.left else 1
    y = key
    while y != self.root:
        if y == y.parent.right:
            r = r + y.parent.left.size + 1
        y = y.parent

    return r



