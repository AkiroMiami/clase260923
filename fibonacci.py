def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

try:
    n = int(input("Ingrese la cantidad de términos de la secuencia de Fibonacci que desea imprimir: "))
    if n <= 0:
        print("Por favor, ingrese un número positivo.")
    else:
        print("Secuencia de Fibonacci:")
        fib_sequence = fibonacci(n)
        print(fib_sequence)
except ValueError:
    print("Por favor, ingrese un número válido.")
