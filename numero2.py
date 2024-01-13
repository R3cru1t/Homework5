"""
Помилки (номери рядків через пробіл, цей рядок - 10 11 13 14 15): !!!
"""


def primes(a, b):
    """Повернути список простих чисел на відрізку від 'a' до 'b'."""
    res = []
    c = 0
    for i in range(a, b + 1):
        for j in range(i):
            if i % (j + 1) != 0:
                c += 1
                if c % 2 != 0 and c <= b:
                    res.append(c)

    return res

print(primes(1, 11))