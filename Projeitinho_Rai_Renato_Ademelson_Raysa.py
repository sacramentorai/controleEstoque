import os
import Manipulação
import ProdutoGeral

os.system("cls")

BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[0m'

class Moeda:
    def formatar(valor):
        return f"R${valor:,.2f}".replace(",", ".")


def cancelar_compra():
    os.system("cls")
    codigo = input("Código da compra a ser cancelada: ")
    compras = Manipulação.carregar_arquivo('compras.txt')
    novas_compras = [compra for compra in compras if not compra.startswith(codigo)]
    if len(compras) == len(novas_compras):
        print(f"{RED}Compra não encontrada.{RESET}")
    else:
        Manipulação.salvar_arquivo('compras.txt', novas_compras, sobrescrever=True)
        print(f"{GREEN}Compra cancelada com sucesso.{RESET}")

def cancelar_venda():
    os.system("cls")
    codigo = input("Código da venda a ser cancelada: ")
    vendas = Manipulação.carregar_arquivo('vendas.txt')
    novas_vendas = [venda for venda in vendas if not venda.startswith(codigo)]
    if len(vendas) == len(novas_vendas):
        print(f"{RED}Venda não encontrada.{RESET}")
    else:
        Manipulação.salvar_arquivo('vendas.txt', novas_vendas, sobrescrever=True)
        print(f"{GREEN}Venda cancelada com sucesso.{RESET}")

def saldo_financeiro():
    os.system("cls")
    produtos = Manipulação.carregar_arquivo('produtos.txt')
    compras = Manipulação.carregar_arquivo('compras.txt')
    vendas = Manipulação.carregar_arquivo('vendas.txt')

    total_investido = 0
    total_arrecadado = 0

    for produto in produtos:
        codigo, nome, descricao, preco_compra, preco_venda = produto.strip().split(";")
        qtd_comprada = sum(int(c.split(";")[3]) for c in compras if c.split(";")[1] == codigo)
        qtd_vendida = sum(int(v.split(";")[3]) for v in vendas if v.split(";")[1] == codigo)
        total_investido += qtd_comprada * float(preco_compra)
        total_arrecadado += qtd_vendida * float(preco_venda)
    
    lucro_total = total_arrecadado - total_investido
    print(f"{YELLOW}Total investido: {Moeda.formatar(total_investido)}{RESET}")
    print(f"{YELLOW}Total arrecadado: {Moeda.formatar(total_arrecadado)}{RESET}")
    print(f"{YELLOW}Lucro total: {Moeda.formatar(lucro_total)}{RESET}")

def autenticar():
    senha = "8787"
    tentativa = input(f"{YELLOW}Digite a senha para acessar o sistema: {RESET}")
    if tentativa == senha:
        return True
    else:
        print(f"{RED}Senha incorreta. Acesso negado.{RESET}")
        return False

def menu():
    if not autenticar():
        return
    
    while True:
        os.system("cls")
        frase = "Escolha uma opção"
        print(f"{YELLOW}┌─{'─' * 18}{frase.upper()}{'─' * 20}─┐{RESET}")
        print(f"{YELLOW}│ ┌─{'─' * 51}─┐ │{RESET}")
        print(f"{YELLOW}│ │ 1 - Cadastrar Produto          2 - Comprar Produto  │ │{RESET}")
        print(f"{YELLOW}│ │ 3 - Vender Produto             4 - Listar Produtos  │ │{RESET}")
        print(f"{YELLOW}│ │ 5 - Detalhar Produto           6 - Remover Produto  │ │{RESET}")
        print(f"{YELLOW}│ │ 7 - Atualizar Produto          8 - Cancelar Compra  │ │{RESET}")
        print(f"{YELLOW}│ │ 9 - Cancelar Venda            10 - Saldo Financeiro │ │{RESET}")
        print(f"{YELLOW}│ │ 11 - Sair                                           │ │{RESET}")
        print(f"{YELLOW}│ └─{'─' * 51}─┘ │{RESET}")
        print(f"{YELLOW}└─{'─' * 55}─┘{RESET}")

        opcao = input(f"{YELLOW}Digite sua escolha: {RESET}")

        if opcao == "1":
            ProdutoGeral.cadastrar_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "2":
            ProdutoGeral.comprar_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "3":
            ProdutoGeral.vender_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "4":
            ProdutoGeral.listar_produtos()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "5":
            ProdutoGeral.detalhar_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "6":
            ProdutoGeral.remover_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "7":
            ProdutoGeral.atualizar_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "8":
            cancelar_compra()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "9":
            cancelar_venda()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "10":
            saldo_financeiro()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "11":
            os.system("cls")
            print("Saindo...")
            break
        else:
            print(f"{RED}Opção inválida! Tente novamente.{RESET}")

menu()
