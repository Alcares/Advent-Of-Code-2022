def find_common_member(*args):
    unpacked_strings = args
    character_set = [set(string) for string in unpacked_strings]
    common_element = [character_set[i] & character_set[i + 1] for i in range(len(character_set) - 1)]
    return str(common_element)[3:4]


def create_score_map():
    mapping = {f"{chr(_ +96)}": _ for _ in range(1, 27)}
    mapping_part2 = {f"{chr(_ +64)}": _ + 26 for _ in range(1, 27)}
    mapping.update(mapping_part2)

    return mapping


def solution_1(mapping):
    with open("input.txt") as f:
        backpacks = f.read().splitlines()

        score = 0
        for index, line in enumerate(backpacks):
            half_point = len(line) // 2
            first_compartment = set(line[0:half_point])
            second_compartment = set(line[half_point:])
            common_member = find_common_member(first_compartment, second_compartment)
            score += score_map[common_member]

    return score


def solution_2(mapping):
    with open("input.txt") as f:
        backpacks = f.read().splitlines()
        group = []

        score = 0
        for index, line in enumerate(backpacks):
            group.append(line)
            if len(group) == 3:
                line1, line2, line3 = set(group.pop()), set(group.pop()), set(group.pop())
                badge = find_common_member(line1, line2, line3)
                badge_formatted = badge
                score += score_map[badge_formatted]

    return score


if __name__ == "__main__":
    score_map = create_score_map()
    print(solution_1(score_map))  
    print(solution_2(score_map))  

