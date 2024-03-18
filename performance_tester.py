import matplotlib.pyplot as plt
import random
import timeit
import gc
import csv
from binary_tree import BinarySearchTree, AVLTree
from linked_list import OrderedLinkedList


def test_os_operation_performance(data_structure_type, operation, max_size, use_random_selection=False, num_runs=3):
    random.seed(42)  # Fix the seed for reproducibility
    gc.disable()  # Disable garbage collector

    # Initialize the specified data structure
    data_structure_classes = {
        'OrderedLinkedList': OrderedLinkedList,
        'BinarySearchTree': BinarySearchTree,
        'AVLTree': AVLTree
    }
    ds_class = data_structure_classes.get(data_structure_type)
    if ds_class is None:
        raise ValueError("Unsupported data structure type.")

    operation_times = []
    list_sizes = range(10, max_size, 700)  # More granular steps

    for size in list_sizes:
        time_taken = 0
        for _ in range(num_runs):  # Repeat test to get an average
            ds = ds_class()
            for i in range(size):
                ds.insert(random.randint(1, 2*size))  # Variable random range

            target = random.randint(1, size) if use_random_selection else size//2  # Random or middle element

            start = timeit.default_timer()
            if operation == 'os_select':
                ds.os_select(target)
            elif operation == 'os_rank':
                ds.os_rank(target)
            else:
                raise ValueError("Unsupported operation. Use 'os_select' or 'os_rank'.")
            time_taken += timeit.default_timer() - start

        operation_times.append(time_taken / num_runs)  # Average time

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
    colors = ['b', 'g', 'r']
    for i, (list_sizes, operation_times) in enumerate(zip(list_sizes_list, operation_times_list)):
        plt.plot(list_sizes, operation_times, marker='o', linestyle='-', color=colors[i], label=labels[i])

    plt.title(title)
    plt.xlabel('List Size')
    plt.ylabel('Time (seconds)')
    #plt.yscale('log')  # Logarithmic scale
    plt.legend()
    plt.grid(True)
    plt.show()

