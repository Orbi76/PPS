
LINE_WIDTH = 85
def started(msg=""):
    output = f"Operation started: {msg}..."
    dashes = "-" * LINE_WIDTH
   # print("-------------------------------------------------------------------------------------")
    print(f"{dashes}\n {output}\n")


def completed():
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed.\n{dashes}\n")
   # print("-------------------------------------------------------------------------------------")

def error(msg):
    print(f"Error! {msg}\n")


def menu():
    print(f"""Please select on of the following options:
    {"[years]":<10} List unique years
    {"[tally]":<10} Tally up medals
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the program
    """)
    selection = input("Your selection: ")
    return selection.strip().lower()


"""
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
"""

def display_medal_tally(tally):
    numberOfGoldMedals = tally.get("Gold")
    numberOfSilverMedals = tally.get("Silver")
    numberOfBronzeMedals = tally.get("Bronze")

    print(f"| Gold       |  {numberOfGoldMedals}  |")
    print(f"| Silver     |  {numberOfSilverMedals}  |")
    print(f"| Bronze     |  {numberOfBronzeMedals}  |")

def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")
"""        
    numberOfGoldMedals = team_tally.get("Gold")
    numberOfSilverMedals = team_tally.get("Silver")
    numberOfBronzeMedals = team_tally.get("Bronze")
    
 
    for i in team_tally:
        print(team_tally[i].get("Name"))
        print(f"\t\tGold:"+str(team_tally[i].get("Gold"))+", Silver:"+str(team_tally[i].get("Silver"))+", Bronze:"+str(team_tally[i].get("Bronze")))
"""

#years = {"2022", "2021","2023", "2020"}

def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for row in sorted_years:
        print(row)

"""
started("ezt")
completed()
error("Hiba")
menu()
display_medal_tally(tally)
display_team_medal_tally(team_tally)
display_years(years)

"""
#menu()