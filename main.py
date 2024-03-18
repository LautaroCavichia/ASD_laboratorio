from performance_tester import test_os_operation_performance, plot_performance, save_to_csv, plot_multiple_performances

# os_rank
list_sizes, operation_times = test_os_operation_performance('OrderedLinkedList', 'os_rank',10000)
#save_to_csv('os_rank_middle_case_performance_ordered_linked_list.csv', list_sizes, operation_times)
list_sizes2, operation_times2 = test_os_operation_performance('BinarySearchTree', 'os_rank', 10000)
#save_to_csv('os_rank_middle_case_performance_binary_search_tree.csv', list_sizes2, operation_times2)
list_sizes3, operation_times3 = test_os_operation_performance('AVLTree', 'os_rank',10000)
#save_to_csv('os_rank_middle_case_performance_avl_tree.csv', list_sizes3, operation_times3)
plot_multiple_performances([list_sizes, list_sizes2, list_sizes3], [operation_times, operation_times2, operation_times3], [  'OrderedLinkedList', 'BinarySearchTree', 'AVLTree'], 'os_rank Performance')


# os_select
list_sizesb, operation_timesb = test_os_operation_performance('OrderedLinkedList','os_select', 10000)
#save_to_csv('os_select_middle_case_performance_ordered_linked_list.csv', list_sizesb, operation_timesb)
list_sizes2b, operation_times2b = test_os_operation_performance('BinarySearchTree', 'os_select',10000)
#save_to_csv('os_select_middle_case_performance_binary_search_tree.csv', list_sizes2b, operation_times2b)
list_sizes3b, operation_times3b = test_os_operation_performance('AVLTree', 'os_select',10000)
#save_to_csv('os_select_middle_case_performance_avl_tree.csv', list_sizes3b, operation_times3b)
plot_multiple_performances([list_sizesb, list_sizes2b, list_sizes3b], [operation_timesb, operation_times2b, operation_times3b], [  'OrderedLinkedList', 'BinarySearchTree', 'AVLTree'], 'os_select Performance')
