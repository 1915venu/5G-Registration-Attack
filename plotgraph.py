import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_barplot(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Set up the seaborn style (white background with grid)
    sns.set(style="whitegrid")

    # Create the plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='UE_ID', y='Time', data=df, palette='Blues')  # Adjust palette as needed

    # Enhance the plot with labels and title
    plt.xlabel('UE ID', fontsize=14)
    plt.ylabel('Time (seconds)', fontsize=14)
    plt.title('Time vs UE ID', fontsize=16, fontweight='bold')

    # Add grid and improve layout
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    # Show the plot
    plt.show()

# Path to your CSV file
csv_file = 'time_differences_ninejun.csv'  # Replace with your CSV file path

# Plot the bar plot
plot_barplot(csv_file)
