
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
