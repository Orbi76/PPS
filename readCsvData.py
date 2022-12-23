import csv
from pathlib import Path

data_folder = Path("/Users/gabor/Documents/Solent/5. év Masters/Computer Fundamentals/Python/")

file_to_open = data_folder / "song.csv"

f = open(file_to_open)

reader = csv.reader(f)
header = []
header = next(reader)

rows = []
reversed_rows = []

for row in reader:
  rows.append(row)
  reversed_rows.append(row[::-1])

print (header)
print (rows)
print(reversed_rows)

#print(list(reversed_rows))

#rows
#reversed_rows = reversed(rows)
#print (rows)
#print (reversed_rows)
#print(header)

"""
with open("song.csv", "a", newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Kicsi Gesztenye", "TNT", "pop", "2016"])
  
 """

# Ez beolvassa a filet és létrehoz egy új csv filet a beolvasott értékekkel és - jelet használ elkülönítőnek.
with open('song.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

  with open('new_song.csv','w') as new_file:
    csv_writer = csv.writer(new_file, delimiter='-')

    for line in csv_reader:
      #reverse a list using slicing operator
        csv_writer.writerow(line[::-1])
        
