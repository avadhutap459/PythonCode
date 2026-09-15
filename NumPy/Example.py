
print("---------Without Numpy-----------")
numbers = [10, 20, 30, 40, 50]

result = []

for num in numbers:
    result.append(num * 2)

print(result)


print("---------------With Numpy List--------------")

import numpy as np

numbers = np.array([10,20,30,40,50])

result = numbers * 2

print(result)

print("--------------DataType using numpy--------")

print(type(result))

print("---------------With Numpy Tuple--------------")

numbers = np.array((1,2,3,4,5))

result = numbers * 2

print(result)

print("---------------With Numpy 2D-Array--------------")

print(np.array([[1,2,3],[4,5,6]]))


print("---------------With Numpy 3D-Array--------------")

print(np.array([[[1,2],[3,4]],[[5,6],[7,8]]]))


print("---------------With Numpy Find Dimension--------------")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.ndim)

print("---------------With Numpy Get Shape--------------")

print(arr.shape)

print("---------------With Numpy Get Size--------------")

print(arr.size)  # 3 * 2 = 6

print("---------------With Numpy Get DataType--------------")

print(arr.dtype)

print("---------------With Numpy Specific DataType--------------")

print(np.array([1,2,3],dtype=np.float64))

print("---------------With Numpy Print Zero--------------")

print(np.zeros(5))

print(np.zeros((3,2)))

print("---------------With Numpy Print One--------------")

print(np.ones(5))

print(np.ones((3,2)))

print("---------------With Numpy Fill Specific Value--------------")

arr = np.full((3, 3), 10)

print(arr)

print("---------------With Numpy Arrange--------------")
arr = np.arange(1, 10)

print(arr)

arr = np.arange(0, 20, 2)

print(arr)

print("---------------With Numpy linspace--------------")

arr = np.linspace(0, 10, 5)

print(arr)

print("---------------With Numpy Random--------------")

print(np.random.rand(5))

print(np.random.randint(1, 100, 5))

arr = np.random.randint(
    1,
    100,
    size=(3, 4)
)

print(arr)

print("---------------With Numpy Indexing--------------")

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])

print(arr[-1])

print("---------------With Numpy 2-D Indexing--------------")

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 1])

print("---------------With Numpy Slicing--------------")

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])

print("---------------With Numpy 2D Slicing--------------")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr[0:2])  # First 2 row

print(arr[:, 0:2]) # First 2 columns

print("---------------With Numpy Arithmetic Operations--------------")

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)

print(a - b)

print(a / b)

print("---------------With Numpy Scalar Operations--------------")

arr = np.array([10, 20, 30])

print(arr + 5)

print(arr * 10)


print("---------------With Numpy Mathematical Functions--------------")

arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))

print(np.power(arr, 2))

print(np.abs([-10, 20, -30]))

print(np.sum(arr))

print(arr.sum())

print(np.mean(arr))

print(np.min(arr))
print(np.max(arr))

print(np.std(arr))

print(np.median(arr))

print("---------------With Numpy Axis--------------")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.sum(arr)) # Sum Everything

print(np.sum(arr, axis=0)) # Sum Column

print(np.sum(arr, axis=1)) # Sum Row

print("---------------With Numpy Reshape--------------")

arr = np.arange(1, 7)

print(arr)

arr2 = arr.reshape(2, 3)

print(arr2)

print("---------------With Numpy Flatten--------------")
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = arr.flatten()

print(flat)

print("---------------With Numpy ravel--------------")

print( arr.ravel())

# flatten() generally returns a copy.
# ravel() generally returns a view when possible.

print("---------------With Numpy Transpose--------------")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T)

print("---------------With Numpy Concatenation--------------")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b))

print(result)

print("---------------With Numpy Stack--------------")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))

print(np.hstack((a, b)))

print("---------------With Numpy Splitting--------------")
arr = np.array([1, 2, 3, 4, 5, 6])

result = np.split(arr, 3)

print(result)

print("---------------With Numpy Boolean Filtering--------------")
arr = np.array([10, 25, 30, 45, 50])
result = arr[arr > 30]

print(result)

print("---------------With Numpy Multiple Conditions--------------")
result = arr[(arr > 20) & (arr < 50)]

print(result)

print("---------------With Numpy Where Conditions--------------")

arr = np.array([10, 20, 30, 40])

result = np.where(arr > 25, 1, 0)

print(result)

print("---------------With Numpy Sorting--------------")
arr = np.array([50, 10, 40, 20, 30])

print(np.sort(arr))

print("---------------With Numpy Unique Values--------------")
arr = np.array([10, 20, 10, 30, 20, 40])

print(np.unique(arr))

print("---------------With Numpy Searching--------------")
arr = np.array([10, 20, 30, 40])

index = np.where(arr == 30)

print(index)

print("---------------With Numpy Copy vs View--------------")

arr = np.array([1, 2, 3])

view = arr.view()

view[0] = 100

print(arr)

arr = np.array([1, 2, 3])

copy_arr = arr.copy()

copy_arr[0] = 100

print(arr)

print("---------------With Numpy Broadcasting--------------")
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr + 10)

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

row = np.array([10, 20, 30])

print(arr + row)

print("---------------With Numpy Matrix Multiplication--------------")

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

result = a @ b

print(result)

print(np.matmul(a, b))

print("---------------With Numpy Dot Product--------------")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))

print("---------------With Numpy Linear Algebra--------------")
matrix = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.det(matrix))
print(np.linalg.inv(matrix))

A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([8, 13])

solution = np.linalg.solve(A, B)

print(solution)


print("---------------With Saving NumPy Arrays--------------")

# np.save("data.npy", arr)
# arr = np.load("data.npy")
# np.savez("data.npz", numbers=arr)

print("--------------NumPy and CSV-------------------------")

# data = np.loadtxt("data.csv",delimiter=",")

# np.array()	Create array
# np.zeros()	Array of zeros
# np.ones()	Array of ones
# np.full()	Fill with value
# np.arange()	Range of values
# np.linspace()	Evenly spaced values
# np.random.rand()	Random floats
# np.random.randint()	Random integers
# np.reshape()	Change shape
# .flatten()	Convert to 1D copy
# .ravel()	Flatten, view when possible
# .T	Transpose
# np.concatenate()	Join arrays
# np.vstack()	Vertical stacking
# np.hstack()	Horizontal stacking
# np.split()	Split arrays
# np.sort()	Sort
# np.unique()	Unique values
# np.where()	Conditional selection
# np.sum()	Sum
# np.mean()	Average
# np.median()	Median
# np.std()	Standard deviation
# np.min()	Minimum
# np.max()	Maximum
# np.sqrt()	Square root
# np.abs()	Absolute value
# np.dot()	Dot product
# np.matmul()	Matrix multiplication
# np.linalg.solve()	Solve equations
# np.linalg.inv()	Matrix inverse
# np.save()	Save NumPy array
# np.load()	Load NumPy array
