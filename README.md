# Calculadora de Latas de Tinta

Este programa calcula a quantidade de latas de tinta necessárias para pintar uma área com base na altura e largura informadas pelo usuário, considerando também o rendimento da tinta (em metros quadrados por lata).

## Como Funciona

1. O usuário informa a **altura** e a **largura** da área a ser pintada, bem como o **rendimento** da tinta (quantos metros quadrados uma lata de tinta cobre).
2. O programa calcula a área total a ser pintada e, em seguida, determina a quantidade de latas necessárias para cobrir essa área, arredondando para cima, já que não é possível comprar frações de lata de tinta.
3. O programa trata casos de erro, como a entrada de valores não numéricos ou zero para o rendimento.

## Estrutura do Código

- **Função `calcular_tinta`**: Recebe os parâmetros de altura, largura e rendimento, calcula a área, determina a quantidade de latas necessárias e imprime o resultado.
- **Função `main`**: Controla a entrada de dados do usuário e valida se os valores inseridos são válidos.

## Exemplos de Uso

Ao executar o código, o usuário será solicitado a inserir as seguintes informações:

- **Altura** do local a ser pintado (em metros).
- **Largura** do local a ser pintado (em metros).
- **Rendimento** da tinta (em metros quadrados por lata).

Exemplo de saída:
```
Qual a ALTURA do local a ser pintado? (em metros): 5
Qual a LARGURA do local a ser pintado? (em metros): 8
Qual o rendimento da lata de tinta? (em m² por lata): 20
Área a ser pintada: 40.00 metros quadrados
Serão necessárias aproximadamente 2.0 latas de tinta
(Cálculo exato: 2.00 latas)
```

## Requisitos

Este código foi escrito em Python 3. Certifique-se de ter o Python instalado em sua máquina para executá-lo.

## Tratamento de Erros

- O programa verifica se os valores de **altura**, **largura** e **rendimento** são válidos (maiores que zero).
- Ele também trata entradas não numéricas e erros de divisão por zero.

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Salve o código em um arquivo com a extensão `.py`, por exemplo `Main.py`.
3. Execute o código no terminal ou prompt de comando:

   ```bash
   python Main.py
   ```

## Licença

Este código é de uso livre. Sinta-se à vontade para adaptá-lo e usá-lo conforme necessário.

---

Caso tenha dúvidas ou queira sugerir melhorias, sinta-se à vontade para contribuir com o projeto!