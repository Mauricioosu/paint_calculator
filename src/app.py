import streamlit as st
import math


def calcular_necessidade_tinta(altura, largura, rendimento):
    if rendimento == 0:
        raise ValueError("Rendimento não pode ser zero.")
    area = altura * largura
    latas = area / rendimento
    # Substituindo o arredondamento manual do arquivo original por math.ceil
    # O original usava: round(latas + 0.4999, 2)
    latas_arredondadas = math.ceil(latas)
    return area, latas, latas_arredondadas


# UI
def main():
    st.set_page_config(page_title="Calculadora de Tinta", page_icon="🎨") 
    st.title("🎨 Calculadora de Tinta")
    st.markdown("Determine a quantidade exata de material para sua obra.")

    with st.sidebar:
        st.header("Parâmetros")
        altura = st.number_input("Altura (m)", min_value=0.1, format="%.2f")
        largura = st.number_input("Largura (m)", min_value=0.1, format="%.2f")
        rendimento = st.number_input("Rendimento (m²/lata)", min_value=0.1, value=10.0, format="%.2f")

    if st.button("Calcular Material", type="primary"):
        try:
            area, latas_exatas, latas_finais = calcular_necessidade_tinta(altura, largura, rendimento)   
            col1, col2, col3 = st.columns(3)
            col1.metric("Área Total", f"{area:.2f} m²")
            col2.metric("Latas (Exato)", f"{latas_exatas:.2f}")
            col3.metric("A Comprar", f"{latas_finais} un", delta="Arredondado", delta_color="inverse")      
            st.success(f"Você precisará comprar **{latas_finais}** latas de tinta.")
        except Exception as e:
            st.error(f"Erro no cálculo: {str(e)}")


if __name__ == "__main__":
    main()
