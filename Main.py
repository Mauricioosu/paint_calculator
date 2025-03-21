"""
Calcula a quantidade de latas de tinta necessárias para pintar uma área.

Args:
    altura (float): Altura da área em metros
    largura (float): Largura da área em metros
    rendimento (float): Rendimento da tinta em metros quadrados por lata

Returns:
    float: Quantidade de latas necessárias
"""

def calcular_tinta(altura, largura, rendimento):

    try:
        area = altura * largura
        latas = area / rendimento
        
        # Arredonda para cima, pois não se pode comprar fração de lata
        latas_arredondadas = round(latas + 0.4999, 2)
        
        print(f"Área a ser pintada: {area:.2f} metros quadrados")
        print(f"Serão necessárias aproximadamente {latas_arredondadas} latas de tinta")
        print(f"(Cálculo exato: {latas:.2f} latas)")
        
        return latas_arredondadas
    
    except ZeroDivisionError:
        print("Erro: O rendimento não pode ser zero!")
        return None
    except ValueError:
        print("Erro: Por favor, insira apenas números válidos!")
        return None

def main():
    # Loop para garantir entradas válidas
    while True:
        try:
            altura = float(input('Qual a ALTURA do local a ser pintado? (em metros): '))
            largura = float(input('Qual a LARGURA do local a ser pintado? (em metros): '))
            rendimento = float(input('Qual o rendimento da lata de tinta? (em m² por lata): '))
            
            # Verifica se os valores são positivos
            if altura <= 0 or largura <= 0 or rendimento <= 0:
                print("Erro: Os valores devem ser maiores que zero!")
                continue
            
            break
            
        except ValueError:
            print("Erro: Por favor, insira um número válido!")
    
    calcular_tinta(altura, largura, rendimento)
    
if __name__ == "__main__":
    main()