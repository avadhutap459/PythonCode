import pandas as pd

print("----------------------Print in table format-----------------")
data = {
    "ID": [101, 102, 103],
    "Name": ["Avadhut", "Rahul", "John"],
    "Department": ["IT", "HR", "IT"],
    "Salary": [100000, 80000, 120000]
}

df = pd.DataFrame(data)

print(df)

print("-----------------------------Datatype for df-----------------")

print(type(df))

print("---------------------View Specific Records Order From First-------------------")
print(df.head())
print(df.head(2))

print("---------------------View Specific Records Order From Last-------------------")
print(df.tail())
print(df.tail(2))


print("---------------------Shape-------------------")
print(df.shape)

print("---------------------Number Of Rows-------------------")

print(len(df))

print("---------------------Number Of Column-------------------")

print(df.shape[1])

print("---------------------Column Name-------------------")
print(df.columns)

print("---------------------Data Type-------------------")
print(df.dtypes)

print("---------------------Information-------------------")
print(df.info())

print("---------------------Describe-------------------")

print(df.describe())

print("---------------------Selecting Specific Column-------------------")

print(df["Name"])

print("---------------------Selecting Multiple Column-------------------")

result = df[
    ["Name", "Salary"]
]

print(result)

print("-----------------------Selecting a Row with loc---------------------")
print(df.loc[2])  # Label Base
print(df.loc[0, "Name"])

print("-----------------------Selecting Rows with iloc---------------------")
print(df.iloc[2]) # Index Base
print(df.iloc[0, 1])

print("-----------------------Filtering Data---------------------")
df = pd.DataFrame({
    "Name": ["Avadhut", "Rahul", "John"],
    "Salary": [100000, 80000, 120000]
})

result = df[df["Salary"] > 90000]

print(result)

result = df[
    (df["Name"] == "Avadhut") &
    (df["Salary"] > 90000)
]

print(result)

print("-----------------------Add new columns---------------------")

df["Bonus"] = df["Salary"] * 0.10

print(df)

print("-----------------------Modifiy columns---------------------")

df["Salary"] = df["Salary"] * 1.10

print(df)

print("-----------------------Rename columns---------------------")

df.rename(
    columns={
        "Name": "EmployeeName",
        "Salary": "AnnualSalary"
    },
    inplace=True
)

print(df)
print("-----------------------Delete columns---------------------")

df.drop(
    columns=["Bonus"],
    inplace=True
)

print(df)
print("-----------------------Add Rows---------------------")
new_employee = pd.DataFrame({
    "EmployeeName": ["Mike"],
    "AnnualSalary": [90000]
})

df = pd.concat(
    [df, new_employee],
    ignore_index=True
)
print(df)
print("-----------------------Remove Rows---------------------")
df.drop(
    index=0,
    inplace=True
)
print(df)

print("-----------------------Sorting---------------------")
df.sort_values(
    by="AnnualSalary"
)

print(df)

df.sort_values(
    by="AnnualSalary",
    ascending=False
)

print(df)

df.sort_values(
    by=["EmployeeName", "AnnualSalary"],
    ascending=[True, False]
)

print(df)

print("-------------------------Missing Values------------------")

df = pd.DataFrame({
    "EmployeeName": ["Avadhut", "Rahul", None],
    "AnnualSalary": [100000, None, 120000]
})

print(df.isnull())

print(df.isna())

print("----------------------Count Missing Values-------------------")

print(df.isnull().sum())

print("-----------------------------Remove Missing Rows------------")

df.dropna()

print(df)

print("-------------------------Fill Missing Values-------------------")

df["AnnualSalary"] = df["AnnualSalary"].fillna(0)

print(df)

print("------------------------Duplicate Records----------------")
print(df.duplicated())

print("---------------------Unique Values---------------------")
print(df["AnnualSalary"].unique())

print("-----------------------value_counts------------------------")
print(df["AnnualSalary"].value_counts())

print("---------------------------GroupBy-------------------------")
df = pd.DataFrame({
    "Department": [
        "IT", "IT", "HR", "HR", "Finance"
    ],
    "Salary": [
        100000, 120000, 80000, 90000, 110000
    ]
})

print(df)

result = df.groupby(
    "Department"
)["Salary"].mean()

print(result)

print("-------------------------Multiple Aggregations----------------")
result = df.groupby(
    "Department"
)["Salary"].agg(
    ["count", "mean", "min", "max"]
)

print(result)

print("------------------------GroupBy Multiple Columns-------------")
result = df.groupby(
    ["Department", "Salary"]
)["Salary"].mean()

print(result)

print("-----------------------------apply()----------------------")

def calculate_bonus(salary):
    return salary * 0.10

df["Bonus"] = df["Salary"].apply(
    calculate_bonus
)

print(df)

print("--------------------------Lambda------------------------")
df["SalaryCategory"] = df["Salary"].apply(
    lambda x: "High" if x >= 100000 else "Low"
)

print(df)

print("-----------------------Reading CSV------------------------")
df = pd.read_csv("employees.csv")

print("----------------------Writing CSV------------------------")
df.to_csv(
    "employees_output.csv",
    index=False
)

print("----------------------Reading Excel-------------------------")
df = pd.read_excel(
    "employees.xlsx"
)

print("------------------------Writing Excel-----------------------")
df.to_excel(
    "employees_output.xlsx",
    index=False
)

print("-----------------------Reading Json ---------------------------")
df = pd.read_json(
    "employees.json"
)

print("---------------------Writing Json----------------------------")
df.to_json(
    "employees.json",
    orient="records"
)

print("----------------------------Reading SQL-------------------------")
df = pd.read_sql(
    "SELECT * FROM Employees",
    connection
)

print("-----------------------Concat--------------------------")
df1 = pd.DataFrame({
    "Name": ["Avadhut", "Rahul"]
})

df2 = pd.DataFrame({
    "Name": ["John", "Mike"]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(result)

print("----------------------Merge-----------------------------")

employees = pd.DataFrame({
    "EmployeeID": [1, 2, 3],
    "Name": ["Avadhut", "Rahul", "John"]
})
departments = pd.DataFrame({
    "EmployeeID": [1, 2, 3],
    "Department": ["IT", "HR", "Finance"]
})
result = pd.merge(
    employees,
    departments,
    on="EmployeeID"
)

print("--------------------------SQL JOIN Comparison--------------------")

pd.merge(
    employees,
    departments,
    on="EmployeeID"
)  # SELECT * FROM Employees e INNER JOIN Departments d ON e.EmployeeID = d.EmployeeID;

print("--------------------------Join Types------------------------")
pd.merge(
    df1,
    df2,
    on="ID",
    how="inner"
)

print("----------------------Pivot Table---------------------")
result = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="mean"
)

print("---------------------Date Handling-------------")

df["Date"] = pd.to_datetime(
    df["Date"]
)
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

print("--------------------Filter Date--------------")

result = df[
    df["Date"] >= "2026-01-01"
]

print("------------------------String Operations-------------")
df["Name"] = df["Name"].str.upper()
df["Name"].str.lower()
df[
    df["Name"].str.contains(
        "Avadhut",
        case=False,
        na=False
    )
]

print("---------------Data Type Conversion----------------")
df["Salary"] = df["Salary"].astype(int)
df["EmployeeID"] = df["EmployeeID"].astype(str)
df["JoiningDate"] = pd.to_datetime(
    df["JoiningDate"]
)

print("--------------------Reset Index-------------------------")
df = df.reset_index(drop=True)

print("--------------------Set Index-------------------------")
df = df.set_index("EmployeeID")

print("--------------------Query--------------------------------")
result = df[
    df["Salary"] > 100000
]