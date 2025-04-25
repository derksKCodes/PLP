# Importing necessary libraries
import pandas as pd                # For data manipulation and analysis
import numpy as np                 # For numerical operations
import matplotlib.pyplot as plt    # For creating visualizations
from sklearn.datasets import load_iris  # For loading the Iris dataset
import seaborn as sns  # Import seaborn for styling

# Function to load, explore, and clean the Iris dataset
def load_and_explore_data():
    """
    Loads the Iris dataset, explores its structure, and cleans it.

    Returns:
        pandas.DataFrame: The cleaned dataset.
    """
    try:
        # Load the Iris dataset from sklearn
        iris_data = load_iris()          # Load the Iris dataset as a Bunch object.  It contains data and metadata.

        # Convert the dataset into a DataFrame with feature names as column headers
        iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
        # Create a Pandas DataFrame.
        # data:  The actual data (the feature measurements).
        # columns:  The names of the features (e.g., 'sepal length (cm)').

        # Add a column for the target (species encoded as integers)
        iris_df['target'] = iris_data.target      # 'target' is a column with integer codes representing the species (0, 1, 2).

        # Map the target integers to actual species names as a categorical column
        iris_df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
        # Create a 'species' column with the actual species names ('setosa', 'versicolor', 'virginica').
        # pd.Categorical.from_codes():  A constructor to create a categorical variable.
        # iris_data.target:  The integer codes for the species.
        # iris_data.target_names:  The array of species names corresponding to the codes.

        # Display the first 5 rows of the dataset
        print("First 5 rows of the dataset:")
        print(iris_df.head(), "\n")      # Print the first 5 rows of the DataFrame.  The '\n' adds a newline for spacing.

        # Display structure and data types of the dataset
        print("Dataset information:")
        print(iris_df.info(), "\n")          # Print a summary of the DataFrame, including column names, data types, and non-null counts.
       

        # Check for missing values in each column
        print("Missing values per column:")
        print(iris_df.isnull().sum(), "\n")      # Print the number of missing values (NaN) in each column.
        # .isnull():  Returns a DataFrame of boolean values (True if a value is missing, False otherwise).
        # .sum():  Sums the boolean values for each column (True is treated as 1, False as 0), giving the count of missing values.

        # Drop rows with missing values (if any exist)
        iris_df = iris_df.dropna()      # Remove any rows that contain missing values.  In the Iris dataset, there are no missing values, so this doesn't change the data.

        # Display the first few rows after cleaning
        print("Dataset after cleaning (dropping missing values):")
        print(iris_df.head(), "\n")      # Print the first 5 rows of the DataFrame after the (no) dropna() operation.

        # Return the cleaned DataFrame
        return iris_df          # Return the processed DataFrame.

    except Exception as e:
        # Print error message if an exception occurs
        print(f"An error occurred: {e}")      # Handle exceptions (errors) that might occur during the data loading or cleaning process.
        return None          # Return None to signal that an error occurred.

# Function to perform basic analysis on the dataset
def basic_data_analysis(df):
    """
    Performs basic analysis of the input DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.
    """
    if df is None:
        # Handle case where no data is provided
        print("Error: No data to analyze.")      # Print an error message if the input DataFrame is None.
        return          # Exit the function.

    try:
        # Display summary statistics for numeric columns
        print("Basic statistics of numerical columns:")
        print(df.describe(), "\n")      # Print descriptive statistics for all numerical columns.
        # .describe():  Computes statistics like mean, standard deviation, min, max, quartiles, etc.

        # Compute and display mean values grouped by species
        print("Mean of numerical columns grouped by species:")
        print(df.groupby('species', observed=True).mean(), "\n")      # Group the data by the 'species' column and calculate the mean of each numerical column for each species.
        # .groupby('species'):  Groups the DataFrame by the unique values in the 'species' column.
        # .mean():  Calculates the mean of the remaining numerical columns for each group.

        # Print interpretation of the dataset
        print("Patterns and findings:")
        print("- The dataset contains measurements for sepal length, sepal width, petal length, and petal width for three species of Iris.")
        print("- The describe() output shows statistical distribution of each feature.")
        print("- The groupby() output shows how species differ in each numerical feature.\n")
        #  This part just prints some text describing the data.

    except Exception as e:
        # Handle and print any exceptions during analysis
        print(f"An error occurred during analysis: {e}")      # Catch and print any exceptions that occur during the analysis.

# Function to create visualizations for the dataset
def data_visualization(df):
    """
    Creates four different types of visualizations using matplotlib, all in the same figure.

    Args:
        df (pd.DataFrame): The dataset to visualize.
    """
    if df is None:
        print("Error: No data to visualize.")
        return

    try:
        # Set seaborn style for cleaner aesthetics
        sns.set_style("whitegrid")    # Set the visual style of the plots to 'whitegrid'.  Seaborn enhances Matplotlib.

        # Create a 2x2 grid for the subplots
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        # Create a figure and a 2x2 grid of subplots.
        #  2, 2:  Specifies the number of rows and columns in the grid.
        #  figsize:  Sets the size of the entire figure (width, height) in inches.
        fig.suptitle('Iris Dataset Visualizations', fontsize=16, fontweight='bold', y=1.02)
        # Add a title to the entire figure.
        #  fontsize:  Size of the title text.
        #  fontweight:  Make the title bold.
        #  y:  Vertical position of the title (1.02 moves it slightly above the top of the subplots).

        # Line chart: Sepal length trend over time
        df['time'] = range(len(df))  # Add a time/index column
        # Create a new column 'time' that represents the index of each row (0, 1, 2, ...).  This is used as a proxy for time.
        axes[0, 0].plot(df['time'], df['sepal length (cm)'], marker='o', color='navy', linewidth=2)
        # Create a line plot in the top-left subplot (axes[0, 0]).
        #  df['time']:  The x-axis data (time).
        #  df['sepal length (cm)']:  The y-axis data (sepal length).
        #  marker='o':  Use circles as markers for the data points.
        #  color='navy':  Use navy blue for the line and markers.
        #  linewidth=2:  Set the thickness of the line.
        axes[0, 0].set_title('Sepal Length Over Time', fontsize=12)
        # Set the title of the subplot.
        axes[0, 0].set_xlabel('Time (Index)', fontsize=10)
        # Set the label for the x-axis.
        axes[0, 0].set_ylabel('Sepal Length (cm)', fontsize=10)
        # Set the label for the y-axis.
        axes[0, 0].grid(True)
        # Add a grid to the subplot.

        # Bar chart: Average petal length by species
        species_means = df.groupby('species', observed=True)['petal length (cm)'].mean()
        # Calculate the mean petal length for each species.
        #  df.groupby('species'): Group the data by the 'species' column.
        #  observed=True:  Use only the species that actually appear in the data.
        #  ['petal length (cm)'].mean():  Calculate the mean of the 'petal length (cm)' column for each species group.
        axes[0, 1].bar(species_means.index, species_means.values, color=['#ff9999','#66b3ff','#99ff99'])
        # Create a bar chart in the top-right subplot (axes[0, 1]).
        #  species_means.index:  The x-axis data (the species names).
        #  species_means.values:  The y-axis data (the mean petal lengths).
        #  color:  A list of colors for the bars.
        axes[0, 1].set_title('Average Petal Length per Species', fontsize=12)
        # Set the title of the subplot.
        axes[0, 1].set_xlabel('Species', fontsize=10)
        # Set the label for the x-axis.
        axes[0, 1].set_ylabel('Petal Length (cm)', fontsize=10)
        # Set the label for the y-axis.

        # Histogram: Sepal width distribution
        axes[1, 0].hist(df['sepal width (cm)'], bins=20, color='darkseagreen', edgecolor='black')
        # Create a histogram in the bottom-left subplot (axes[1, 0]).
        #  df['sepal width (cm)']:  The data for the histogram.
        #  bins=20:  Divide the data into 20 bins.
        #  color:  The color of the bars.
        # edgecolor:  The color of the bar edges.
        axes[1, 0].set_title('Distribution of Sepal Width', fontsize=12)
        # Set the title of the subplot.
        axes[1, 0].set_xlabel('Sepal Width (cm)', fontsize=10)
        # Set the label for the x-axis.
        axes[1, 0].set_ylabel('Frequency', fontsize=10)
        # Set the label for the y-axis.

        # Scatter plot: Sepal length vs Petal length colored by species
        colors = {'setosa': 'crimson', 'versicolor': 'darkorange', 'virginica': 'dodgerblue'}
        # Define a dictionary to map species names to colors.
        for species in df['species'].unique():
            # Iterate over the unique species names.
            subset = df[df['species'] == species]
            # Create a subset of the DataFrame containing only the data for the current species.
            axes[1, 1].scatter(subset['sepal length (cm)'], subset['petal length (cm)'],
                               label=species, color=colors[species], edgecolors='black', s=50)
            # Create a scatter plot in the bottom-right subplot (axes[1, 1]) for the current species.
            #  subset['sepal length (cm)']:  The x-axis data (sepal length for the current species).
            #  subset['petal length (cm)']:  The y-axis data (petal length for the current species).
            #  label:  The label for the species (used in the legend).
            #  color:  The color for the data points, taken from the 'colors' dictionary.
            #  edgecolors:  The color of the marker edges.
            #  s:  The size of the markers.
        axes[1, 1].set_title('Sepal vs Petal Length by Species', fontsize=12)
        # Set the title of the subplot.
        axes[1, 1].set_xlabel('Sepal Length (cm)', fontsize=10)
        # Set the label for the x-axis.
        axes[1, 1].set_ylabel('Petal Length (cm)', fontsize=10)
        # Set the label for the y-axis.
        axes[1, 1].legend(title='Species')
        # Add a legend to the subplot, with the title 'Species'.
        axes[1, 1].grid(True)
        # Add a grid to the subplot.

        # Make layout tight to avoid overlap
        plt.tight_layout()
        # Adjust the spacing between subplots to prevent overlapping of titles and labels.
        plt.subplots_adjust(top=0.92)  # Adjust top spacing for title
        # Adjust the top margin of the figure to make space for the main title.
        plt.show()      # Display the entire figure with all four subplots.

    except Exception as e:
        # Handle and print any exceptions during visualization
        print(f"An error occurred during visualization: {e}")      # Catch and print any errors during the visualization process.

# Main program execution
if __name__ == "__main__":
    iris_df = load_and_explore_data()     # Load and clean data
    # Call the load_and_explore_data() function to load and preprocess the Iris dataset, and store the resulting DataFrame in iris_df.
    basic_data_analysis(iris_df)          # Analyze data
    # Call the basic_data_analysis() function to perform basic statistical analysis on the DataFrame.
    data_visualization(iris_df)           # Visualize data
    # Call the data_visualization() function to create and display visualizations of the data.
