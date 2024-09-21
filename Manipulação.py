BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[0m'

def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='UTF8') as f:
            return f.readlines()
    except:
        return []

def salvar_arquivo(nome_arquivo, dados, sobrescrever=False):
    try:
        modo = 'w' if sobrescrever else 'a+'
        with open(nome_arquivo, modo, encoding='UTF8') as f:
            f.writelines(dados)
    except Exception as e:
        print(f"{RED}Erro ao salvar o arquivo: {e}{RESET}")

def gerar_codigo(arquivo):
    registros = carregar_arquivo(arquivo)
    if registros:
        ultimo_registro = registros[-1].split(";")[0]
        return str(int(ultimo_registro) + 1)
    return "1"
