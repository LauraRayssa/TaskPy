
from tarefas import adicionar_tarefa, listar_tarefas



def exibir_menu():
    print("\n===== TASKPY =====")
    print("Gerenciador de Tarefas")
    print("----------------------")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")


def main():
    while True:
        exibir_menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            print("Funcionalidade em desenvolvimento!")

        elif opcao == "4":
            print("Funcionalidade em desenvolvimento!")

        elif opcao == "5":
            print("Encerrando o TaskPy. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
