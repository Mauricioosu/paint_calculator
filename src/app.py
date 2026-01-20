import streamlit as st
import time
from core import calcular_tinta
import database as db

# Configuração Inicial
st.set_page_config(page_title="Sistema Multi-Tools", page_icon="🛠️")

# Inicializa o Banco de Dados ao abrir o app
db.init_db()

# Gerenciamento de Sessão
if 'logado' not in st.session_state:
    st.session_state['logado'] = False
if 'usuario' not in st.session_state:
    st.session_state['usuario'] = ""


# Funções de Interface
def tela_login():
    st.title("🔐 Acesso ao Sistema")
    tab1, tab2 = st.tabs(["Login", "Cadastrar-se"])
    with tab1:
        st.subheader("Entrar")
        username = st.text_input("Usuário", key="login_user")
        password = st.text_input("Senha", type="password", key="login_pwd")
        if st.button("Entrar", type="primary"):
            if db.verificar_login(username, password):
                st.session_state['logado'] = True
                st.session_state['usuario'] = username
                st.success("Login realizado com sucesso!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos.")

    with tab2:
        st.subheader("Novo Cadastro")
        new_user = st.text_input("Escolha um usuário", key="new_user")
        new_pwd = st.text_input("Escolha uma senha", type="password", key="new_pwd")
        confirm_pwd = st.text_input("Confirme a senha", type="password")
        if st.button("Criar Conta"):
            if new_pwd != confirm_pwd:
                st.warning("As senhas não coincidem.")
            elif len(new_pwd) < 4:
                st.warning("A senha deve ter pelo menos 4 caracteres.")
            else:
                if db.criar_usuario(new_user, new_pwd):
                    st.success("Conta criada! Faça login na aba ao lado.")
                else:
                    st.error("Este nome de usuário já está em uso.")


def sistema_principal():
    # Sidebar com Logout
    with st.sidebar:
        st.write(f"Olá, **{st.session_state['usuario']}**!")
        if st.button("Sair / Logout"):
            st.session_state['logado'] = False
            st.rerun()
        st.divider()
        menu = st.radio("Ferramentas", ["Calculadora de Tinta", "Calculadora de IMC"])

    # Roteamento das Ferramentas
    if menu == "Calculadora de Tinta":
        renderizar_tinta()
    elif menu == "Calculadora de IMC":
        st.title("⚖️ Calculadora de IMC")
        st.info("Módulo em desenvolvimento...")


def renderizar_tinta():
    st.title("🎨 Calculadora de Tinta")
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    altura = c1.number_input("Altura (m)", min_value=0.1, format="%.2f")
    largura = c2.number_input("Largura (m)", min_value=0.1, format="%.2f")
    rendimento = c3.number_input("Rendimento (m²/lata)", min_value=0.1, value=10.0)

    if st.button("Calcular", type="primary"):
        try:
            res = calcular_tinta(altura, largura, rendimento)
            st.success(f"Você precisa de **{res['latas_necessarias']}** latas.")
            with st.expander("Ver detalhes"):
                st.write(f"Área Total: {res['area']:.2f} m²")
                st.write(f"Cálculo Exato: {res['latas_exatas']:.2f} latas")
        except ValueError as e:
            st.error(str(e))


# Controlar o fluxo
def main():
    if st.session_state['logado']:
        sistema_principal()
    else:
        tela_login()


if __name__ == "__main__":
    main()
