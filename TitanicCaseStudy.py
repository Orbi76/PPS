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

print("Please select one of the following options:")
print("[1] Display the names of all passengers")
print("[2] Display the number of passengers that survived")
print("[3] Display the number of passengers per gender")
print("[4] Display the number of passengers per age group")
response = int(input())
print(f"You have selected option: {response} ")

if (response == 1):
  print("The names of the passengers are...")
  passenger_name = []

  for record in records:
   # print(record[3])
    passenger_name.append(record[3])

 # print (*passenger_name,sep='\n')
  print ("\n".join(passenger_name))




