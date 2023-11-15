with open("day_1_input.txt") as f:
    data = f.read().splitlines()
    for index, line in enumerate(data):
        if line == "":
            data[index] = "a"

    data_as_str = " ".join(data)
    data_final = data_as_str.split("a")

    sums = {}
    for index, line in enumerate(data_final):

        res = [eval(i) for i in data_final[index].strip().split(" ")]
        sums[f"{index}"] = sum(res)

    print(max(sums.values()))
    list_of_calories_summed_per_elf = list(sums.values())
    print(list_of_calories_summed_per_elf)
    sort_calories = sorted(list_of_calories_summed_per_elf)
    s1 = sort_calories[-1]
    s2 = sort_calories[-2]
    s3 = sort_calories[-3]

    print(s1+s2+s3)


    # with open("day_2_output.txt", "w") as files:
    #     files.write(data)
