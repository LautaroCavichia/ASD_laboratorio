class BaseNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Node(BaseNode):
    def __init__(self, key):
        super().__init__(key)
        self.parent = None


class AVLNode(BaseNode):
    def __init__(self, key):
        super().__init__(key)
        self.parent = None
        self.height = 1
        self.size = 1

    def get_balance(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height

    def update_values(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = max(left_height, right_height) + 1
        left_size = self.left.size if self.left else 0
        right_size = self.right.size if self.right else 0
        self.size = left_size + right_size + 1


class BaseTree:
    def __init__(self):
        self.root = None

    def set_root(self, key):
        self.root = Node(key)

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


class BinarySearchTree(BaseTree):
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self.recursive_insert(self.root, key)

    def recursive_insert(self, node, key):
        if node is None:
            return Node(key)
        if key == node.key:
            return node  # No duplicates allowed
        elif key < node.key:
            node.left = self.recursive_insert(node.left, key)
            node.left.parent = node
        elif key > node.key:
            node.right = self.recursive_insert(node.right, key)
            node.right.parent = node
        return node

    def os_select(self, i):
        result = []
        self.inorder_tree_walk_until(self.root, result, i)
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


class AVLTree(BaseTree):
    def insert(self, key):
        if self.root is None:
            self.root = AVLNode(key)
        else:
            self.root = self.recursive_insert(self.root, key)

    def recursive_insert(self, node, key):
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self.recursive_insert(node.left, key)
        elif key > node.key:
            node.right = self.recursive_insert(node.right, key)
        else:
            return node  # No duplicates allowed
        node.update_values()
        return self._balance(node)

    def _balance(self, node):
        balance_factor = node.get_balance()
        if balance_factor > 1:
            if node.left.get_balance() < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance_factor < -1:
            if node.right.get_balance() > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.update_values()
        y.update_values()
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.update_values()
        x.update_values()
        return x

    def os_select(self, i):
        if i < 1 or i > self.root.size:
            return None
        return self._os_select(self.root, i)

    def _os_select(self, node, i):
        left_size = node.left.size if node.left else 0
        if i == left_size + 1:
            return node.key
        elif i <= left_size:
            return self._os_select(node.left, i)
        else:
            return self._os_select(node.right, i - left_size - 1)

    def os_rank(self, key):
        return self._os_rank(self.root, key)

    def _os_rank(self, node, key):
        if not node:
            return 0
        if key == node.key:
            return (node.left.size if node.left else 0) + 1
        elif key < node.key:
            return self._os_rank(node.left, key)
        else:
            left_size = node.left.size if node.left else 0
            return left_size + 1 + self._os_rank(node.right, key)

