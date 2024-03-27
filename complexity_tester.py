import time
import gc
from ds_generator import generate_linked_list_data, generate_bst_data, generate_avl_data
import random
import matplotlib.pyplot as plt


def run_test(data_structure_type, operation, size, case):
    gc.disable()
    # Initialize the data structure
    if data_structure_type == 'AVL':
        data_structure = generate_avl_data(size)
        if operation == 'os_select':
            if case == 'best':
                select_target = size // 2
            elif case == 'average':
                select_target = random.randint(1, size)
            else:
                select_target = random.randint(size/2 , size)
        elif operation == 'os_rank':
            # Generating all possible keys and selecting based on case
            all_keys = [i for i in range(size)]
            if case == 'best':
                rank_target = all_keys[size // 2]
            elif case == 'average':
                # Random key for an average case
                rank_target = random.choice(all_keys)
            else:
                rank_target = all_keys[size - 1]

    elif data_structure_type == 'BST':
        data_structure = generate_bst_data(size, case)
        if operation == 'os_select':
            if case == 'best':
                select_target = 1
            elif case == 'average':
                select_target = random.randint(1, size)
            else:
                select_target = size
        elif operation == 'os_rank':
            if case == 'best':
                rank_target = 1
            elif case == 'average':
                rank_target = random.randint(1, size)
            else:
                rank_target = size

    elif data_structure_type == 'OrderedLinkedList':
        data_structure = generate_linked_list_data(size)
        if operation == 'os_select':
            if case == 'best':
                select_target = 1
            elif case == 'average':
                select_target = random.randint(1, size)
            else:
                select_target = size
        elif operation == 'os_rank':
            if case == 'best':
                rank_target = 1
            elif case == 'average':
                rank_target = random.randint(1, size)
            else:
                rank_target = size

    if operation == 'os_select':
        start_time = time.time()
        data_structure.os_select(select_target)
    elif operation == 'os_rank':
        start_time = time.time()
        data_structure.os_rank(rank_target)
    operation_time = time.time() - start_time
    gc.enable()
    return operation_time


def run_multiple_tests(sizes, num_runs, operation, case):
    data_structure_types = ['AVL', 'BST', 'OrderedLinkedList']
    results = []

    for data_structure_type in data_structure_types:
        for size in sizes:
            total_time = 0

            for i in range(num_runs):
                operation_time = run_test(data_structure_type, operation, size, case)
                total_time += operation_time

            average_time = total_time / num_runs
            results.append((data_structure_type, size, average_time))

    return results


def test_data_structure_cases(sizes, num_runs, operation, data_structure_type):
    cases = ['best', 'average', 'worst']
    results = []

    for case in cases:
        for size in sizes:
            total_time = 0
            for _ in range(num_runs):

                operation_time = run_test(data_structure_type, operation, size, case)
                total_time += operation_time

            average_time = total_time / num_runs
            results.append((data_structure_type, size, average_time, case))

    return results


def plot_results(results, operation, scale='linear', different_data_structures=True):
    plt.figure(figsize=(10, 5))
    if different_data_structures:
        for data_structure_type in ['AVL', 'BST', 'OrderedLinkedList']:
            sizes = [size for ds_type, size, avg_time in results if ds_type == data_structure_type]
            times = [avg_time for ds_type, size, avg_time in results if ds_type == data_structure_type]
            plt.plot(sizes, times, marker='o', label=data_structure_type)
    else:
        for case in ['best', 'average', 'worst']:
            sizes = [size for ds_type, size, avg_time, c in results if c == case]
            times = [avg_time for ds_type, size, avg_time, c in results if c == case]
            plt.plot(sizes, times, marker='o', label=f'{case} case')

    plt.title(f'{operation} performance comparison')
    plt.xlabel('Size')
    plt.ylabel('Time (s)')
    plt.legend()
    if scale == 'log':
        plt.yscale('log')
    plt.tight_layout()
    plt.grid(True, which="both", ls="--")
    plt.show()


def double_plot_results(results1, results2, operation, scale='linear'):
    plt.figure(figsize=(10, 5))
    for case in ['average', 'worst']:
        sizes = [size for ds_type, size, avg_time, c in results1 if c == case]
        times = [avg_time for ds_type, size, avg_time, c in results1 if c == case]
        plt.plot(sizes, times, marker='o', label=f'{case} case {results1[0][0]}')

        sizes = [size for ds_type, size, avg_time, c in results2 if c == case]
        times = [avg_time for ds_type, size, avg_time, c in results2 if c == case]
        plt.plot(sizes, times, marker='o', label=f'{case} case {results2[0][0]}')

    plt.title(f'{operation} performance comparison')
    plt.xlabel('Size')
    plt.ylabel('Time (s)')
    plt.legend()
    if scale == 'log':
        plt.yscale('log')
    plt.tight_layout()
    plt.grid(True, which="both", ls="--")
    plt.show()



def export_to_latex_direct(results, operation_case):
    header = """\\begin{figure}[H]
\\label{tab:%s_combined}
\\begin{tabular}{|c|c|c|c|}
\\toprule
List Size & AVL Tree Time (seconds) & BST Time (seconds) & Ordered Linked List Time (seconds) \\\\
\\midrule""" % operation_case

    footer = """\\bottomrule
\\end{tabular}
\\caption{OS-SELECT %s performance table for all data structures}
\\end{figure}""" % operation_case.replace('_', ' ').capitalize()

    # Assuming results are sorted by size
    # First, we need to structure the results by size and data structure
    structured_results = {}
    for data_structure_type, size, average_time in results:
        if size not in structured_results:
            structured_results[size] = {}
        structured_results[size][data_structure_type] = average_time

    # Generate rows for the first 5 and last 5 sizes
    sizes_sorted = sorted(structured_results.keys())
    selected_sizes = sizes_sorted[:5] + ["..."] + sizes_sorted[-5:]

    rows = []
    for size in selected_sizes:
        if size == "...":
            rows.append("... & ... & ... & ... \\\\")
            continue

        avl_time = structured_results[size].get('AVL', 'N/A')
        bst_time = structured_results[size].get('BST', 'N/A')
        oll_time = structured_results[size].get('OrderedLinkedList', 'N/A')
        row = f"{size} & {avl_time:e} & {bst_time:e} & {oll_time:e} \\\\"
        rows.append(row)

    latex_code = "\n".join([header] + rows + [footer])

    return latex_code