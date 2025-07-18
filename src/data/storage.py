import pickle
from pathlib import Path

# Шляхи для збереження даних
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

CONTACTS_FILE = DATA_DIR / "addressbook.pkl"
NOTES_FILE = DATA_DIR / "notebook.pkl"

# Збереження контактів та нотаток
def save_data(book=None, notes=None):
    from address_book.models import AddressBook
    from notebook.notes import NoteBook
    if book is not None:
        with open(CONTACTS_FILE, "wb") as f:
            pickle.dump(book, f)
    if notes is not None:
        with open(NOTES_FILE, "wb") as f:
            pickle.dump(notes, f)

# Завантаження контактів та нотаток
def load_data():
    from address_book.models import AddressBook
    from notebook.notes import NoteBook
    book = AddressBook()
    notes = NoteBook()
    if CONTACTS_FILE.exists():
        with open(CONTACTS_FILE, "rb") as f:
            book = pickle.load(f)
    if NOTES_FILE.exists():
        with open(NOTES_FILE, "rb") as f:
            notes = pickle.load(f)
    return book, notes