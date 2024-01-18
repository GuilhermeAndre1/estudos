def is_armstrong_number(number):
#Converter o número em string para pegar os dígitos
    numero_string = str(number)
#Calcular the number of digits
    numero_de_digitos = len(numero_string)
#Calcular a soma de cada dígito elevado à potência do número de dígitos
    soma_armstrong = sum(int(digito) ** numero_de_digitos for digito in numero_string)
#Checar se a soma é igual ao número original
    return soma_armstrong == number