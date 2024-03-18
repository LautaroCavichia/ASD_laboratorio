class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
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


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:  # Duplicate keys not allowed
            return node

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
            return 0  # Key not in tree
        if key == node.key:
            return (node.left.size if node.left else 0) + 1
        elif key < node.key:
            return self._os_rank(node.left, key)
        else:
            left_size = node.left.size if node.left else 0
            return left_size + 1 + self._os_rank(node.right, key)
