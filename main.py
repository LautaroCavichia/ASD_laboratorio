from performance_tester import test_os_operation_performance, plot_performance, save_to_csv, plot_multiple_performances



list_sizes, operation_times = test_os_operation_performance('OrderedLinkedList','os_select', 13000, 'worst', 3)
save_to_csv('os_select_worst_case_performance_ordered_linked_list.csv', list_sizes, operation_times)
list_sizes2, operation_times2 = test_os_operation_performance('BinarySearchTree', 'os_select',13000, 'worst', 3)
save_to_csv('os_select_worst_case_performance_binary_search_tree.csv', list_sizes2, operation_times2)
list_sizes3, operation_times3 = test_os_operation_performance('AVLTree', 'os_select',13000, 'worst', 3)
save_to_csv('os_select_worst_case_performance_avl_tree.csv', list_sizes3, operation_times3)
plot_multiple_performances([list_sizes, list_sizes2, list_sizes3], [operation_times, operation_times2, operation_times3], [  'OrderedLinkedList', 'BinarySearchTree', 'AVLTree'], 'os_select Performance')
plot_multiple_performances([list_sizes, list_sizes2, list_sizes3], [operation_times, operation_times2, operation_times3], [  'OrderedLinkedList', 'BinarySearchTree', 'AVLTree'], 'os_select Performance', 'log')
