import csv
import random

# Open the CSV file and read its rows into a list
with open('phonies.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

# Shuffle the rows randomly
random.shuffle(rows)

# Open a new CSV file and write the shuffled rows into it
with open('shuffled_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)