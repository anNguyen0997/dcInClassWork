# players = {'Jorge': 78,
#     'Fiona': 87,
#     'Carlos': 88,
#     'Jonothan': 84,
#     'Wes': 76,
#     'Jordan': 81,
#     'Matt': 79,
#     'Khanh': 80}

# top3 = {}


# for score in players.values():
#     # topScore = max(players.values())
#     print(score)
#     if score < topScore:

        

# Dez's Solution -----------------------
players = {
    'Kate' : 12,
    'Bill' : 3,
    'Joe' : 9,
    'Jackie' : 22,
    'Lin' : 18
}

def medalAssignment(players: dict) -> list:
    
    highestScores = sorted(players, key=players.get, reverse=True)
    
    print("Gold: ", highestScores[0])
    print("Silver: ", highestScores[1])
    print("Bronze: ", highestScores[2])
    
medalAssignment(players)