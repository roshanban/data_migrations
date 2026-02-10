# pandas note 
#---------------------------------------
# data load in  all format
#eda
# -missing 
# -duplicate 
# -discribe
#report generate 
# data sorting based on values
# and indexing wise sorting
# filter marks
# data convert or write one to many
# columns drop
# indexing


# Data load and separate 
# import pandas as pd
# airbnb_review_df = pd.read_csv('airbnb_last_review.tsv', nrows=5, sep='\t', parse_dates=['last_review'])
# filtering columns ----------
# schools_df = pd.read_csv('schools.csv', nrows=5, sep='|', usecols=[1,2,3,4,5], index_col=[1])

# Write CSV-------
# df.to_csv("output.csv", index=False)

# Write Excel
# df.to_csv("output.csv", index=False)

# Basic Data Exploration------------------
# df.head()      # first 5 rows
# df.tail()      # last 5 rows
# df.shape       # (rows, columns)
# df.columns     # column names
# df.info()      # data types + nulls
# df.describe()  # statistics

# Selecting Data-----------------------
# Select Column
# df["Age"]
# Multiple Columns-----
# df[["Name", "City"]]
# Select Row (index based)-----
# df.loc[0]
# Select specific rows & columns-----
# df.loc[0:2, ["Name", "Age"]]

# Filtering Data (VERY IMPORTANT)
# Simple condition
# df[df["Age"] > 26]
# Multiple conditions-----
# df[(df["Age"] > 25) & (df["City"] == "Kathmandu")]

# Using isin
# df[df["City"].isin(["Kathmandu", "Pokhara"])]

# Adding & Modifying Columns--------------
# Add new column
# df["Salary"] = [30000, 40000, 35000]
# Create column from existing------
# df["Age_after_5_years"] = df["Age"] + 5

# Conditional column
# df["Adult"] = df["Age"].apply(lambda x: "Yes" if x >= 18 else "No")

# Updating Values----------
# df.loc[df["Name"] == "Ram", "City"] = "Biratnagar"

# Deleting Columns & Rows-------------------
# Drop column
# df.drop("Salary", axis=1, inplace=True)
# Drop row
# df.drop(0, axis=0, inplace=True)

# Handling Missing Data (NULL / NaN)----------
# Check missing values
# df.isnull()
# df.isnull().sum()

# Fill missing values----------
# df.fillna(0)
# df.fillna(method="ffill")
# df.fillna(method="bfill")

# Drop missing rows
# df.dropna()

# Sorting Data---------
# df.sort_values(by="Age")
# df.sort_values(by="Age", ascending=False)

# GroupBy (VERY IMPORTANT)-------
# data = {
#     "Department": ["IT", "HR", "IT", "HR"],
#     "Salary": [50000, 40000, 60000, 45000]
# }
# df = pd.DataFrame(data)

# Group by department
# df.groupby("Department")["Salary"].mean()

# Multiple aggregations---------
# df.groupby("Department").agg(
#     avg_salary=("Salary", "mean"),
#     max_salary=("Salary", "max")
# )

# String Operations---------
# df["Name"].str.lower()
# df["Name"].str.upper()
# df["Name"].str.contains("ra")
# df["Name"].str.replace("Ram", "Ramesh")

# Date & Time-------
# df["Date"] = pd.to_datetime(df["Date"])
# df["Year"] = df["Date"].dt.year
# df["Month"] = df["Date"].dt.month
# df["Day"] = df["Date"].dt.day

# Merge & Join (Like SQL)
# pd.merge(df1, df2, on="id", how="inner")
# pd.merge(df1, df2, on="id", how="left")
# pd.merge(df1, df2, on="id", how="right")

# Concatenation-------
# pd.concat([df1, df2])
# pd.concat([df1, df2], axis=1)

# Apply, Map, Lambda--------
# df["Age"].apply(lambda x: x * 2)
# df["Gender"].map({"M": "Male", "F": "Female"})

# Value Counts-------
# df["City"].value_counts()
# df["City"].value_counts(normalize=True)

# Pivot Table-----------
# pd.pivot_table(
#     df,
#     values="Salary",
#     index="Department",
#     aggfunc="mean"
# )
# melt-----------------------
# df_melt = df.melt(
#     id_vars=["Date"],
#     value_vars=["case_nep", "death_nep", "case_ind", "death_ind"],
#     var_name="Type",
#     value_name="Count"
# )

# print(df_melt)

# What is Melting?------>> Melting turns column headers into row values.
# What is Pivoting?------->> Pivoting spreads row values into columns.
# pivot_table() handles duplicates
# Melt to analyze, Pivot to present------

# categorial data in pandas























