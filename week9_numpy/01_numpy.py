# pip install numpy
# Import the numpy library
import numpy as np

# Create numpy arrays for height (in meters) and weight (in kilograms)
np_height = np.array([1.75, 1.80, 1.65, 1.90])
np_weight = np.array([70, 80, 60, 90])

# Calculate BMI: BMI = weight / height^2
bmi = np_weight / np_height ** 2
print(bmi)  # Print all BMI values

# Print BMI values greater than 23
print(bmi[bmi > 23])  # Boolean indexing in NumPy

# Check the type of the numpy array
print(type(np_height))  # Output: <class 'numpy.ndarray'>

# ---------------------------------------------
# 2D Numpy Arrays
# ---------------------------------------------

# Create a 2D numpy array with two rows
np_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Check the shape of the 2D array (rows, columns)
print(np_2d.shape)  # Output: (2, 3)

# Access specific elements
print(np_2d[0][2])      # Row 0, Column 2 → 3
print(np_2d[0, 1])      # Row 0, Column 1 → 2

# Slicing: All rows, Columns 1 to 2
print(np_2d[:, 1:3])    # Output: [[2 3] [5 6]]

# Access all columns of row 1
print(np_2d[1, :])      # Output: [4 5 6]

# ---------------------------------------------
# Practice with 2D Array: Baseball Stats
# ---------------------------------------------

# Each row contains [height, weight]
np_baseball = np.array([
    [1.80, 75],
    [1.85, 80],
    [1.70, 65],
    [1.95, 90]
])

# Get only the height data (first column)
np_height_in = np_baseball[:, 0]

# Print basic statistics on height
print(np.mean(np_height_in))   # Mean
print(np.median(np_height_in)) # Median

# Same statistics with labels
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Correlation between height and weight
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))  # 2x2 correlation matrix
