"""

"Programa destinado a calcular a quantidade de tinta necessária para pintar uma parede.
O usuário informa o rendimento das latas de tinta e a altura e largura do que está pintando

"""

altura = float(input('Qual a ALTURA do local que esta sendo pintado? em metros: '))
largura = float(input('Qual a LARGURA do local que esta sendo pintado? em metros: '))
rendimento = float(input('Qual o rendimento da lata de tinta? em metros quadrados: '))

def resultado():
    calculado = (altura * largura)/rendimento
    print(f'Voce vai precisar de {calculado} latas de tinta')


resultado()


