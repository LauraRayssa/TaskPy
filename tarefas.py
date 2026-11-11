
# Lista que armazena as tarefas durante a execução
tarefas = []


def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ").strip()

    if descricao == "":
        print("A descrição não pode estar vazia.")
        return

    tarefa = {
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(tarefa)

    print("Tarefa adicionada com sucesso!")


def listar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n===== MINHAS TAREFAS =====")

    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else " "
        print(f"[{indice}] [{status}] {tarefa['descricao']}")

    total = len(tarefas)
    concluidas = sum(tarefa["concluida"] for tarefa in tarefas)

    print(f"\nTotal: {total}")
    print(f"Concluídas: {concluidas}")
    print(f"Pendentes: {total - concluidas}")
