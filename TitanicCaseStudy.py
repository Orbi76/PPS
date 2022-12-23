import csv
from pathlib import Path

data_folder = Path("/Users/gabor/Documents/Solent/5. év Masters/Computer Fundamentals/Python/")

file_to_open = data_folder / "titanic.csv"
f = open(file_to_open)
