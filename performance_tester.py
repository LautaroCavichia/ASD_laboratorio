import matplotlib.pyplot as plt
import random
import timeit
import gc
import csv
from binary_tree import BinarySearchTree, AVLTree
from linked_list import OrderedLinkedList


def test_os_operation_performance(data_structure_type, operation, max_size, case='middle', num_runs=3):
    random.seed(42)
    gc.disable()  # Disable garbage collector

    data_structure_classes = {
        'OrderedLinkedList': OrderedLinkedList,
        'BinarySearchTree': BinarySearchTree,
        'AVLTree': AVLTree
    }
    ds_class = data_structure_classes.get(data_structure_type)
    if ds_class is None:
        raise ValueError("Unsupported data structure type.")

    operation_times = []
    list_sizes = range(10, max_size, 1000)

    for size in list_sizes:
        time_taken = 0

        for _ in range(num_runs):
            ds = ds_class()
            for i in range(size):
                if operation == 'os_rank':
                    if case == 'best' and i == 0:
                        ds.insert(1)
                    if case == 'middle' and i == size // 2:
                        ds.insert(size)
                    if case == 'worst' and i == size - 1:
                        ds.insert(2*size)
                ds.insert(random.randint(1, 2*size))

            if operation == 'os_select':
                if case == 'middle':
                    if ds_class == AVLTree:
                        target = size // 4
                    else:
                        target = size // 2
                elif case == 'worst':
                    target = size
                elif case == 'best':
                    if ds_class == AVLTree:
                        target = size // 2 + random.randint(1, size // 4)
                    else:
                        target = 1
                elif case == 'random':
                    target = random.randint(1, size//2)
                else:
                    raise ValueError("Unsupported case")

            elif operation == 'os_rank':
                if case == 'middle':
                    target = size
                elif case == 'worst':
                    target = 2*size
                elif case == 'best':
                    target = 1
                elif case == 'random':
                    target = random.randint(1, 2*size)
                else:
                    raise ValueError("Unsupported case")

            start = timeit.default_timer()
            if operation == 'os_select':
                ds.os_select(target)
            elif operation == 'os_rank':
                ds.os_rank(target)
            else:
                raise ValueError("Unsupported operation")
            time_taken += timeit.default_timer() - start

        operation_times.append(time_taken / num_runs)

    gc.enable()  # Re-enable garbage collector

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


def plot_multiple_performances(list_sizes_list, operation_times_list, labels, title, scale='linear'):
    plt.figure(figsize=(10, 5))
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, (list_sizes, operation_times) in enumerate(zip(list_sizes_list, operation_times_list)):
        plt.plot(list_sizes, operation_times, marker='o', linestyle='-', color=colors[i], label=labels[i])

    plt.title(title)
    plt.xlabel('List Size')
    plt.ylabel('Time (seconds)')
    if scale == 'log':
        plt.yscale('log')  # Logarithmic scale
    plt.legend()
    plt.grid(True)
    plt.show()


def avl_worst_case():
    operation_times = []
    avl = AVLTree()
    list_sizes = range(10, 40000, 1000)
    for size in list_sizes:
        for i in range(40000):
            avl.insert(i)

        start = timeit.default_timer()
        avl.os_select(40000)
        time_taken = timeit.default_timer() - start
        operation_times.append(time_taken)
    return list_sizes, operation_times




