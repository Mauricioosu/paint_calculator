import math


def calcular_tinta(altura: float, largura: float, rendimento: float) -> dict:
    """
    Calcula a necessidade de tinta de forma pura.
    Raises:
        ValueError: Se os inputs forem inválidos (<= 0).
    """
    if altura <= 0 or largura <= 0 or rendimento <= 0:
        raise ValueError("Valores devem ser maiores que zero.")

    area = altura * largura
    latas_exatas = area / rendimento
    latas_necessarias = math.ceil(latas_exatas)

    return {
        "area": area,
        "latas_exatas": latas_exatas,
        "latas_necessarias": latas_necessarias
    }
