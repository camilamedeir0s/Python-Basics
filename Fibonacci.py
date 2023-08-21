def obter_quantidade_elementos():
    while True:
        try:
            quantidade_elementos = int(input("Digite a quantidade de elementos desejada: "))
            return quantidade_elementos
        except ValueError:
            print("Entrada inválida. Insira um número.")

def calcular_fibonacci(quantidade_elementos):
    elemento_anterior = 0
    elemento_atual = 1

    print("Sequência de Fibonacci:")
    for elemento in range(quantidade_elementos):
        if elemento == 0:
            print(elemento_anterior, end=' ')
        else:
            print(elemento_atual, end=' ')
            elemento_auxiliar = elemento_anterior + elemento_atual
            elemento_anterior = elemento_atual
            elemento_atual = elemento_auxiliar

def main():
    quantidade_elementos = obter_quantidade_elementos()
    calcular_fibonacci(quantidade_elementos)

if __name__ == "__main__":
    main()
