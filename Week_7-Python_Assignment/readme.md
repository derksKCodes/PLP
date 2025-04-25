# Data Analysis and Visualization with Python

## Overview

This Python script performs data analysis and visualization on the Iris dataset using the `pandas`, `numpy`, `matplotlib`, and `seaborn` libraries. It loads the dataset, explores its structure, cleans it, performs basic statistical analysis, and generates four different visualizations:

1.  **Line Chart**:  Sepal length trend over time (using row number as a proxy for time).
2.  **Bar Chart**:  Average petal length per species.
3.  **Histogram**:  Distribution of sepal width.
4.  **Scatter Plot**:  Relationship between sepal length and petal length, colored by species.

## Prerequisites

Make sure you have the following libraries installed:

-   `pandas`
-   `numpy`
-   `matplotlib`
-   `seaborn`
-   `scikit-learn`

You can install them using pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
UsageClone the repository (or download the script).Ensure you have the required libraries installed.Run the Python script:python your_script_name.py
Replace your_script_name.py with the actual name of the Python file.OutputThe script will:Print the first 5 rows of the dataset.Print the dataset information (number of rows, columns, data types).Print the number of missing values per column.Print the first 5 rows of the dataset after cleaning (dropping missing values, if any).Print descriptive statistics for the numerical columns.Print the mean values of the numerical columns grouped by species.Display four plots in a 2x2 grid:Sample OutputFirst 5 rows of the dataset:   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target    species
0                5.1             3.5              1.4             0.2       0  setosa
1                4.9             3.0              1.4             0.2       0  setosa
2                4.7             3.2              1.3             0.2       0  setosa
3                4.6             3.1              1.5             0.2       0  setosa
4                5.0             3.6              1.4             0.2       0  setosa
Dataset information:<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
sepal length (cm)    150 non-null float64
sepal width (cm)     150 non-null float64
petal length (cm)    150 non-null float64
petal width (cm)     150 non-null float64
target               150 non-null int64
species              150 non-null category
dtypes: category(1), float64(4), int64(1)
memory usage: 6.5 KB
Missing values per column:sepal length (cm)    0
sepal width (cm)     0
petal length (cm)    0
petal width (cm)     0
target               0
species              0
dtype: int64
Dataset after cleaning (dropping missing values):   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target    species
0                5.1             3.5              1.4             0.2       0  setosa
1                4.9             3.0              1.4             0.2       0  setosa
2                4.7             3.2              1.3             0.2       0  setosa
3                4.6             3.1              1.5             0.2       0  setosa
4                5.0             3.6              1.4             0.2       0  setosa
Basic statistics of numerical columns:       sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target
count         150.000000        150.000000         150.000000        150.000000   150.0
mean            5.843333          3.057333           3.758000          1.199333     1.0
std             0.828066          0.435866           1.765298          0.762238     0.8
min             4.300000          2.000000           1.000000          0.100000     0.0
25%             5.100000          2.800000           1.600000          0.300000     0.0
50%             5.800000          3.000000           4.350000          1.300000     1.0
75%             6.400000          3.300000           5.100000          1.800000     2.0
max             7.900000          4.400000           6.900000          2.500000     2.0
Mean of numerical columns grouped by species:             sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target
species
setosa                 5.006             3.428              1.462             0.246     0.0
versicolor             5.936             2.770              4.260             1.326     1.0
virginica              6.588             2.974              5.552             2.026     2.0

**Visualizations:**

![Screenshot 2025-04-25 135933](Week_7-Python_Assignment/Screenshot 2025-04-25 135933.png)
