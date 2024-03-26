from complexity_tester import *

#test os_select operation performance on AVLTree
sizes = range(10, 1000, 50)
num_runs = 1
operation = 'os_rank'
results = test_data_structure_cases(sizes, num_runs, operation, 'BST')
plot_results(results, operation, 'linear', False)








