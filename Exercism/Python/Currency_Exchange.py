#Estimar o valor depois da troca
def exchange_money(budget, exchange_rate):
    exchanged_currency = budget / exchange_rate
    return exchanged_currency

#Calcular a moeda restante após uma troca
def get_change(budget, exchanging_value):
    money_left = budget - exchanging_value
    return money_left

#Calcular o valor das notas
def get_value_of_bills(denomination, number_of_bills):
    total_value_of_bills = number_of_bills * denomination
    return total_value_of_bills

#Calcular o número de notas
def get_number_of_bills(amount, denomination):
    number_of_currency_bills = amount // denomination
    return number_of_currency_bills

#Calcular quanto sobrou após a troca de moedas
def get_leftover_of_bills(amount, denomination):
    leftover_amount = amount % denomination
    return leftover_amount

#Descobrir o valor depois da troca
def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_decimal = spread / 100  #Convertendo o Spread Decimal
    effective_exchange_rate = exchange_rate * (1 + spread_decimal) #Calculando a taxa efetiva de troca
    max_value = int(budget / effective_exchange_rate) #Valor máximo na nova moeda
    max_value = max_value - (max_value % denomination) #Ajuste pela Denominação
    return max_value


