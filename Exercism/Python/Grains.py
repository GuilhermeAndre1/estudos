#Quantos grãos existem em uma casa
def square(number):
    if 1 <= number <= 64:
        graos_casa = 2 ** (number - 1)
        return graos_casa
    else:
        raise ValueError("square must be between 1 and 64")
    
#Total de grãos no tabuleiro
def total():
    graos_totais = sum(2 ** i for i in range(64))
    return graos_totais
