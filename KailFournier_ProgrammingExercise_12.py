import numpy as np
import csv

# Read the grades.csv file
data = []
with open('grades.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        # Extract exam grades (columns 2, 3, 4) as integers
        grades = [int(row[2]), int(row[3]), int(row[4])]
        data.append(grades)

# Convert to NumPy array
data_array = np.array(data)

# Function to calculate statistics for a single array
def calculate_stats(arr, label):
    mean = np.mean(arr)
    median = np.median(arr)
    std_dev = np.std(arr)
    minimum = np.min(arr)
    maximum = np.max(arr)
    print(f"\n{label}:")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

# Calculate statistics for each student's grades (row)
print("Statistics for each student's grades:")
for i, row in enumerate(data_array):
    calculate_stats(row, f"Student {i+1}")

# Calculate statistics for the entire array (flattened)
flattened_data = data_array.flatten()
print("\nStatistics for all grades:")
calculate_stats(flattened_data, "All Grades")

# Calculate pass/fail counts for each exam
passing_score = 60
num_students = data_array.shape[0]
exam_names = ["Exam 1", "Exam 2", "Exam 3"]

print("\nPass/Fail Counts for Each Exam:")
for i in range(3):  # Iterate over each exam (column)
    exam_grades = data_array[:, i]
    passes = np.sum(exam_grades >= passing_score)
    fails = num_students - passes
    print(f"\n{exam_names[i]}:")
    print(f"Passed (≥ {passing_score}): {passes}")
    print(f"Failed (< {passing_score}): {fails}")

# Calculate overall pass percentage
total_grades = flattened_data.size
total_passes = np.sum(flattened_data >= passing_score)
pass_percentage = (total_passes / total_grades) * 100
print(f"\nOverall Pass Percentage Across All Exams: {pass_percentage:.2f}%")