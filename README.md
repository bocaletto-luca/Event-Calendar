# Event Calendar Free

**Author**: Bocaletto Luca Aka Elektronoide
![Screenshot 2023-10-08 165730](https://github.com/elektronoide/Event-Calendar-Free/assets/134635227/9c4ea3e2-d32e-4267-aee8-54b053827775)

## Descrizione

Event Calendar Free è un'applicazione per la gestione degli eventi basata su una GUI (Interfaccia Grafica Utente) sviluppata utilizzando il framework PyQt5. Questa applicazione consente agli utenti di visualizzare, aggiungere ed eliminare eventi in un calendario interattivo.

## Caratteristiche principali

1. **Calendario Interattivo**: L'applicazione presenta un calendario interattivo che consente agli utenti di selezionare una data specifica facendo clic su di essa.

2. **Visualizzazione degli Eventi**: Quando un utente seleziona una data nel calendario, l'applicazione mostra una finestra dedicata denominata "Eventi del [Data selezionata]" che visualizza gli eventi associati a quella data.

3. **Aggiunta di Eventi**: Gli utenti possono aggiungere nuovi eventi inserendo un nome e una descrizione per l'evento e facendo clic sul pulsante "Aggiungi Evento". Questi eventi vengono memorizzati in un database SQLite.

4. **Eliminazione di Eventi**: Gli utenti possono eliminare eventi selezionando le righe corrispondenti nella tabella degli eventi e facendo clic sul pulsante "Elimina Evento". Gli eventi eliminati vengono rimossi dal database SQLite.

5. **Visualizzazione Dettagli Evento**: Gli eventi vengono visualizzati in una tabella che mostra l'ID dell'evento, il nome e la descrizione. Questi dettagli aiutano gli utenti a identificare e gestire gli eventi.

6. **Persistenza dei Dati**: I dati sugli eventi vengono memorizzati in un database SQLite chiamato 'events.db', consentendo agli utenti di accedere agli eventi anche dopo la chiusura e la riapertura dell'applicazione.

7. **Validazione degli Input**: L'applicazione include una validazione per assicurarsi che l'utente inserisca almeno il nome dell'evento prima di aggiungerlo.

## Utilizzo

1. All'avvio, l'applicazione mostra un calendario interattivo.
2. Gli utenti possono selezionare una data specifica facendo clic su di essa nel calendario.
3. Quando viene selezionata una data, viene visualizzata una finestra separata che mostra gli eventi associati a quella data.
4. Gli utenti possono aggiungere nuovi eventi inserendo il nome e la descrizione dell'evento e facendo clic su "Aggiungi Evento".
5. Gli utenti possono eliminare eventi selezionando le righe corrispondenti nella tabella degli eventi e facendo clic su "Elimina Evento".
6. Tutti gli eventi vengono memorizzati in modo persistente nel database 'events.db', quindi possono essere consultati in futuro.

Event Calendar Free offre una soluzione semplice e intuitiva per la gestione degli eventi personali, consentendo agli utenti di organizzare e pianificare le proprie attività quotidiane.
