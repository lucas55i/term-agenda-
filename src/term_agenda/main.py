from term_agenda.commands import (
    list_items,
    add_item,
    mark_done,
)

def menu():
    print("\n=== TERM AGENDA ===")
    print("1) Listar compromissos")
    print("2) Adicionar compromisso")
    print("3) Marcar como concluído")
    print("4) Sair")

    return input("Selecione uma opção: ").strip()

def flow_add():
    print("\nAdicionar compromisso")
    title = input("Título: ").strip()
    date = input("Data (YYYY-MM-DD): ").strip()
    time = input("Hora (HH:MM) [opcional]: ").strip()

    time = time if time else None
    add_item(title, date, time)
    print("✔ Compromisso adicionado com sucesso")

def flow_done():
    list_items()
    try:
        item_id = int(input("\nID do compromisso concluído: "))
        mark_done(item_id)
        print("✔ Compromisso marcado como concluído")
    except ValueError:
        print("ID inválido")

def main():
    while True:
        option = menu()

        if option == "1":
            list_items()

        elif option == "2":
            flow_add()

        elif option == "3":
            flow_done()

        elif option == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
