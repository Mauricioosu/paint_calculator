import streamlit as st
import sys
import os
from core import calcular_tinta

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


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
            resultado = calcular_tinta(altura, largura, rendimento)
            area = resultado["area"]
            latas_exatas = resultado["latas_exatas"]
            latas_finais = resultado["latas_necessarias"]
            col1, col2, col3 = st.columns(3)
            col1.metric("Área Total", f"{area:.2f} m²")
            col2.metric("Latas (Exato)", f"{latas_exatas:.2f}")
            col3.metric("A Comprar", f"{latas_finais} un", delta="Arredondado", delta_color="inverse")
            st.success(f"Você precisará comprar **{latas_finais}** latas de tinta.")
        except ValueError as ve:
            st.error(f"Erro de Validação: {str(ve)}")
        except Exception as e:
            st.error(f"Erro inesperado: {str(e)}")


if __name__ == "__main__":
    main()
