import CRUD_ID.Interecao.Entrada
import CRUD_ID.Consulta.Consultar
import os


def main():
    new_path = os.getcwd() + "\\dados_usuario.txt"
    texto = """
    [1] Adicionar informacoes
    [2] Consultar informacoes a partir do CPF
    """
    escolha = 5
    while escolha != 0:
        print(texto)
        escolha = int(input())
        if escolha == 1:
            CRUD_ID.Interecao.Entrada.insert(new_path)
        elif escolha == 2:
            CRUD_ID.Consulta.Consultar.consultar(new_path)


if __name__ == "__main__":
    main()
