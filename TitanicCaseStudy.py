import csv
from pathlib import Path

data_folder = Path("/Users/gabor/Documents/Solent/5. év Masters/Computer Fundamentals/Python/")

file_to_open = data_folder / "titanic.csv"

records = []
print("Loading data...", end="")

f = open(file_to_open)
reader = csv.reader(f)
header = []
header = next(reader)

for row in reader:
  records.append(row)

f.close()
print(" Done!")
print(f"Successfully loaded {len(records)} records.")
