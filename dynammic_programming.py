# fibonacci Recursive version
def fib(n: int):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# time complexity: O(2^n)
# -> each increment to the input, increases branches by factor of 2
# space complexity: O(0) as no memory is used

# fibonacci Dynamic Programming version
def fib_dynamic(n: int):
    if n <= 1:
        return fib[n]
    fib = []
    fib.insert(0, 1)
    fib.insert(1, 1)
    i = 2
    while i <= n:
        fib.insert(i, fib[i - 1] + fib[i - 2])
        i += 1
    return fib[n]


# time complexity: O(n) as while loop executes at max n - 1 times
# space complexity: O(n) as function must store at most n + 1 values
