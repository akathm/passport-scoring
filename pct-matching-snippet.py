### **This script is not ready for use**
### This file is intended to take inputs from a string array of all stamps achieved by a given Passport
### and return the % match which that stamp array has compared with all other stamp arrays 
### (i.e. a higher match, means a less unique stamp array).
### an example csv for input.csv can be found here: https://redash.grantsdata.xyz/queries/73/source
### This is an experimental feature for Passport scoring.

import csv

input_csv = 'input.csv'
output_csv = 'output.csv'

def calculate_match_percentage(string1, string2): ## need to iterate through all rows here...
    elements1 = set(string1.split(','))
    elements2 = set(string2.split(','))
    common_elements = elements1.intersection(elements2)
    match_percentage = (len(common_elements) / len(elements1)) * 100
    return f"{match_percentage:.2f}%"

rows = []
with open(input_csv, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    stamp_column_index = header.index('stamp_array')
    rows.append(header + ['match_percentage'])  # Append column header
    for row in reader:
        string_value = row[stamp_column_index]
        new_row = row + [calculate_match_percentage(string_value, string_value)]
        rows.append(new_row)

# Write the match_pct data to the output CSV
with open(output_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print(f"Match percentages appended to '{output_csv}' successfully.")
