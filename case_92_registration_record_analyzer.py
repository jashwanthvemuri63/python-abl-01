teams = ["Team A", "Team B", "Team C", "Team D"]
schedule = [("Team A", "09:00", "Court 1"), ("Team B", "09:00", "Court 1"),
            ("Team A", "09:00", "Court 2")]
matches = [("Team A", "Team B", 2, 1), ("Team C", "Team D", 1, 1),
           ("Team A", "Team C", 0, 1), ("Team B", "Team D", 2, 0)]

print("Schedule conflicts:")
conflict_found = False
for i in range(len(schedule)):
    for j in range(i + 1, len(schedule)):
        if schedule[i][0] == schedule[j][0] and schedule[i][1] == schedule[j][1]:
            print(f"  {schedule[i][0]} is listed in two events at {schedule[i][1]}")
            conflict_found = True
if not conflict_found:
    print("  None")

points = [0, 0, 0, 0]
goals_for = [0, 0, 0, 0]
goals_against = [0, 0, 0, 0]
for home, away, home_goals, away_goals in matches:
    home_index = teams.index(home)
    away_index = teams.index(away)
    goals_for[home_index] += home_goals
    goals_against[home_index] += away_goals
    goals_for[away_index] += away_goals
    goals_against[away_index] += home_goals
    if home_goals > away_goals:
        points[home_index] += 3
    elif away_goals > home_goals:
        points[away_index] += 3
    else:
        points[home_index] += 1
        points[away_index] += 1

standings = []
for i in range(len(teams)):
    standings.append([teams[i], points[i], goals_for[i] - goals_against[i]])
for i in range(len(standings)):
    for j in range(0, len(standings) - i - 1):
        if (standings[j][1] < standings[j + 1][1] or
            (standings[j][1] == standings[j + 1][1] and standings[j][2] < standings[j + 1][2])):
            standings[j], standings[j + 1] = standings[j + 1], standings[j]

print("\nFinal ranking (points, then goal difference)")
for rank, row in enumerate(standings, start=1):
    point_label = "pt" if row[1] == 1 else "pts"
    print(f"  {rank}. {row[0]:<7} {row[1]} {point_label:<3} {row[2]:+d} GD")
