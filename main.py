import csv
from pathlib import Path
import process
import tui


def read_data(file_path):
    tui.started(f"Reading data from {file_path}")

    data_folder = Path("/Users/gabor/Documents/Solent/5. év Masters/Computer Fundamentals/Python/")

    file_to_open = data_folder / file_path

    f = open(file_to_open)

    data = []

    reader = csv.reader(f)
    header = []
    header = next(reader)
    for row in reader:
        data.append(row)
    tui.completed()
    return data




def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
           process.list_years(athlete_data)
        elif selection == "tally":
            process.tally_medals(athlete_data)
        elif selection == "team":
            process.tally_team_medals(athlete_data)
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()