# For fun mini-project
# Mateusz Kolpa
# 2019-07-16

import math
import random


def random_list(amount=5, rnge=(0, 5)):
    numbers = []
    for i in range(amount):
        numbers.append(random.randrange(rnge[0], rnge[1]))
    return numbers


def sorted(numbers):
    for i in range(len(numbers)):
        if numbers[i] > numbers[min(i+1, len(numbers)-1)]:
            # If number in array lower is bigger than one higher, then return False
            return False
    return True


def do_calculations(lst):
    lst1 = []
    lst2 = []
    # if not sorted(lst) or len(lst) > 1:
    if sorted(lst):
        return [lst]
    else:
        avg = sum(lst) / len(lst)

        for num in lst:
            if num < avg:
                lst1.append(num)
            else:
                lst2.append(num)
        return [lst1, lst2]


def make_one_array(arrays):
    new_arrs = []
    for arr in arrays:
        for a in arr:
            new_arrs.append(a)
    return new_arrs


if __name__ == "__main__":
    rl = [random_list(amount=5000, rnge=(0, 100))]
    print(rl)

    for i in range(math.ceil(math.sqrt(len(rl[0])))):
        # For ex. [10, 5, 3, 5, 7, 1, 5, 2, 8, 3] -> len = 10
        # Then with 10 sqrt = 3.16
        # Then ceil(3.16) = 4
        # So the loop will be executed 4 times

        new_rl = []
        for nums in rl:
            for n in do_calculations(nums):
                new_rl.append(n)
        rl = new_rl

    rl = make_one_array(rl)
    print(rl)
