import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_csv("all_stocks_5yr.csv")
dfv2 = pd.read_csv("all_stocks_5yr.csv")

print("\t\t\t--- To print the top and bottom 3 rows ---")
print(df.head(3))
print(df[["date","Name","high"]].tail(3))

print("\n\t\t\t --- To print specific rows based off integer index location ---")
print(df.iloc[150000:150003])

print("\n\t\t\t --- Print based of context from specific row ---")
print(df.loc[df["date"] == "2018-01-02"])

print("\n\t\t\t --- To create a new column based off existing data ---")
df["Close Volume Total"] = df["close"] * df["volume"]
print(df.head(3))
# df.to_csv("new data")

print("\n\t\t\t--- Filtering data based on a conditional test --- ")
temp_df= dfv2.loc[    (dfv2["close"] > 1000)        &
                    (dfv2["volume"] > 5000000)    &
                    (dfv2["Name"] != "AAL")       ]
print(temp_df)


print("\n\t\t\t--- Calculating aggregates ---")
print(dfv2.groupby(["Name"]).mean())


print("\n\t\t\t--- Plotting data in matplotlib ---")
# import matplotlib
import matplotlib.pyplot as plt
# create new df consisting on only AAL stock
new_df = (df.loc[df["Name"] == "AAL"])
# save new df as AAL Stocks
new_df.to_csv("AAL_Stocks.csv")
# set x and y axis
x = new_df["date"]
y = new_df["close"]
# plot x and y axis
plt.plot(x,y)
plt.title("AAL 5 Year Close Stock Price", fontsize=24)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Close Value", fontsize =14)
# hide axis as to not lag computer
plt.axis(False)
# print graph
plt.show()