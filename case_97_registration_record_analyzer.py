incidents = [("INC-01", 5, 4, 3), ("INC-02", 4, 5, 5), ("INC-03", 3, 2, 5)]
ranked = []
for incident_id, severity, location_priority, frequency in incidents:
    score = 3 * severity + 2 * location_priority + frequency
    ranked.append([incident_id, severity, location_priority, frequency, score])
for i in range(len(ranked)):
    for j in range(0, len(ranked) - i - 1):
        if ranked[j][4] < ranked[j + 1][4]:
            ranked[j], ranked[j + 1] = ranked[j + 1], ranked[j]
print("Score = 3 x severity + 2 x location priority + frequency\n")
for rank, row in enumerate(ranked, start=1):
    print(f"  {rank}. {row[0]}  score {row[4]}  (severity {row[1]}, location {row[2]}, frequency {row[3]})")
if ranked:
    print(f"\nNext action: inspect {ranked[0][0]} first")
