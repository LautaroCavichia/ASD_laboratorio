import random
from binary_tree import BinarySearchTree, AVLTree
from linked_list import OrderedLinkedList


def generate_linked_list_data(size):
    ordered_list = OrderedLinkedList()
    for i in range(size):
        ordered_list.insert(i)
    return ordered_list



def generate_bst_data(size, case):
    bst = BinarySearchTree()
    if case == 'best':
        def insert_balanced(bst, numbers):
            if not numbers:
                return
            mid_index = len(numbers) // 2
            print(numbers[mid_index])
            bst.insert(numbers[mid_index])
            insert_balanced(bst, numbers[:mid_index])
            insert_balanced(bst, numbers[mid_index + 1:])
        numbers = list(range(size))
        insert_balanced(bst, numbers)

    elif case == 'average':
        for _ in range(size):
            bst.insert(random.randint(0, size*2))

    elif case == 'worst':
        for i in range(size):
            bst.insert(i)
    return bst


def generate_avl_data(size):
    avl = AVLTree()
    for _ in range(size):
        avl.insert(random.randint(0, size*2))
    return avl

