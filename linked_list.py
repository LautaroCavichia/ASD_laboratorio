class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class OrderedLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            self.size += 1
        elif self.head.key > key:
            if self.head.key == key:
                return  # No duplicates allowed
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        else:
            current = self.head
            while current.next is not None and current.next.key < key:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def delete(self, key):
        if self.head is None:
            return
        if self.head.key == key:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next is not None and current.next.key != key:
            current = current.next
        if current.next is not None:
            current.next = current.next.next
            self.size -= 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.key, end=' ')
            current = current.next
        print()

    def os_select(self, i):
        if i <= 0 or i > self.size:
            return None
        current_node = self.head
        for j in range(i-1):
            current_node = current_node.next
        return current_node.key

    def os_rank(self, key):
        current_node = self.head
        rank = 1
        while current_node is not None:
            if current_node.key == key:
                return rank
            current_node = current_node.next
            rank += 1
        return None



