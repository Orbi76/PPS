def started(msg=""):
    print("-------------------------------------------------------------------------------------")
    print(f"Operation started: {msg}...\n")


def completed():
    print("")
    print("Operation completed.")
    print("-------------------------------------------------------------------------------------")

def error(msg):
    print(f"Error! {msg}!")


def menu():
    print(f"Please select on of the following options:")
    print(f"[years]    List unique years")
    print(f"[tally]    Tally up medals")
    print(f"[ctally]    Tally up medals for each team")
    print(f"[exit]    Exit the program")
    response = input()
    print(f"Your selection: {response} ")

tally = {
        "Gold": "13372",
        "Silver": "222",
        "Bronze": "3333"
    }

team_tally = {
"Country1": {"Name": "United Kingdom", "Gold": 10, "Silver": 5, "Bronze": 2},
"Country2": {"Name": "Germany", "Gold": 15, "Silver": 16, "Bronze": 17},
"Country3": {"Name": "Hungary", "Gold": 20, "Silver": 50, "Bronze": 200}
}


def display_medal_tally(tally):
    numberOfGoldMedals = tally.get("Gold")
    numberOfSilverMedals = tally.get("Silver")
    numberOfBronzeMedals = tally.get("Bronze")

    print(f"| Gold       |  {numberOfGoldMedals}  |")
    print(f"| Silver     |  {numberOfSilverMedals}  |")
    print(f"| Bronze     |  {numberOfBronzeMedals}  |")

def display_team_medal_tally(team_tally):
    numberOfGoldMedals = team_tally.get("Gold")
    numberOfSilverMedals = team_tally.get("Silver")
    numberOfBronzeMedals = team_tally.get("Bronze")
    for i in team_tally:
        print(team_tally[i].get("Name"))
        print(f"\t\tGold:"+str(team_tally[i].get("Gold"))+", Silver:"+str(team_tally[i].get("Silver"))+", Bronze:"+str(team_tally[i].get("Bronze")))



started("ezt")
completed()
error("Hiba")
menu()
display_medal_tally(tally)
display_team_medal_tally(team_tally)