# For fun mini-project
# Mateusz Kolpa
# 2019-07-16
import random


def random_list(amount=50, rnge=(0, 10)):
    # This function provides a set of random numbers
    numbers = []
    for i in range(amount):
        numbers.append(random.randrange(rnge[0], rnge[1]))
    return numbers


def is_sorted(numbers):
    # Function that checks if numbers in given array are sorted
    for j in range(len(numbers)):
        if numbers[j] > numbers[min(j+1, len(numbers)-1)]:
            # If number in array lower is bigger than one higher, then return False
            return False
    return True


def do_calculations(lst):
    # This function makes new arrays
    if is_sorted(lst):
        return [lst]

    lst1 = []
    lst2 = []
    avg = sum(lst) / len(lst)

    for num in lst:
        if num < avg:
            lst1.append(num)
        else:
            lst2.append(num)
    return [lst1, lst2]


def merge(arrays):
    # This function merges the whole array of arrays to one single array
    new_arrs = []
    for a in arrays:
        for b in a:
            new_arrs.append(b)
    return new_arrs


if __name__ == "__main__":
    rl = [random_list(amount=100000, rnge=(0, 10000))]
    print(rl)

    i = 0

    while not is_sorted(merge(rl)):
        i += 1

        new_rl = []
        for nums in rl:
            for n in do_calculations(nums):
                new_rl.append(n)
        rl = new_rl
        print(f'Amount of shells: {len(rl)}')
        if is_sorted(merge(rl)):
            print('Break')

    print(f'Amount of loops done: {i}')
    print(merge(rl))
