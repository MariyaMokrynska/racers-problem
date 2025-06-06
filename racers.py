def non_winners(races):
    # Write your solution here!
    winners_set = set()
    all_racers_set = set()
    non_winners_set = set()
    for names in races.values():
        winners_set.add(names[0])
        for name in names:
            all_racers_set.add(name)
    non_winners_set = all_racers_set - winners_set
    return non_winners_set


races_1 = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}
assert non_winners(races_1) == {"Latifi", "Stroll"}

races_2 = {
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
}
assert non_winners(races_2) == {"Hamilton", "Tsunoda"}

races_3 = {
    "Monaco": ("Leclerc", "Verstappen", "Sainz"),
    "Barcelona": ("Sainz", "Verstappen", "Leclerc"),
    "Zandvoort": ("Verstappen", "Sainz", "Leclerc")
}
# If all drivers present in the dictionary won a race
# then the return value should be an empty set
assert non_winners(races_3) == set()

print("All tests passed! Discuss time/space complexity if time remains")
