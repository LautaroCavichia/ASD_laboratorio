from complexity_tester import *


def get_user_input(prompt, choices=None):
    user_input = input(prompt)
    if choices and user_input not in choices:
        print(f"Invalid choice. Please choose from {choices}.")
        return get_user_input(prompt, choices)
    return user_input


def run_and_plot(operation, case, max_size, num_runs):
    sizes = range(10, max_size, max_size // 10)
    if case == 'worst':
        sizes = range(10, max_size // 1000, max_size // 10) # Worst case is limited because of recursion depth

    results = run_multiple_tests(sizes, num_runs, operation, case)
    plot_results(results, operation, 'linear')
    plot_results(results, operation, 'log')


if __name__ == "__main__":
    operation = get_user_input("Select operation (os_select(s)/os_rank(r): ", ['s', 'r'])
    map_operation = {'s': 'os_select', 'r': 'os_rank'}
    operation = map_operation[operation]
    case = get_user_input("Select case (best(b)/average(a)/worst(w)): ", ['b', 'a', 'w'])
    map_case = {'b': 'best', 'a': 'average', 'w': 'worst'}
    case = map_case[case]
    max_size = int(get_user_input("Max Size: "))
    num_runs = int(get_user_input("Number of Runs: "))
    print(f"Running {operation} operation with {case} case, up to size {max_size}, {num_runs} times.")
    run_and_plot(operation, case, max_size, num_runs)
    print("Plotted!")

