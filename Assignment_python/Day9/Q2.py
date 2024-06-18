# 2. Read the Editions data, create dictionary with line number as key and the number of words present in that line as value for the data.

import pandas as pd

file_path = r"C:\Users\ajayk\Downloads\employee_data\employee_data\Editions.txt"

df = pd.read_table(file_path, header=None)

print("****DATAFRAME****\n",df.head(5))
print("****DATAFRAME-SHAPE****\n",df.shape)

def Count(df):
    line_word_count = {}
    for index, row in df.iterrows():
        word_count = len(row.iloc[0].split())  # Count words in the first (and only) column of the row
        line_word_count[index + 1] = word_count  # Store the word count with line number
    return line_word_count

# Call the function and print the result
word_counts = Count(df)
print("****COUNT OF WORDS****\n",word_counts)
