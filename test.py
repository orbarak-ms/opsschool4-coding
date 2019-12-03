
def sum_positive_number(num_list):
    final_sum = 0
    for i in num_list:
        if i > 0:
            final_sum += i
    print(final_sum)


if __name__ == '__main__':
    list_of_numbers = [12, 1, -7, 23, 80, 214, -9]
    sum_positive_number(list_of_numbers)
