import os
import Manipulação

os.system("cls")

BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[0m'

class Moeda:
    def formatar(valor):
        return f"R${valor:,.2f}".replace(",", ".")


def cadastrar_produto():
    os.system("cls")
    produtos = Manipulação.carregar_arquivo('produtos.txt')
    codigo = Manipulação.gerar_codigo('produtos.txt')
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")

    while True:
        try:
            preco_compra = float(input("Preço de compra do produto: "))
            break
        except:
            print(f"{RED}Erro: Insira um valor numérico válido para o preço de compra.{RESET}")
    
    while True:
        try:
            preco_venda = float(input("Preço de venda do produto: "))
            break
        except:
            print(f"{RED}Erro: Insira um valor numérico válido para o preço de venda.{RESET}")

    produtos.append(f"{codigo};{nome};{descricao};{preco_compra};{preco_venda}\n")
    Manipulação.salvar_arquivo('produtos.txt', produtos, sobrescrever=True)
    print(f"{GREEN}Produto cadastrado com sucesso!{RESET}")

def remover_produto():
    os.system("cls")
    codigo = input("Código do produto a ser removido: ")
    produtos = Manipulação.carregar_arquivo('produtos.txt')
    novo_produtos = [p for p in produtos if not p.startswith(codigo)]
    
    if len(produtos) == len(novo_produtos):
        print(f"{RED}Produto não encontrado.{RESET}")
    else:
        Manipulação.salvar_arquivo('produtos.txt', novo_produtos, sobrescrever=True)
        Manipulação.salvar_arquivo('compras.txt', [c for c in Manipulação.carregar_arquivo('compras.txt') if not c.startswith(codigo)], sobrescrever=True)
        Manipulação.salvar_arquivo('vendas.txt', [v for v in Manipulação.carregar_arquivo('vendas.txt') if not v.startswith(codigo)], sobrescrever=True)
        print(f"{GREEN}Produto e seus registros de compras e vendas removidos com sucesso.{RESET}")

def atualizar_produto():
    os.system("cls")
    codigo = input("Código do produto a ser atualizado: ")
    produtos = Manipulação.carregar_arquivo('produtos.txt')
    for i, produto in enumerate(produtos):
        if produto.startswith(codigo):
            nome = input("Novo nome do produto: ")
            descricao = input("Nova descrição do produto: ")
            
            while True:
                try:
                    preco_compra = float(input("Novo preço de compra: "))
                    break
                except:
                    print(f"{RED}Erro: Insira um valor numérico válido para o preço de compra.{RESET}")

            while True:
                try:
                    preco_venda = float(input("Novo preço de venda: "))
                    break
                except:
                    print(f"{RED}Erro: Insira um valor numérico válido para o preço de venda.{RESET}")
            
            produtos[i] = f"{codigo};{nome};{descricao};{preco_compra};{preco_venda}\n"
            Manipulação.salvar_arquivo('produtos.txt', produtos, sobrescrever=True)
            print(f"{GREEN}Produto atualizado com sucesso.{RESET}")
            return
    print(f"{RED}Produto não encontrado.{RESET}")

def comprar_produto():
    os.system("cls")
    codigo = input("Código do produto: ")
    produtos = Manipulação.carregar_arquivo('produtos.txt')

    if not any(produto.startswith(codigo) for produto in produtos):
        print(f"{RED}Erro: Produto não encontrado.{RESET}")
        return

    data_compra = input("Data da compra: ")
    codigo_compra = Manipulação.gerar_codigo('compras.txt')

    while True:
        try:
            quantidade = int(input("Quantidade comprada: "))
            break
        except:
            print(f"{RED}Erro: Insira um valor numérico válido para a quantidade.{RESET}")

    compras = Manipulação.carregar_arquivo('compras.txt')
    compras.append(f"{codigo_compra};{codigo};{data_compra};{quantidade}\n")
    Manipulação.salvar_arquivo('compras.txt', compras, sobrescrever=True)
    print(f"{GREEN}Compra registrada com sucesso.{RESET}")

def vender_produto():
    os.system("cls")
    codigo = input("Código do produto a ser vendido: ")
    produtos = Manipulação.carregar_arquivo('produtos.txt')

    if not any(produto.startswith(codigo) for produto in produtos):
        print(f"{RED}Erro: Produto não encontrado.{RESET}")
        return

    data_venda = input("Data da venda: ")
    codigo_venda = Manipulação.gerar_codigo('vendas.txt')

    while True:
        try:
            quantidade = int(input("Quantidade a ser vendida: "))
            break
        except:
            print(f"{RED}Erro: Insira um valor numérico válido para a quantidade.{RESET}")

    compras = Manipulação.carregar_arquivo('compras.txt')
    vendas = Manipulação.carregar_arquivo('vendas.txt')

    qtd_comprada = sum(int(c.split(";")[3]) for c in compras if c.split(";")[1] == codigo)
    qtd_vendida = sum(int(v.split(";")[3]) for v in vendas if v.split(";")[1] == codigo)

    if quantidade > (qtd_comprada - qtd_vendida):
        print(f"{RED}Erro: Quantidade insuficiente para venda.{RESET}")
        return

    vendas.append(f"{codigo_venda};{codigo};{data_venda};{quantidade}\n")
    Manipulação.salvar_arquivo('vendas.txt', vendas, sobrescrever=True)
    print(f"{GREEN}Venda registrada com sucesso.{RESET}")

def listar_produtos():
    os.system("cls")
    produtos = Manipulação.carregar_arquivo('produtos.txt')
    compras = Manipulação.carregar_arquivo('compras.txt')
    vendas = Manipulação.carregar_arquivo('vendas.txt')
    
    if produtos:
        print(f"{YELLOW}Produtos cadastrados:\n{RESET}")
        for produto in produtos:
            codigo, nome, descricao, preco_compra, preco_venda = produto.strip().split(";")
            qtd_comprada = sum(int(c.split(";")[3]) for c in compras if c.split(";")[1] == codigo)
            qtd_vendida = sum(int(v.split(";")[3]) for v in vendas if v.split(";")[1] == codigo)
            preco_compra_formatado = Moeda.formatar(float(preco_compra))
            preco_venda_formatado = Moeda.formatar(float(preco_venda))
            
            print(f"{YELLOW}Código: {codigo}{RESET}")
            print(f"Nome: {nome}")
            print(f"Descrição: {descricao}")
            print(f"Preço Compra: {preco_compra_formatado}")
            print(f"Preço Venda: {preco_venda_formatado}")
            print(f"Quantidade Comprada: {qtd_comprada}")
            print(f"Quantidade Vendida: {qtd_vendida}\n")
    else:
        print(f"{RED}Nenhum produto cadastrado.{RESET}")

def detalhar_produto():
    os.system("cls")
    codigo = input("Código do produto: ")
    print("\n")
    produtos = Manipulação.carregar_arquivo('produtos.txt')
    compras = Manipulação.carregar_arquivo('compras.txt')
    vendas = Manipulação.carregar_arquivo('vendas.txt')

    for produto in produtos:
        if produto.startswith(codigo):
            codigo, nome, descricao, preco_compra, preco_venda = produto.strip().split(";")
            qtd_comprada = sum(int(c.split(";")[3]) for c in compras if c.split(";")[1] == codigo)
            qtd_vendida = sum(int(v.split(";")[3]) for v in vendas if v.split(";")[1] == codigo)
            valor_investido = qtd_comprada * float(preco_compra)
            valor_arrecadado = qtd_vendida * float(preco_venda)
            lucro = valor_arrecadado - valor_investido
            
            print(f"{YELLOW}Código do produto: {codigo}{RESET}")
            print(f"Nome do produto: {nome}")
            print(f"Descrição do produto: {descricao}")
            print(f"Preço de compra do produto: {Moeda.formatar(float(preco_compra))}")
            print(f"Preço de venda do produto: {Moeda.formatar(float(preco_venda))}")
            print(f"Quantidade Comprada: {qtd_comprada}")
            print(f"Quantidade Vendida: {qtd_vendida}")
            print(f"Valor total investido: {Moeda.formatar(valor_investido)}")
            print(f"Valor total arrecadado: {Moeda.formatar(valor_arrecadado)}")
            print(f"Lucro: {Moeda.formatar(lucro)}\n")

            print("Compras do produto:")
            for compra in compras:
                if compra.split(";")[1] == codigo:
                    print(f"  {compra.strip()}")

            print("\nVendas do produto:")
            for venda in vendas:
                if venda.split(";")[1] == codigo:
                    print(f"  {venda.strip()}")
            return
    print(f"{RED}Produto não encontrado.{RESET}")    