# Event Calendar

**Author:** Bocaletto Luca

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge&logo=gnu)](LICENSE) [![Language: Python](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python)](https://www.python.org/) [![Linux-Compatible](https://img.shields.io/badge/Linux-Compatible-blue?style=for-the-badge&logo=linux)](https://www.kernel.org/) [![Status: Complete](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)](https://github.com/bocaletto-luca/Directory-Monitor)

## Description

Event Calendar Free is an event management application based on a Graphical User Interface (GUI) developed using the PyQt5 framework. This application allows users to view, add, and delete events on an interactive calendar.

![Screenshot 2023-10-08 165730](https://github.com/elektronoide/Event-Calendar-Free/assets/134635227/9c4ea3e2-d32e-4267-aee8-54b053827775)

## Key Features

1. **Interactive Calendar**: The application features an interactive calendar that enables users to select a specific date by clicking on it.

2. **Event Display**: When a user selects a date on the calendar, the application displays a dedicated window titled "Events for [Selected Date]" that shows the events associated with that date.

3. **Event Addition**: Users can add new events by entering a name and description for the event and clicking the "Add Event" button. These events are stored in an SQLite database.

4. **Event Deletion**: Users can delete events by selecting the corresponding rows in the event table and clicking the "Delete Event" button. Deleted events are removed from the SQLite database.

5. **Event Details Display**: Events are displayed in a table that shows the event's ID, name, and description. These details help users identify and manage events.

6. **Data Persistence**: Event data is stored in an SQLite database named 'events.db,' allowing users to access events even after closing and reopening the application.

7. **Input Validation**: The application includes validation to ensure that users enter at least the event name before adding it.

## Usage

1. Upon startup, the application displays an interactive calendar.

2. Users can select a specific date by clicking on it in the calendar.

3. When a date is selected, a separate window is displayed showing the events associated with that date.

4. Users can add new events by entering the event name and description and clicking "Add Event."

5. Users can delete events by selecting the corresponding rows in the event table and clicking "Delete Event."

6. All events are persistently stored in the 'events.db' database, allowing for future reference.

Event Calendar Free provides a simple and intuitive solution for personal event management, enabling users to organize and plan their daily activities.

---

**Note**: Ensure that you have installed all the necessary dependencies before running the application.

**Maintainer Update**

My current GitHub account is **@bocaletto-luca**, which is now the official maintainer of all projects previously published under the **@Elektronoide** account. Please direct any issues, pull requests, or stars to **@bocaletto-luca** for future updates.

---
