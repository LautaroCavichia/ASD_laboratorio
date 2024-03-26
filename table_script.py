import pandas as pd

# Load the CSV files into pandas dataframes
avl_df = pd.read_csv('os_select_worst_case_performance_avl_tree.csv')
bst_df = pd.read_csv('os_select_worst_case_performance_binary_search_tree.csv')
oll_df = pd.read_csv('os_select_worst_case_performance_ordered_linked_list.csv')



combined_df = avl_df.merge(bst_df, on='List Size').merge(oll_df, on='List Size')

# Now you'd have a single dataframe with the following columns if the merge is successful:
# 'List Size', 'Time (seconds)_avl', 'Time (seconds)_bst', 'Time (seconds)_oll'
# Let's rename these for clarity
combined_df.columns = ['List Size', 'AVL Tree Time (seconds)', 'BST Time (seconds)',
                       'Ordered Linked List Time (seconds)']


# Function to convert the merged dataframe to LaTeX table with specified format
def combined_dataframe_to_latex(df, caption, label):
    # Convert time to scientific format with 6 significant digits for all time columns
    for col in df.columns[1:]:  # Skip the first 'List Size' column
        df[col] = df[col].apply(lambda x: f"{x:.6e}")

    # Generate LaTeX table code
    latex_code = df.to_latex(index=False, caption=caption, label=label, escape=False, column_format='|c|c|c|c|')
    return latex_code


# Generate LaTeX table for the combined data
combined_latex = combined_dataframe_to_latex(combined_df, "OS-RANK Middle case Performance for All Data Structures",
                                             "tab:os_rank_combined")

print(combined_latex)
