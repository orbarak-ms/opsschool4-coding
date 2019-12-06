import json

with open('hw.json', 'r') as data:
    obj = json.load(data)

ages = obj['ppl_ages']
bucket = obj['buckets']
oldest_age = max(ages.values())+1
bucket.append(oldest_age)
bucket.append(0)
sort_age = sorted(bucket)
number_of_buckets = len(sort_age)

def main():
    for i in range(number_of_buckets-1):
        print(sort_age[i],"-",sort_age[i+1],":", sep="")
        for key in ages:
            if ages[key] in range(sort_age[i],sort_age[i+1]):
                print("-",key)

if __name__ == '__main__':
    main()