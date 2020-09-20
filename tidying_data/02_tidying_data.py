import pandas as pd

# extended column printing distance
#pd.set_option('display.max_rows', 500) # sets max number of rows
pd.set_option('display.max_columns', 500) # sets max numbers of columns
pd.set_option('display.width', 1000) # sets width of table

# From the Journal of Statistical Software
# Extract from Tidy Data by Hadley Wickham

# Five most common problems with messy datasets, along with their remedies:
# Column headers are values, not variable names.
# Multiple variables are stored in one column.
# Variables are stored in both rows and columns.
# Multiple types of observational units are stored in the same table.
# A single observational unit is stored in multiple tables.

# Source:http://vita.had.co.nz/papers/tidy-data.pdf

df = pd.read_csv("billboard.csv")

print("The file billboard.csv consists of columns that are values not variables")
print(df.head(3))

print("\nThe weeks data has been pivoted")
df_melt = pd.melt(
        df,
        id_vars=["year", "artist", "track", "time", "date.entered"],
        var_name = "week",
        value_name = "rating",
                        )
print(df_melt)
#df_melt.to_csv("billboard_melt.csv")

print("\nA problem with df_melt is that each week has been pivoted to have its own data row value")
# there for every given song there are 72 weeks of data and in total 24k datasets
print(df_melt.loc[df_melt["track"] =="Kryptonite"])

df_songs_with_duplicates = df_melt[["year", "artist", "track", "time"]] # this creates the df_songs from df_melt ...
# ... without columns date.entered, week or rating
print(df_songs_with_duplicates) # the df still has 24k rows

#df_songs_with_duplicates.to_csv("billboard_songs_with_duplicates.csv")

df_songs = df_songs_with_duplicates.drop_duplicates() # .drop_duplicates function removes duplicates
print(df_songs) # without duplicates there are now only 317 rows, down from 24k

# process of assigning each billboard song a unique id
df_songs.to_csv("billboard_songs_without_index.csv", index=False)
# adding an unique id to billboard dataframe caused errors due to clash with index values
# in order to combat this I created a new df without index values

df_id = pd.read_csv("billboard_songs_without_index.csv")

df_id["id"] = range(len(df_id))
# without indexing errors I use the following functions to assign range values for the new id column

print(df_id)

df_id.to_csv("billboard_songs_with_id.csv", index=False)


# here will will merge billboard_melt and billboard_songs_with_id
# the id column
df_ratings_with_duplicates = df_melt.merge(
    df_id, on=["year", "artist","track", "time"]
    )

print(df_ratings_with_duplicates)
#df_ratings_with_duplicates.to_csv("billboard_ratings_with_duplicates.csv")

# now I have the billboard.csv with ratings and id variables I can filter the ...
# ... columns I want, drop dublicates and save that data

df_ratings = df_ratings_with_duplicates[["id", "date.entered", "week", "rating"]] # dataset ready to be merged ...
# ... using nessary information
print(df_ratings)
df_ratings.to_csv("billboard_ratings_with_id.csv", index=False)

df_ratings_v2 = df_ratings_with_duplicates[["id","artist", "track", "time", "date.entered", "week", "rating"]]

print(df_ratings_v2)

df_ratings_v2.to_csv("billboard_clean.csv", index=False)