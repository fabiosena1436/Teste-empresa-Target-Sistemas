
# Para a sequência de Fibonacci:
def fibonacci_check(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

numero = int(input("Digite um número: "))
if fibonacci_check(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci")