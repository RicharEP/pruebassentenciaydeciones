def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
