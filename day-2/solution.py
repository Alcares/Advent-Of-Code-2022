def calculate_round_score(enemy_shape, my_shape):
    if my_shape == "X":  # lose
        return points_per_outcome["lose"] + points_per_my_shape[lose_variants[enemy_shape]]
    if my_shape == "Y":  # draw
        return points_per_outcome["draw"] + points_per_my_shape[draw_variants[enemy_shape]]
    if my_shape == "Z":  # win
        return points_per_outcome["win"] + points_per_my_shape[win_variants[enemy_shape]]


with open("day_2_input.txt") as file:
    rounds = file.read().splitlines()
    print(rounds)

points_per_my_shape = {"X": 1, "Y": 2, "Z": 3}  # A, B, C    ||    X, Y, Z   ||  Rock, Paper, Sc
points_per_enemy_shape = {"A": 1, "B": 2, "C": 3}
points_per_outcome = {"lose": 0, "draw": 3, "win": 6}

win_variants = {"A": "Y", "B": "Z", "C": "X"}
lose_variants = {"A": "Z", "B": "X", "C": "Y"}
draw_variants = {"A": "X", "B": "Y", "C": "Z"}

total_points = 0

for round in range(len(rounds)):
    print(rounds[round])
    points = calculate_round_score(rounds[round][0], rounds[round][2])
    total_points += points

print(total_points)
