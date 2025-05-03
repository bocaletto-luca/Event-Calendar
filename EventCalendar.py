# Nome del software: Event Calendar Free
# Autore: Bocaletto Luca
# Importa le librerie necessarie
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QVBoxLayout, QPushButton, QDialog, QLineEdit, QTableWidget, QTableWidgetItem, QWidget, QMessageBox

# Definizione della classe principale dell'applicazione
class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Impostazioni della finestra principale
        self.setWindowTitle("Calendario Eventi")  # Imposta il titolo della finestra principale
        self.setGeometry(100, 100, 600, 400)  # Imposta la posizione e le dimensioni della finestra principale

        # Inizializzazione dell'interfaccia utente
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()  # Crea un layout verticale per la finestra principale

        # Creazione del widget del calendario
        self.calendar = QCalendarWidget(self)  # Crea un widget del calendario all'interno della finestra principale
        self.calendar.clicked.connect(self.show_event_window)  # Connette il segnale "clicked" del calendario alla funzione show_event_window

        layout.addWidget(self.calendar)  # Aggiunge il widget del calendario al layout

        self.central_widget = QWidget()  # Crea un widget centrale
        self.central_widget.setLayout(layout)  # Imposta il layout appena creato come layout del widget centrale
        self.setCentralWidget(self.central_widget)  # Imposta il widget centrale come widget centrale della finestra principale

    def show_event_window(self, date):
        date_str = date.toString("yyyy-MM-dd")  # Converte la data selezionata in una stringa nel formato specificato
        event_window = EventWindow(date_str)  # Crea una finestra degli eventi passando la data come argomento
        event_window.exec()  # Esegue la finestra degli eventi in modalità modale

# Definizione della classe della finestra degli eventi
class EventWindow(QDialog):
    def __init__(self, date_str):
        super().__init__()

        # Impostazioni della finestra degli eventi
        self.setWindowTitle(f"Eventi del {date_str}")  # Imposta il titolo della finestra degli eventi con la data selezionata
        self.setGeometry(100, 100, 400, 400)  # Imposta la posizione e le dimensioni della finestra degli eventi

        self.date_str = date_str  # Memorizza la data selezionata come attributo della finestra degli eventi

        # Inizializzazione dell'interfaccia utente
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()  # Crea un layout verticale per la finestra degli eventi

        # Creazione della tabella degli eventi
        self.event_table = QTableWidget()  # Crea una tabella per visualizzare gli eventi
        self.event_table.setColumnCount(3)  # Aggiunto una colonna per l'ID
        self.event_table.setHorizontalHeaderLabels(["ID", "Nome Evento", "Descrizione Evento"])
        layout.addWidget(self.event_table)

        # Caricamento degli eventi dalla base di dati
        self.load_events()

        self.event_input = QLineEdit()  # Crea un campo di input per il nome dell'evento
        self.event_input.setPlaceholderText("Nome Evento")  # Imposta un testo di esempio nel campo di input
        self.desc_input = QLineEdit()  # Crea un campo di input per la descrizione dell'evento
        self.desc_input.setPlaceholderText("Descrizione Evento")  # Imposta un testo di esempio nel campo di input

        self.add_event_button = QPushButton("Aggiungi Evento")  # Crea un pulsante per aggiungere un evento
        self.add_event_button.clicked.connect(self.add_event)  # Connette il pulsante all'azione di aggiunta di un evento

        self.delete_event_button = QPushButton("Elimina Evento")  # Crea un pulsante per eliminare un evento
        self.delete_event_button.clicked.connect(self.delete_event)  # Connette il pulsante all'azione di eliminazione di un evento

        layout.addWidget(self.event_input)  # Aggiunge il campo di input per il nome dell'evento al layout
        layout.addWidget(self.desc_input)  # Aggiunge il campo di input per la descrizione dell'evento al layout
        layout.addWidget(self.add_event_button)  # Aggiunge il pulsante "Aggiungi Evento" al layout
        layout.addWidget(self.delete_event_button)  # Aggiunge il pulsante "Elimina Evento" al layout

        self.setLayout(layout)  # Imposta il layout appena creato come layout della finestra degli eventi

    def load_events(self):
        self.event_table.setRowCount(0)  # Imposta il numero di righe della tabella degli eventi a 0
        conn = sqlite3.connect('events.db')  # Si connette al database SQLite
        cursor = conn.cursor()  # Crea un cursore per eseguire query SQL

        # Crea la tabella degli eventi se non esiste già nel database
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                datamem DATE NOT NULL
            )
        ''')

        # Seleziona gli eventi dalla tabella che corrispondono alla data selezionata
        cursor.execute("SELECT id, name, description FROM events WHERE datamem=?", (self.date_str,))
        events = cursor.fetchall()  # Ottiene tutti gli eventi

        conn.close()  # Chiude la connessione al database

        # Popola la tabella degli eventi con i dati ottenuti
        for row, event in enumerate(events):
            self.event_table.insertRow(row)
            for col, value in enumerate(event):
                item = QTableWidgetItem(str(value))
                self.event_table.setItem(row, col, item)

    def add_event(self):
        event_name = self.event_input.text()  # Ottiene il testo inserito nel campo di input per il nome dell'evento
        event_desc = self.desc_input.text()  # Ottiene il testo inserito nel campo di input per la descrizione dell'evento

        if event_name:
            conn = sqlite3.connect('events.db')  # Si connette al database SQLite
            cursor = conn.cursor()  # Crea un cursore per eseguire query SQL

            # Crea la tabella degli eventi se non esiste già nel database
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    datamem DATE NOT NULL
                )
            ''')

            # Inserisce un nuovo evento nel database con il nome, la descrizione e la data
            cursor.execute("INSERT INTO events (name, description, datamem) VALUES (?, ?, ?)", (event_name, event_desc, self.date_str))
            conn.commit()  # Conferma la transazione nel database
            conn.close()  # Chiude la connessione al database

            self.event_input.clear()  # Cancella il testo nel campo di input per il nome dell'evento
            self.desc_input.clear()  # Cancella il testo nel campo di input per la descrizione dell'evento
            self.load_events()  # Richiama la funzione per ricaricare gli eventi nella tabella
        else:
            QMessageBox.warning(self, 'Errore', 'Inserisci un nome per l\'evento.')  # Mostra un messaggio di avviso se il nome dell'evento è vuoto

    def delete_event(self):
        selected_rows = set()  # Crea un insieme per memorizzare le righe selezionate nella tabella
        for item in self.event_table.selectedItems():  # Itera sugli elementi selezionati nella tabella
            selected_rows.add(item.row())  # Aggiunge la riga dell'elemento selezionato all'insieme

        conn = sqlite3.connect('events.db')  # Si connette al database SQLite
        cursor = conn.cursor()  # Crea un cursore per eseguire query SQL

        for row in sorted(selected_rows, reverse=True):  # Itera sulle righe selezionate in ordine inverso
            event_id = self.event_table.item(row, 0).text()  # Ottiene l'ID dell'evento dalla tabella
            cursor.execute("DELETE FROM events WHERE id=?", (event_id,))  # Elimina l'evento dal database
            conn.commit()  # Conferma la transazione nel database
            self.event_table.removeRow(row)  # Rimuove la riga dalla tabella

        conn.close()  # Chiude la connessione al database

# Blocco di codice principale per avviare l'applicazione
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crea un'applicazione Qt
    window = CalendarApp()  # Crea la finestra principale dell'applicazione
    window.show()  # Mostra la finestra principale
    sys.exit(app.exec_())  # Esegue l'applicazione e gestisce l'uscita
