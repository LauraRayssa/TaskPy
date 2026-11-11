
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


def concluir_tarefa():
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    listar_tarefas()

    try:
        numero = int(input("\nDigite o número da tarefa que deseja concluir: "))

        if 1 <= numero <= len(tarefas):
            tarefa = tarefas[numero - 1]

            if tarefa["concluida"]:
                print("\nEssa tarefa já está concluída!")
            else:
                tarefa["concluida"] = True
                print("\nTarefa concluída com sucesso!")
        else:
            print("\nNúmero de tarefa inválido.")

    except ValueError:
        print("\nDigite um número válido.")


def excluir_tarefa():
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    listar_tarefas()

    try:
        numero = int(input("\nDigite o número da tarefa que deseja excluir: "))

        if 1 <= numero <= len(tarefas):
            tarefa = tarefas[numero - 1]

            confirmacao = input(
                f"\nDeseja realmente excluir '{tarefa['descricao']}'? (s/n): "
            ).strip().lower()

            if confirmacao == "s":
                tarefas.pop(numero - 1)
                print("\nTarefa excluída com sucesso!")
            else:
                print("\nExclusão cancelada.")
        else:
            print("\nNúmero de tarefa inválido.")

    except ValueError:
        print("\nDigite um número válido.")
