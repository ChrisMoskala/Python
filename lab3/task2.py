import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("test.csv")
# print(df.to_string()) to show everything
# print(df)
# print(df.duplicated())
print(df.corr())
df["bill_amt_X"] = df.iloc[:, 6:11].sum(axis=1)
print(df)
df.head(10)
df2 = df[["limit_bal", "age", "education:1", "bill_amt_X"]]
df2.sort_values(by=["age"], ascending=False).head(10)
print(df2)
df.hist("limit_bal")
df.hist("age")
df.plot(kind="scatter", x="age", y="limit_bal")
plt.show()
