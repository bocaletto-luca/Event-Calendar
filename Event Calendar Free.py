# Name Software: Event Calendar Free
# Author: Bocaletto Luca

# Importazioni delle librerie necessarie
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QVBoxLayout, QPushButton, QDialog, QLineEdit, QTableWidget, QTableWidgetItem, QWidget, QMessageBox

# Definizione della classe principale dell'applicazione
class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Impostazioni della finestra principale
        self.setWindowTitle("Calendario Eventi")
        self.setGeometry(100, 100, 600, 400)

        # Inizializzazione dell'interfaccia utente
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Creazione del widget del calendario
        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.show_event_window)

        layout.addWidget(self.calendar)

        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

    def show_event_window(self, date):
        date_str = date.toString("yyyy-MM-dd")
        event_window = EventWindow(date_str)
        event_window.exec()

# Definizione della classe della finestra degli eventi
class EventWindow(QDialog):
    def __init__(self, date_str):
        super().__init__()

        self.setWindowTitle(f"Eventi del {date_str}")
        self.setGeometry(100, 100, 400, 400)
        self.date_str = date_str

        # Inizializzazione dell'interfaccia utente
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Creazione della tabella degli eventi
        self.event_table = QTableWidget()
        self.event_table.setColumnCount(3) # Aggiunto una colonna per l'ID
        self.event_table.setHorizontalHeaderLabels(["ID", "Nome Evento", "Descrizione Evento"])
        layout.addWidget(self.event_table)

        # Caricamento degli eventi dalla base di dati
        self.load_events()

        self.event_input = QLineEdit()
        self.event_input.setPlaceholderText("Nome Evento")
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("Descrizione Evento")

        self.add_event_button = QPushButton("Aggiungi Evento")
        self.add_event_button.clicked.connect(self.add_event)

        self.delete_event_button = QPushButton("Elimina Evento")
        self.delete_event_button.clicked.connect(self.delete_event)

        layout.addWidget(self.event_input)
        layout.addWidget(self.desc_input)
        layout.addWidget(self.add_event_button)
        layout.addWidget(self.delete_event_button)

        self.setLayout(layout)

    def load_events(self):
        self.event_table.setRowCount(0)
        conn = sqlite3.connect('events.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                datamem DATE NOT NULL
            )
        ''')

        cursor.execute("SELECT id, name, description FROM events WHERE datamem=?", (self.date_str,))
        events = cursor.fetchall()

        conn.close()

        for row, event in enumerate(events):
            self.event_table.insertRow(row)
            for col, value in enumerate(event):
                item = QTableWidgetItem(str(value))
                self.event_table.setItem(row, col, item)

    def add_event(self):
        event_name = self.event_input.text()
        event_desc = self.desc_input.text()

        if event_name:
            conn = sqlite3.connect('events.db')
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    datamem DATE NOT NULL
                )
            ''')

            cursor.execute("INSERT INTO events (name, description, datamem) VALUES (?, ?, ?)", (event_name, event_desc, self.date_str))
            conn.commit()
            conn.close()

            self.event_input.clear()
            self.desc_input.clear()
            self.load_events()
        else:
            QMessageBox.warning(self, 'Errore', 'Inserisci un nome per l\'evento.')

    def delete_event(self):
        selected_rows = set()
        for item in self.event_table.selectedItems():
            selected_rows.add(item.row())

        conn = sqlite3.connect('events.db')
        cursor = conn.cursor()

        for row in sorted(selected_rows, reverse=True):
            event_id = self.event_table.item(row, 0).text()
            cursor.execute("DELETE FROM events WHERE id=?", (event_id,))
            conn.commit()

        conn.close()

        self.load_events()

# Blocco di codice principale per avviare l'applicazione
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec_())
