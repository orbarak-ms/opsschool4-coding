if __name__ == '__main__':
    import json

    with open('hw.json') as import_file:
        data = json.load(import_file)

    sorted_ages = data['buckets']
    people_list = data['ppl_ages']
    extra_age = [0, max(people_list.values()) + 1]
    sorted_ages.extend(extra_age)
    sorted_ages = sorted(sorted_ages)

    for i in range(len(sorted_ages) - 1):
        print(sorted_ages[i], "-", sorted_ages[i + 1], ":", sep="")
        for key in people_list:
            if people_list[key] >= sorted_ages[i]:
                if people_list[key] < sorted_ages[i + 1]:
                    print("  -", key)
