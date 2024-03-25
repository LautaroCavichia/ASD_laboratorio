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
    list_sizes = range(1, max_size, 600)

    for size in list_sizes:
        time_taken = 0


        for _ in range(num_runs):
            ds = ds_class()
            for i in range(size):
                #insert first number for testing best case
                if case == 'best' and i == 0:
                    ds.insert(1)
                ds.insert(random.randint(1, 2*size))

            if case == 'middle':
                target = size // 2
            elif case == 'worst':
                target = 2*size - 1
            elif case == 'best':
                target = 1
            elif case == 'random':
                target = random.randint(1, size)
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


def plot_multiple_performances(list_sizes_list, operation_times_list, labels, title):
    plt.figure(figsize=(10, 5))
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, (list_sizes, operation_times) in enumerate(zip(list_sizes_list, operation_times_list)):
        plt.plot(list_sizes, operation_times, marker='o', linestyle='-', color=colors[i], label=labels[i])

    plt.title(title)
    plt.xlabel('List Size')
    plt.ylabel('Time (seconds)')
    #plt.yscale('log')  # Logarithmic scale
    plt.legend()
    plt.grid(True)
    plt.show()

