import pandas as pd


print("--------------------Pandas Series------------------")
numbers = pd.Series([10, 20, 30, 40])

print(numbers)

print("---------------------Custom Index------------------")
numbers1 = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)

print(numbers1)