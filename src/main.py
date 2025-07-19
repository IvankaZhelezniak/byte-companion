from colorama import init, Fore, Style
from difflib import get_close_matches                # ✅ Для інтелектуального аналізу команд
from data.storage import load_data, save_data
from address_book import (
    add_contact, edit_contact, delete_contact,
    search_contacts, show_all_contacts,
    birthdays_reminder, show_contacts_help
)
from notebook import (
    add_note,
    delete_note,
    edit_note,
    show_notes,
    find_note as search_notes,
    show_notes_help
)

# Ініціалізація colorama для коректного відображення кольорів у Windows
init(autoreset=True)

# ✅ Функція для підказки команди, якщо користувач зробив помилку у введенні
def suggest_command(user_input, commands):
    # Порівнює введену команду з допустимими
    # Повертає список схожих команд (найбільше 1 результат), які мають схожість ≥ 0.5
    matches = get_close_matches(user_input, commands, n=1, cutoff=0.5)

    # Якщо знайшлися схожі команди — повертаємо першу
    if matches:
        return matches[0]
    return None                  # Інакше повертаємо None (нічого не пропонувати)


# ✅ Функція реалізує режим роботи з контактами (address book)
def contacts_mode(book, notes):
    # Виводимо повідомлення про вхід у режим контактів
    print(Fore.YELLOW + "\n📒 Entering contacts mode " + Style.DIM + "(type 'help' for available commands)")
    # Список всіх допустимих команд у цьому режимі
    valid_commands = ['add', 'edit', 'delete', 'search', 'all', 'birthdays', 'help', 'back']
    while True:
        user_input = input(Fore.CYAN + "Enter command: ").strip().lower()

        if user_input == "back":
            print(Fore.BLUE + "↩️  Returning to main menu.")
            break
        elif user_input == "add":
            add_contact(book)
        elif user_input == "edit":
            edit_contact(book)
        elif user_input == "delete":
            delete_contact(book)
        elif user_input == "search":
            search_contacts(book)
        elif user_input == "all":
            show_all_contacts(book)
        elif user_input == "birthdays":
            birthdays_reminder(book)
        elif user_input == "help":
            show_contacts_help()
        else:
            suggestion = suggest_command(user_input, valid_commands)
            if suggestion:
                print(Fore.YELLOW + f"❓ Можливо ви мали на увазі '{suggestion}'?")
            else:
                print(Fore.RED + "❌ Unknown command. Type 'help' to see available commands.")

def notes_mode(book, notes):
    print(Fore.YELLOW + "\n📓 Entering notes mode " + Style.DIM + "(type 'help' for available commands)")
    valid_commands = ['add', 'edit', 'delete', 'list', 'search', 'help', 'back']
    while True:
        user_input = input(Fore.CYAN + "Enter command: ").strip().lower()

        if user_input == "back":
            print(Fore.BLUE + "↩️  Returning to main menu.")
            break
        elif user_input == "add":
            add_note(notes)
        elif user_input == "edit":
            edit_note(notes)
        elif user_input == "delete":
            delete_note(notes)
        elif user_input == "all":
            show_notes(notes)
        elif user_input == "find":
            search_notes(notes)
        elif user_input == "help":
            show_notes_help()
        else:
            suggestion = suggest_command(user_input, valid_commands)
            if suggestion:
                print(Fore.YELLOW + f"❓ Можливо ви мали на увазі '{suggestion}'?")
            else:
                print(Fore.RED + "❌ Unknown command. Type 'help' to see available commands.")

def main():
    book, notes = load_data()
    print(Fore.GREEN + "👋 Welcome to Personal Assistant!")
    while True:
        mode = input(Fore.CYAN + "\nEnter mode (contacts/notes or exit): ").strip().lower()

        if mode == "contacts":
            contacts_mode(book, notes)
        elif mode == "notes":
            notes_mode(book, notes)
        elif mode == "exit":
            print(Fore.GREEN + "👋 Good bye!")
            save_data(book, notes)
            break
        else:
            suggestion = suggest_command(mode, ['contacts', 'notes', 'exit'])
            if suggestion:
                print(Fore.YELLOW + f"❓ Можливо ви мали на увазі '{suggestion}'?")
            else:
                print(Fore.RED + "❌ Invalid input. Please enter 'contacts', 'notes' or 'exit'.")

if __name__ == "__main__":
    main()
