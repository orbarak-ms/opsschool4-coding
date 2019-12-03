def ppl_older_than_30(ages):
    for name, age in ppl_ages.items():
        if age >= 30:
            print(name)

def print_ppl_age(ages):
    for name, age in ppl_ages.items():
        if age > 30:
            print(name +"is older than 30")
        elif age = 30:
            print(name + "is 30 years ols")
        elif age < 30:
            print(name + "is under 30")


if __name__ == '__main__':
    ppl_ages = {'david': 20, 'itzik': 30, 'yaron': 40, 'arie': 34}
    ppl_older_than_30(ppl_ages)

