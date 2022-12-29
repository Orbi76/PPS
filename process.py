import tui
"""
data2 = {"1111", "3333", "5555", "2222"}

data = ("4","Edgar Lindenau Aabye","M",34,"NA","NA","Denmark/Sweden","DEN","1900 Summer",1900,"Summer","Paris","Tug-Of-War","Tug-Of-War Men's Tug-Of-War","Gold",
"16","Juhamatti Tapio Aaltonen","M",28,184,85,"Finland","FIN","2014 Winter",2014,"Winter","Sochi","Ice Hockey","Ice Hockey Men's Ice Hockey","Bronze",
"17","Paavo Johannes Aaltonen","M",28,175,64,"Finland","FIN","1948 Summer",1948,"Summer","London","Gymnastics","Gymnastics Men's Individual All-Around","Bronze",
"17","Paavo Johannes Aaltonen","M",28,175,64,"Finland","FIN","1948 Summer",1948,"Summer","London","Gymnastics","Gymnastics Men's Team All-Around","Silver"
        )
"""

COL_MEDAL = 14
COL_TEAM = 6
COL_YEAR = 9

def list_years(data):
    tui.started("Listing years")
    yearR = set()
    for record in data:
        year = record[COL_YEAR]
        yearR.add(year)
    tui.display_years(yearR)
    tui.completed()

def tally_medals(data):
    tui.started("Tallying medals")

    tally = {
        "Gold": 0,
        "Silver": 0,
        "Bronze": 0
    }
    for row in data:
        medal = row[COL_MEDAL]
        if medal in ("Gold", "Silver", "Bronze"):
            tally[medal] += 1
    tui.display_medal_tally(tally)
    tui.completed()
"""
        if(row == "Gold"):
            numOfGold = tally.get("Gold")
            newNumOfGold = int(numOfGold) + 1
            tally.update({"Gold": newNumOfGold})
        if (row == "Silver"):
            numOfSilver = tally.get("Silver")
            newNumOfSilver = int(numOfSilver) + 1
            tally.update({"Silver": newNumOfSilver})
        if (row == "Bronze"):
            numOfBronze = tally.get("Bronze")
            newNumOfBronze = int(numOfBronze) + 1
            tally.update({"Bronze": newNumOfBronze})

"""


def tally_team_medals(data):
    tui.started("Tallying medals for each team")
    medal_tally = {}
    for record in data:
        team = record[COL_TEAM]
        medal = record[COL_MEDAL]

        if medal not in ("Gold", "Silver", "Bronze"):
            continue

        if team in medal_tally:
            medal_tally[team][medal] += 1
        else:
            medal_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            medal_tally[team][medal] += 1

    tui.display_team_medal_tally(medal_tally)
    tui.completed()
    """      
    result = dict()

    team_tally = {
        "United Kingdom": {"Gold": 10, "Silver": 5, "Bronze": 2},
        "Germany": {"Gold": 15, "Silver": 16, "Bronze": 17},
        "Hungary": {"Gold": 20, "Silver": 50, "Bronze": 200}
    }
    """



#tally_medals(data)
#list_years(data)

