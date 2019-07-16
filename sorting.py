# For fun mini-project
# Mateusz Kolpa
# 2019-07-16
import random


def random_list(amount=50, rnge=(0, 10)):
    # This function provides a set of random numbers
    numbers = []
    for k in range(amount):
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


def predict(numbs):
    # This function predicts max amount of executions
    if len(numbs) > 0:
        highest = 0
        lowest = 0
        for num in numbs:
            if highest < num:
                highest = num
            if lowest > num:
                lowest = num
                
        num_range = highest-lowest
        if num_range > 0:
            factor = 1
            while 2**factor < num_range:
                factor += 1
            return factor

        else:
            return 1

    else:
        return 'Error, can\'t calculate for 0'


if __name__ == "__main__":
    rl = [random_list(amount=10000, rnge=(0, 32))]
    print('Raw numbers: ', rl)
    print('Max amount of loops: ', predict(rl[0]))

    i = 0
    while not is_sorted(merge(rl)):
        i += 1

        new_rl = []
        for nums in rl:
            for n in do_calculations(nums):
                new_rl.append(n)
        rl = new_rl
        print('Amount of shells: ', len(rl))

    print('----------------------------------------')
    print('Amount of loops done: ', i)
    print('Unmerged: ', rl)
    print('Merged: ', merge(rl))
    print('----------------------------------------')

'''
The amount of loops required to be done is highly dependent on the range of numbers
For example, for our x amount of numbers, that have lowest number of 5 and highest of 37, we can subtract
5 from 37, so we have 32. So to calculate the amount of loops, we'll execute we have to find it's higher or equal
power of 2. 


 - So for 32(37-5):
2**5 = 32. So we'll execute the loop 5 times or less. It's gonna be more precise if amount of numbers will be
higher or lower.

 - Another example, 70(80-10):
2**6 = 64, but 64 is less than 70. The number has to be equal to or smaller than the factor of 2.
So 2**7 = 128. And 7 is the amount of max required executions of the loop.


There are some exceptions, for small amount of numbers, there might appear some bugs, but for bigger, like 10'000 or
100'000 there are none(almost)
For example (amount=100, rnge=(0, 32))
'''
