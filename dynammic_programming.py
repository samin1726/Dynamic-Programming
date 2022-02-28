import math

# dynamic programming: pattern of overlapping subproblems

# fibonacci Recursive version
def fib(n: int):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# fibonacci Dynamic Programming version
def fib_dynamic(n: int, memo=[]):
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib_dynamic(n - 1) + fib(n - 2)
    return memo[n]


# Say that you are a traveler on a 2-D grid, you being in the
# top left corner and your goal is to travel to the bottom-right
# corner. You may only move down or right. In how many ways can
# you travel to the goal on a grid with dimensions m * n.

# grid_traveler recursive version
def grid_traveler(r: int, c: int):
    if r == 0 or c == 0:
        return 0
    if r == 1 or c == 1:
        return 1
    return grid_traveler(r - 1, c) + grid_traveler(r, c - 1)


def grid_traveler_dynamic(r: int, c: int, memo={}):
    if r == 0 or c == 0:
        return 0
    if r == 1 or c == 1:
        return 1
    if (r, c) in memo or (c, r) in memo:
        return memo[(r, c)]

    memo[(r, c)] = grid_traveler_dynamic(r - 1, c, memo) + grid_traveler_dynamic(
        r, c - 1, memo
    )
    return memo[(r, c)]


# can_sum: can the target be reached by summing
# the elements in the given array, any number of times
# can_sum recursive version
def can_sum(a: list, target: int):
    if target == 0:
        return True
    if target < 0:
        return False
    i = 0
    result = []
    for element in a:
        result.insert(i, can_sum(a, target - element))
        i += 1
    if True in result:
        return True
    else:
        return False


def can_sum_dynamic(a: list, target: int, memo={}):
    if target == 0:
        return True
    if target < 0:
        return False
    if target in memo:
        return True
    i = 0
    result = []
    for element in a:
        result.insert(i, can_sum_dynamic(a, target - element, memo))
        i += 1
    if True in result:
        memo[target] = True
    else:
        memo[target] = False
    return memo[target]


# given a knapsack with a capacity, and items(with weights and values), find the
# maximum value of the items that can be put into the knapsack without
# exceeding the capacity.
# Example Notation for items: [[1,2],[2,3]] means the index 0th item has weigh 1 and value 2 and so on...
def knapsack(capacity, items, value=0, initial_value=0):
    if capacity == 0:
        return value
    if capacity < 0 or len(items) == 0:
        return initial_value
    i = 0
    result = []
    while i < len(items):
        item = items[i]
        items.pop(i)
        result.insert(i, knapsack(capacity - item[0], items, value + item[1], value))
        items.insert(i, item)
        i += 1
    return max(result)


def knapsack_dynamic(capacity, items, value=0, initial_value=0, memo={}):
    if capacity == 0:
        return value
    if capacity < 0 or len(items) == 0:
        return initial_value
    if capacity in memo:
        return memo[capacity]
    i = 0
    result = []
    while i < len(items):
        item = items[i]
        items.pop(i)
        result.insert(i, knapsack(capacity - item[0], items, value + item[1], value))
        items.insert(i, item)
        i += 1
    memo[capacity] = max(result)
    return memo[capacity]


# return the array of numbers from the given
# array of numbers (numbers can be repeated),
# that reaches the targetSum, and has the least cardinality
def best_sum(targetSum, numbers, array=[]):
    if targetSum == 0:
        return array
    if targetSum < 0:
        return []
    result = []
    for number in numbers:
        array2 = list(array)
        array2.append(number)
        result.append(best_sum(targetSum - number, numbers, array2))
    return max(result)


# return the longest increasing subsequence of
# the given array of numbers.
def LIS(array):
    if array == {}:
        return []
    if len(array) == 1:
        return array
    mid = math.floor(len(array) / 2)
    left = array[:mid]
    right = array[mid:]
    return merge_LIS(LIS(left), LIS(right))


# returns the longest increasing subsequence
# of the two given increasing subsequences
def merge_LIS(left, right):
    i = 0
    new_list = []
    while i < len(left):
        if left[i] <= right[0]:
            new_list.append(left[i])
            i += 1
        else:
            break
    new_list.extend(right)
    return new_list
