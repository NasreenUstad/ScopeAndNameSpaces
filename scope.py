def fact(n):
    """ Calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            print(f"{result} * {f}")
            result *= f

    return result


def factorial(n):
    """ Calculate n! recursively"""
    if n <= 1:
        print(1)
        return 1
    else:
        print(f"{n} * {n-1}")
        return n * factorial(n - 1)


print(fact(4))
print("-" * 30)
# factorial(5)
print(factorial(4))

# for i in range(6):
#     print(i)
#     factorial(i)
#     # print(f"{i}, {factorial(i)}")

