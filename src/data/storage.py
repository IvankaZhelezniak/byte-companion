import pickle                            # для серіалізації/десеріалізації об'єктів Python (контакти, нотатки)
from pathlib import Path                 # зручно працювати з шляхами до файлів

# Шляхи для збереження даних
BASE_DIR = Path(__file__).resolve().parent.parent          # -> /src/storage.py → /src → / (корінь проєкту)
DATA_DIR = BASE_DIR / "data"                               # → /data
DATA_DIR.mkdir(exist_ok=True)                              # Створює папку "data", якщо ще не існує

CONTACTS_FILE = DATA_DIR / "addressbook.pkl"
NOTES_FILE = DATA_DIR / "notebook.pkl"

# Збереження контактів та нотаток
def save_data(book=None, notes=None):
    from address_book.models import AddressBook            # Імпортуємо модель контактів
    from notebook.notes import NoteBook                    # Імпортуємо модель нотаток

    if book is not None:
        with open(CONTACTS_FILE, "wb") as f:          # Відкриваємо файл для запису у бінарному режимі
            pickle.dump(book, f)                      # Зберігаємо книгу контактів
    if notes is not None:
        with open(NOTES_FILE, "wb") as f:
            pickle.dump(notes, f)

# Завантаження контактів та нотаток
def load_data():
    from address_book.models import AddressBook         # Імпортуємо модель контактів
    from notebook.notes import NoteBook

    # Створюємо порожній об'єкт
    book = AddressBook()
    notes = NoteBook()
    # Якщо є файл контактів
    if CONTACTS_FILE.exists():
        with open(CONTACTS_FILE, "rb") as f:
            book = pickle.load(f)           # Завантажуємо об'єкт із файлу

    if NOTES_FILE.exists():
        with open(NOTES_FILE, "rb") as f:
            notes = pickle.load(f)
    return book, notes                # Повертаємо об'єкти