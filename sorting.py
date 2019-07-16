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


def is_sorted(numbers):
    for j in range(len(numbers)):
        if numbers[j] > numbers[min(j+1, len(numbers)-1)]:
            # If number in array lower is bigger than one higher, then return False
            return False
    return True


def do_calculations(lst):
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
    return [lst1, lst2]asdfasdfasdfasdfasdf
    asdfasdf



def make_one_array(arrays):
    new_arrs = []
    for a in arrays:
        for b in a:
            new_arrs.append(b)
    return new_arrs


if __name__ == "__main__":
    rl = [random_list(amount=5000, rnge=(0, 100))]
    print(rl)

    for s in range(math.ceil(math.sqrt(len(rl[0])))):
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
