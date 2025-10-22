# ===============================================
# GERENCIADOR DE TAREFAS - Projeto Python CLI
# Autor: Rafaela Gurgel
# ===============================================

# Lista que vai armazenar todas as tarefas
tarefas = []

# ===============================================
# FUNÇÕES DO PROGRAMA
# ===============================================

def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista"""
    nome = input("Digite o nome da tarefa: ").strip()
    descricao = input("Digite a descrição: ").strip()
    prioridade = input("Defina a prioridade (baixa/média/alta): ").lower().strip()
    categoria = input("Informe a categoria (ex: trabalho, estudo, pessoal...): ").strip()

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }

    tarefas.append(tarefa)
    print(f"\n✅ Tarefa '{nome}' adicionada com sucesso!\n")


def listar_tarefas():
    """Lista todas as tarefas"""
    if not tarefas:
        print("\n📭 Nenhuma tarefa encontrada.\n")
        return

    print("\n📋 LISTA DE TAREFAS:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔️ Concluída" if tarefa["concluida"] else "⏳ Pendente"
        print(f"\n{i}. {tarefa['nome']} [{status}]")
        print(f"   Descrição: {tarefa['descricao']}")
        print(f"   Prioridade: {tarefa['prioridade'].capitalize()}")
        print(f"   Categoria: {tarefa['categoria'].capitalize()}")


def marcar_concluida():
    """Marca uma tarefa como concluída"""
    listar_tarefas()
    try:
        num = int(input("\nDigite o número da tarefa que deseja marcar como concluída: "))
        tarefa = tarefas[num - 1]
        tarefa["concluida"] = True
        print(f"\n✅ Tarefa '{tarefa['nome']}' marcada como concluída!\n")
    except (ValueError, IndexError):
        print("\n Número inválido.\n")


def exibir_por_prioridade():
    """Filtra tarefas por prioridade"""
    prioridade = input("Digite a prioridade desejada (baixa/média/alta): ").lower().strip()
    filtradas = [t for t in tarefas if t["prioridade"] == prioridade]

    if not filtradas:
        print("\n📭 Nenhuma tarefa com essa prioridade.\n")
        return

    print(f"\n📋 Tarefas com prioridade '{prioridade}':")
    for t in filtradas:
        status = "✔️" if t["concluida"] else "⏳"
        print(f" - {t['nome']} ({status}) | Categoria: {t['categoria']}")


def exibir_por_categoria():
    """Filtra tarefas por categoria"""
    categoria = input("Digite a categoria desejada: ").lower().strip()
    filtradas = [t for t in tarefas if t["categoria"].lower() == categoria]

    if not filtradas:
        print("\n📭 Nenhuma tarefa nessa categoria.\n")
        return

    print(f"\n📋 Tarefas da categoria '{categoria}':")
    for t in filtradas:
        status = "✔️" if t["concluida"] else "⏳"
        print(f" - {t['nome']} ({status}) | Prioridade: {t['prioridade']}")


def remover_tarefa():
    """Remove uma tarefa"""
    listar_tarefas()
    try:
        num = int(input("\nDigite o número da tarefa que deseja remover: "))
        tarefa = tarefas.pop(num - 1)
        print(f"\n🗑️ Tarefa '{tarefa['nome']}' removida!\n")
    except (ValueError, IndexError):
        print("\n Número inválido.\n")


# ===============================================
# MENU PRINCIPAL
# ===============================================

def menu():
    while True:
        print("""
===============================
📌 GERENCIADOR DE TAREFAS
===============================
1. Adicionar tarefa
2. Listar tarefas
3. Marcar tarefa como concluída
4. Exibir por prioridade
5. Exibir por categoria
6. Remover tarefa
7. Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            exibir_por_prioridade()
        elif opcao == "5":
            exibir_por_categoria()
        elif opcao == "6":
            remover_tarefa()
        elif opcao == "7":
            print("\n Saindo do gerenciador. Até mais!\n")
            break
        else:
            print("\n Opção inválida, tente novamente.\n")


# ===============================================
# EXECUÇÃO DO PROGRAMA
# ===============================================
if __name__ == "__main__":
    menu()
