
# Program 7: Functional Data Filtering & Matrix Transformation Suite

def filter_matrix(matrix):
    return list(map(
        lambda row: list(filter(lambda x: x >= 0, row)),
        matrix
    ))


def transform_matrix(matrix):
    return list(map(
        lambda row: list(map(lambda x: x * 2, row)),
        matrix
    ))


def sort_tuples(data):
    return sorted(data, key=lambda x: x[1])


def flatten_matrix(matrix):
    return list(map(
        lambda x: x,
        [item for row in matrix for item in row]
    ))


# Input matrix
matrix = [
    [1, -2, 3],
    [-4, 5, 6],
    [7, -8, 9]
]

# Input tuple data
data = [(1, 30), (2, 10), (3, 20)]

# Function calls
filtered = filter_matrix(matrix)
transformed = transform_matrix(filtered)
sorted_data = sort_tuples(data)
flattened = flatten_matrix(filtered)

# Display results
print("Original Matrix:")
print(matrix)

print("\nMatrix after filtering negative values:")
print(filtered)

print("\nMatrix after transformation:")
print(transformed)

print("\nSorted Tuple Data:")
print(sorted_data)

print("\nFlattened Matrix:")
print(flattened)