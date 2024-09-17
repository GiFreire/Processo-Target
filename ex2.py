from sympy import false


def fibonacci(numero):
    if numero < 0 :
        return False
    x, y = 0, 1

    while x <= numero:
        if x == numero:
            return True
        x, y = y, x+y

    return False

numero = int(input("Digite um numero: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")