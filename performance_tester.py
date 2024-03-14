import matplotlib.pyplot as plt
import random
import time
import csv
from binary_search_tree import BinarySearchTree, AVLTree
from linked_list import OrderedLinkedList


def test_os_operation_performance(data_structure_type, operation, use_random_selection=False):

    # Initialize the specified data structure
    if data_structure_type == 'OrderedLinkedList':
        ds = OrderedLinkedList()
        list_sizes = range(10, 6000, 300)
    elif data_structure_type == 'BinarySearchTree':
        ds = BinarySearchTree()
        list_sizes = range(10, 7000, 300)
    elif data_structure_type == 'AVLTree':
        ds = AVLTree()
        list_sizes = range(10, 7000, 300)
    else:
        raise ValueError("Unsupported data structure type.")

    operation_times = []

    for size in list_sizes:
        ds = ds.__class__()

        for i in range(1, size + 1):
            ds.insert(random.randint(1, 1000))

        target = random.randint(1, size) if use_random_selection else size // 2 if operation == 'os_select' else size

        start_time = time.time()
        if operation == 'os_select':
            ds.os_select(target)
        elif operation == 'os_rank':
            ds.os_rank(target)
        else:
            raise ValueError("Unsupported operation. Use 'os_select' or 'os_rank'.")
        end_time = time.time()
        operation_times.append(end_time - start_time)

    return list_sizes, operation_times


def save_to_csv(filename, list_sizes, operation_times):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['List Size', 'Time (seconds)'])
        for size, time_taken in zip(list_sizes, operation_times):
            writer.writerow([size, time_taken])

    print(f"Data saved to {filename}.")


def plot_performance(list_sizes, operation_times, title):
    plt.figure(figsize=(10, 5))
    plt.plot(list_sizes, operation_times, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel('List Size')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()


def plot_multiple_performances(list_sizes_list, operation_times_list, labels, title):
    plt.figure(figsize=(10, 5))
    colors = ['b', 'g', 'r']  # Predefined colors for the plots
    for i, (list_sizes, operation_times) in enumerate(zip(list_sizes_list, operation_times_list)):
        plt.plot(list_sizes, operation_times, marker='o', linestyle='-', color=colors[i], label=labels[i])

    plt.title(title)
    plt.xlabel('List Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

