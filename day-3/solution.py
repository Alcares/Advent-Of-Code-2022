def find_common_member(list1, list2):
    result = False

    for x in list1:
        for y in list2:
            if x == y:
                result = x
                return result

    return "#"

# scores = {"a": 1, "A": 27, "B", 28}
scores = {}
for _ in range(1, 27):
    scores[f"{chr(_ +96)}"] = _

for _ in range(1, 27):
    scores[f"{chr(_ +64)}"] = _ + 26

print(scores)

with open("advent_day3_input.txt") as f:
    backpacks = f.read().splitlines()

    for index, items in enumerate(backpacks):
        half_point = int(len(items)/2)
        first_compartment = items[0:half_point]
        second_compartment = items[half_point:]
        backpacks[index] = [first_compartment, second_compartment]

score = 0

for index, content in enumerate(backpacks):
    result = find_common_member(content[0], content[1])
    score += scores[result]

print(score)
