from linked_list import OrderedLinkedList
from binary_search_tree import *
from performance_tester import test_os_operation_performance, plot_performance, save_to_csv, plot_multiple_performances

# Test the performance of the os_select operation for the OrderedLinkedList
list_sizes, operation_times = test_os_operation_performance('OrderedLinkedList', 'os_rank', use_random_selection=True)

list_sizes2, operation_times2 = test_os_operation_performance('BinarySearchTree', 'os_rank', use_random_selection=True)

list_sizes3, operation_times3 = test_os_operation_performance('AVLTree', 'os_rank', use_random_selection=True)

plot_multiple_performances([list_sizes, list_sizes2, list_sizes3], [operation_times, operation_times2, operation_times3], [  'OrderedLinkedList', 'BinarySearchTree', 'AVLTree'], 'os_rank Performance')

#now os_select
list_sizesb, operation_timesb = test_os_operation_performance('OrderedLinkedList', 'os_select', use_random_selection=True)

list_sizes2b, operation_times2b = test_os_operation_performance('BinarySearchTree', 'os_select', use_random_selection=True)

list_sizes3b, operation_times3b = test_os_operation_performance('AVLTree', 'os_select', use_random_selection=True)

plot_multiple_performances([list_sizesb, list_sizes2b, list_sizes3b], [operation_timesb, operation_times2b, operation_times3b], [  'OrderedLinkedList', 'BinarySearchTree', 'AVLTree'], 'os_select Performance')

