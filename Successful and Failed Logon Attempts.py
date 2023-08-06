import pandas as pd
import matplotlib.pyplot as plt

def successful_logon(dataset_file, column_name):
    df = pd.read_csv(dataset_file)
    column_data = df[column_name]
    value_counts = column_data.value_counts()

    # Print and get the top 10 unique_values and their occurrences
    print(f"Top 10 Unique values in '{column_name}':")
    top_10_values = value_counts.head(10)
    for value in top_10_values.index:
        print(f"{value}: {top_10_values[value]} occurrences")

    # Increase the figure size to avoid cutoff
    plt.figure(figsize=(12, 7))

    # Plot the bar chart for the top 10 unique_values and their occurrences
    plt.bar(top_10_values.index, top_10_values.values, orientation='vertical')  # Set orientation to 'vertical'
    plt.xlabel('Users')
    plt.ylabel('Number of Logon')
    plt.title('Successful Logon')

    plt.xticks(rotation=75)  # Rotate x-axis labels vertically

    plt.tight_layout()  # Ensure labels and title fit within the figure

    plt.savefig(graph_output_path)
    plt.close()

def failed_logon(failed_dataset_file, failed_column_name):
    df = pd.read_csv(failed_dataset_file)
    column_data = df[failed_column_name]
    value_counts = column_data.value_counts()

    # Print and get the top 10 unique_values and their occurrences
    print(f"Top 10 Unique values in '{failed_column_name}':")
    top_10_values = value_counts.head(10)
    for value in top_10_values.index:
        print(f"{value}: {top_10_values[value]} occurrences")

    # Increase the figure size to avoid cutoff
    plt.figure(figsize=(12, 7))

    # Plot the bar chart for the top 10 unique_values and their occurrences
    plt.bar(top_10_values.index, top_10_values.values, orientation='vertical')  # Set orientation to 'vertical'
    plt.xlabel('Users')
    plt.ylabel('Logon Attempts')
    plt.title('Failed Logon')

    plt.xticks(rotation=75)  # Rotate x-axis labels vertically

    plt.tight_layout()  # Ensure labels and title fit within the figure

    plt.savefig(failed_graph_output_path)
    plt.close()


dataset_file_path = "/home/kali/Desktop/Successful Logon_2023_07_31_0003.csv"
failed_dataset_file_path = "/home/kali/Desktop/Failed Logon.csv"
graph_output_path = '/home/kali/Desktop/Successful_logon.png'  # Added '.png' extension
failed_graph_output_path ='/home/kali/Desktop/Failed_logon.png'
column_to_analyze = input("Enter name of column: ")
successful_logon(dataset_file_path, column_to_analyze)
print()
failed_logon(failed_dataset_file_path, column_to_analyze)


