# python D:\Github\task_tracker\task_tracker.py

import argparse
import os

# Cria o objeto parser
parser = argparse.ArgumentParser(description="Exemplo de CLI simples")

# Analisa os argumentos
args = parser.parse_args()

# Lista de tarefas
tarefas = []

# Nome do arquivo onde as tarefas serão salvas
arquivo_tarefas = "tarefas.txt"

def carregar_tarefas():
    """
    Carrega as tarefas do arquivo texto 'tarefas.txt' se ele existir.
    Se o arquivo não existir, não faz nada.

    A função lê cada linha do arquivo e adiciona à lista 'tarefas' um dicionário
    contendo o nome e o status da tarefa.
    """
    if os.path.exists(arquivo_tarefas):
        with open(arquivo_tarefas, "r") as f:
            for linha in f:
                nome, status = linha.strip().split(" - ")
                tarefas.append({"nome": nome, "status": status})
        print("Tarefas carregadas com sucesso.")
    else:
        print("Nenhuma tarefa existente. Criando novo arquivo.")

def salvar_tarefas():
    """
    Salva as tarefas atuais no arquivo texto 'tarefas.txt'.

    A função escreve cada tarefa da lista 'tarefas' no arquivo, no formato:
    nome - status
    """
    with open(arquivo_tarefas, "w") as f:
        for tarefa in tarefas:
            f.write(f"{tarefa['nome']} - {tarefa['status']}\n")
    print("Tarefas salvas com sucesso.")

def adicionar_tarefa(nome, status="pendente"):
    """
    Adiciona uma nova tarefa à lista de tarefas e salva as alterações no arquivo.

    Parâmetros:
    nome (str): O nome da tarefa.
    status (str, opcional): O status da tarefa. Padrão é 'pendente'.

    A tarefa é adicionada à lista 'tarefas' e as alterações são salvas no arquivo.
    """
    tarefa = {"nome": nome, "status": status}
    tarefas.append(tarefa)
    salvar_tarefas()
    print(f"Tarefa '{nome}' adicionada com status '{status}'.")

def alterar_tarefa(indice, novo_nome=None, novo_status=None):
    """
    Altera o nome e/ou status de uma tarefa existente e salva as alterações.

    Parâmetros:
    indice (int): O índice da tarefa a ser alterada na lista.
    novo_nome (str, opcional): O novo nome da tarefa. Padrão é None, ou seja, não alterar.
    novo_status (str, opcional): O novo status da tarefa. Padrão é None, ou seja, não alterar.

    A função altera a tarefa correspondente ao índice fornecido e salva as alterações no arquivo.
    """
    if 0 <= indice < len(tarefas):
        if novo_nome:
            tarefas[indice]["nome"] = novo_nome
        if novo_status:
            tarefas[indice]["status"] = novo_status
        salvar_tarefas()
        print(f"Tarefa '{indice}' alterada.")
    else:
        print(f"Tarefa com índice {indice} não encontrada.")

def deletar_tarefa(indice):
    """
    Deleta uma tarefa da lista de tarefas e salva as alterações.

    Parâmetros:
    indice (int): O índice da tarefa a ser deletada na lista.

    A função remove a tarefa correspondente ao índice fornecido da lista 'tarefas'
    e salva as alterações no arquivo.
    """
    if 0 <= indice < len(tarefas):
        tarefa = tarefas.pop(indice)
        salvar_tarefas()
        print(f"Tarefa '{tarefa['nome']}' deletada.")
    else:
        print(f"Tarefa com índice {indice} não encontrada.")

def listar_tarefas(filtro_status=None):
    """
    Lista todas as tarefas ou apenas as tarefas com um status específico.

    Parâmetros:
    filtro_status (str, opcional): O status das tarefas a serem listadas ('pendente', 'em andamento', 'concluída').
    Se None, todas as tarefas são listadas.

    A função percorre a lista 'tarefas' e imprime as tarefas que correspondem ao status fornecido.
    """
    for i, tarefa in enumerate(tarefas):
        if filtro_status is None or tarefa["status"] == filtro_status:
            print(f"[{i}] {tarefa['nome']} - {tarefa['status']}")

def saida():
    """
    Verifica se o usuário deseja sair do programa.

    Retorna:
    bool: Retorna True se o usuário digitar 's', indicando que deseja sair.
    Caso contrário, retorna False.
    """
    sair = str(input("Deseja sair? [S / N]: ")).strip().lower()
    if sair == "s":
        return True
    return False

# Carrega as tarefas do arquivo
carregar_tarefas()

chave = False
while not chave:
    comando = input("Digite o comando> ").strip().lower()

    if comando == "criar":
        nome = input("Digite o nome da tarefa: ")
        status = input("Digite o status da tarefa (pendente/em andamento/concluída): ").strip().lower()
        adicionar_tarefa(nome, status)

    elif comando == "alterar":
        indice = int(input("Digite o índice da tarefa a ser alterada: "))
        novo_nome = input("Digite o novo nome da tarefa (ou deixe em branco para não alterar): ").strip()
        novo_status = input("Digite o novo status da tarefa (ou deixe em branco para não alterar): ").strip().lower()
        alterar_tarefa(indice, novo_nome or None, novo_status or None)

    elif comando == "deletar":
        indice = int(input("Digite o índice da tarefa a ser deletada: "))
        deletar_tarefa(indice)

    elif comando == "listar":
        listar_tarefas()

    elif comando == "filtrar":
        status = input("Digite o status para filtrar (pendente/em andamento/concluída): ").strip().lower()
        listar_tarefas(status)

    chave = saida()
