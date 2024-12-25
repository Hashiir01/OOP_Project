# no need to run again database is created

import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create fan table with restricted payment options
cursor.execute('''
    CREATE TABLE IF NOT EXISTS fan (
        fan_id INTEGER PRIMARY KEY,
        name TEXT,
        cnic TEXT UNIQUE,
        phone_number TEXT,
        email TEXT,
        payment_method TEXT CHECK(payment_method IN ('BANK TRANSFER', 'DEBIT CARD', 'JAZZ CASH'))
    )
''')

fan_data = [
    (1, "Ahmed Khan", "1234567023", "1234567890", "ahmed@example.com", "JAZZ CASH"),
    (2, "Fatima Ali", "9876543210987", "9876543210", "fatima@example.com", "BANK TRANSFER"),
    (3, "Mohammad Ahmed", "2345678901234", "2345678901", "mohammad@example.com", "DEBIT CARD"),
    (4, "Ayesha Zafar", "3456789012345", "3456789012", "ayesha@example.com", "BANK TRANSFER"),
    (5, "Ali Hassan", "4567890123456", "4567890123", "ali@example.com", "JAZZ CASH"),
    (6, "Sanaullah Khan", "5678901234567", "5678901234", "sanaullah@example.com", "JAZZ CASH"),
    (7, "Farah Siddiqui", "6789012345678", "6789012345", "farah@example.com", "BANK TRANSFER"),
    (8, "Saad Ahmed", "7890123456789", "7890123456", "saad@example.com", "DEBIT CARD"),
    (9, "Amina Akram", "8901234567890", "8901234567", "amina@example.com", "BANK TRANSFER"),
    (10, "Bilal Khan", "9012345678901", "9012345678", "bilal@example.com", "JAZZ CASH"),
    (11, "Sadia Ali", "0123456789012", "0123456789", "sadia@example.com", "JAZZ CASH"),
    (12, "Imran Malik", "1234567890123", "1234567890", "imran@example.com", "BANK TRANSFER"),
    (13, "Rabia Ahmed", "235678901234", "2345678901", "rabia@example.com", "DEBIT CARD"),
    (14, "Kamran Khan", "34569012345", "3456789012", "kamran@example.com", "BANK TRANSFER"),
    (15, "Nida Hussain", "45690123456", "4567890123", "nida@example.com", "JAZZ CASH"),
    (16, "Arif Ali", "5678934567", "5678901234", "arif@example.com", "JAZZ CASH"),
    (17, "Nazia Iqbal", "7890145678", "6789012345", "nazia@example.com", "BANK TRANSFER"),
    (18, "Omar Khan", "78901256789", "7890123456", "omar@example.com", "DEBIT CARD"),
    (19, "Saima Amin", "89012347890", "8901234567", "saima@example.com", "BANK TRANSFER"),
    (20, "Waqar Ahmed", "90123678901", "9012345678", "waqar@example.com", "JAZZ CASH"),
    (21, "Ayesha Ali", "01236789012", "0123456789", "ayesha@example.com", "JAZZ CASH"),
    (22, "Khalid Khan", "12345670123", "1234567890", "khalid@example.com", "BANK TRANSFER"),
    (23, "Aisha Ahmed", "234567901234", "2345678901", "aisha@example.com", "DEBIT CARD"),
    (24, "Rizwan Malik", "345678901345", "3456789012", "rizwan@example.com", "BANK TRANSFER"),
    (25, "Hina Khan", "4567823456", "4567890123", "hina@example.com", "JAZZ CASH"),
    (26, "Asim Ahmed", "5678904567", "5678901234", "asim@example.com", "JAZZ CASH"),
    (27, "Naima Akram", "678901245678", "6789012345", "naima@example.com", "BANK TRANSFER"),
    (28, "Kashif Malik", "780123456789", "7890123456", "kashif@example.com", "DEBIT CARD"),
    (29, "Farida Ali", "890123456890", "8901234567", "farida@example.com", "BANK TRANSFER"),
]


cursor.executemany("INSERT INTO fan (fan_id, name, cnic, phone_number, email, payment_method) VALUES (?, ?, ?, ?, ?, ?)", fan_data)



# Create match table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS match (
        match_id INTEGER PRIMARY KEY,
        team_names TEXT,
        stadium_id INTEGER,
        date_time TEXT,
        FOREIGN KEY (stadium_id) REFERENCES stadium(stadium_id)
    )
''')

# Dummy data for match table with match IDs, team names, stadium IDs, and date-time
match_data = [
    (1, "Karachi Kings,Lahore Qalandars", 1, "2024-01-01 18:00:00"),
    (2, "Quetta Gladiators,Islamabad United", 2, "2024-01-05 19:30:00"),
    (3, "Peshawar Zalmi,Multan Sultans", 3, "2024-01-10 20:00:00"),
    (4, "Lahore Qalandars,Karachi Kings", 1, "2024-01-15 18:30:00"),
    (5, "Islamabad United,Quetta Gladiators", 2, "2024-01-20 19:00:00"),
    (6, "Multan Sultans,Peshawar Zalmi", 3, "2024-01-25 20:30:00"),
    (7, "Karachi Kings,Lahore Qalandars", 1, "2024-01-30 18:45:00"),
    (8, "Quetta Gladiators,Islamabad United", 2, "2024-02-05 19:15:00"),
    (9, "Peshawar Zalmi,Multan Sultans", 3, "2024-02-10 20:45:00"),
    (10, "Lahore Qalandars,Karachi Kings", 1, "2024-02-15 18:15:00"),
]

cursor.executemany("INSERT INTO match (match_id, team_names, stadium_id, date_time) VALUES (?, ?, ?, ?)", match_data)


# Create tickets table with modified ticket_price column
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        ticket_id INTEGER PRIMARY KEY,
        ticket_price TEXT CHECK(ticket_price IN ('VIP', 'First Class', 'Premium', 'General')),
        fan_id INTEGER,
        stadium_id INTEGER,
        match_id INTEGER,
        FOREIGN KEY (fan_id) REFERENCES fan(fan_id),
        FOREIGN KEY (stadium_id) REFERENCES stadium(stadium_id),
        FOREIGN KEY (match_id) REFERENCES match(match_id)
    )
''')

tickets_data = [
    (1, 'VIP', 1, 1, 1),
    (2, 'First Class', 2, 2, 2),
    (3, 'Premium', 3, 3, 3),
    (4, 'General', 4, 1, 4),
    (5, 'VIP', 5, 2, 5),
    (6, 'First Class', 6, 3, 6),
    (7, 'Premium', 7, 1, 7),
    (8, 'General', 8, 2, 8),
    (9, 'VIP', 9, 3, 9),
    (10, 'First Class', 10, 1, 10),
    (11, 'Premium', 11, 2, 11),
    (12, 'General', 12, 3, 12),
    (13, 'VIP', 13, 1, 13),
    (14, 'First Class', 14, 2, 14),
    (15, 'Premium', 15, 3, 15),
    (16, 'General', 16, 1, 16),
    (17, 'VIP', 17, 2, 17),
    (18, 'First Class', 18, 3, 18),
    (19, 'Premium', 19, 1, 19),
    (20, 'General', 20, 2, 20),
    (21, 'VIP', 21, 3, 21),
    (22, 'First Class', 22, 1, 22),
    (23, 'Premium', 23, 2, 23),
    (24, 'General', 24, 3, 24),
    (25, 'VIP', 25, 1, 25),
    (26, 'First Class', 26, 2, 26),
    (27, 'Premium', 27, 3, 27),
    (28, 'General', 28, 1, 28),
    (29, 'VIP', 29, 2, 29),
    (30, 'First Class', 30, 3, 30),
    (31, 'Premium', 31, 1, 31),
    (32, 'General', 32, 2, 32),
    (33, 'VIP', 33, 3, 33),
    (34, 'First Class', 34, 1, 34),
    (35, 'Premium', 35, 2, 35),
    (36, 'General', 36, 3, 36),
    (37, 'VIP', 37, 1, 37),
    (38, 'First Class', 38, 2, 38),
    (39, 'Premium', 39, 3, 39),
    (40, 'General', 40, 1, 40),
]

cursor.executemany("INSERT INTO tickets (ticket_id, ticket_price, fan_id, stadium_id, match_id) VALUES (?, ?, ?, ?, ?)", tickets_data)


# Create stadium table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS stadium (
        stadium_id INTEGER PRIMARY KEY,
        stadium_name TEXT,
        location TEXT
    )
''')
stadium_data = [
    (1, "Gaddafi Stadium", "Lahore"),
    (2, "National Stadium", "Karachi"),
    (3, "Rawalpindi Cricket Stadium", "Rawalpindi"),
    (4, "Arbab Niaz Stadium", "Peshawar"),
    (5, "Bugti Stadium", "Quetta"),
    (6, "Multan Cricket Stadium", "Multan"),
    (7, "Iqbal Stadium", "Faisalabad"),
    (8, "Mirpur Cricket Stadium", "Azad Kashmir"),
    (9, "Sialkot Cricket Stadium", "Sialkot"),
    (10, "Jinnah Stadium", "Gujranwala"),
]


cursor.executemany("INSERT INTO stadium (stadium_id, stadium_name, location) VALUES (?, ?, ?)", stadium_data)



# Create purchase_log table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS purchase_log (
        log_id INTEGER PRIMARY KEY,
        ticket_id INTEGER,
        purchase_time TEXT,
        FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id)
    )
''')

purchase_log_data = [
    (1, 1, "2024-01-01 12:30:00"),
    (2, 2, "2024-01-02 14:45:00"),
    (3, 3, "2024-01-03 16:20:00"),
    (4, 4, "2024-01-04 18:05:00"),
    (5, 5, "2024-01-05 20:15:00"),
    (6, 6, "2024-01-06 22:00:00"),
    (7, 7, "2024-01-07 09:45:00"),
    (8, 8, "2024-01-08 11:30:00"),
    (9, 9, "2024-01-09 13:20:00"),
    (10, 10, "2024-01-10 15:10:00"),
    (11, 11, "2024-03-01 17:30:00"),
    (12, 12, "2024-03-02 19:45:00"),
    (13, 13, "2024-03-03 21:20:00"),
    (14, 14, "2024-03-04 23:05:00"),
    (15, 15, "2024-03-05 10:15:00"),
    (16, 16, "2024-03-06 12:00:00"),
    (17, 17, "2024-03-07 13:45:00"),
    (18, 18, "2024-03-08 15:30:00"),
    (19, 19, "2024-03-09 17:20:00"),
    (20, 20, "2024-03-10 19:10:00"),
    (21, 21, "2024-03-11 21:30:00"),
    (22, 22, "2024-03-12 23:45:00"),
    (23, 23, "2024-03-13 08:20:00"),
    (24, 24, "2024-03-14 10:05:00"),
    (25, 25, "2024-03-15 12:15:00"),
    (26, 26, "2024-03-16 14:00:00"),
    (27, 27, "2024-03-17 15:45:00"),
    (28, 28, "2024-03-18 17:30:00"),
    (29, 29, "2024-03-19 19:20:00"),
    (30, 30, "2024-03-20 21:10:00"),
    (31, 31, "2024-03-21 22:30:00"),
    (32, 32, "2024-03-22 10:45:00"),
    (33, 33, "2024-03-23 12:30:00"),
    (34, 34, "2024-03-24 14:15:00"),
    (35, 35, "2024-03-25 16:00:00"),
    (36, 36, "2024-03-26 17:45:00"),
    (37, 37, "2024-03-27 19:30:00"),
    (38, 38, "2024-03-28 21:20:00"),
    (39, 39, "2024-03-29 23:10:00"),
    (40, 40, "2024-03-30 08:30:00"),
    (41, 41, "2024-04-01 10:45:00"),
    (42, 42, "2024-04-02 12:30:00"),
    (43, 43, "2024-04-03 14:15:00"),
    (44, 44, "2024-04-04 16:00:00"),
    (45, 45, "2024-04-05 17:45:00"),
    (46, 46, "2024-04-06 19:30:00"),
    (47, 47, "2024-04-07 21:20:00"),
    (48, 48, "2024-04-08 23:10:00"),
    (49, 49, "2024-04-09 09:30:00"),
    (50, 50, "2024-04-10 11:45:00"),
    (51, 1, "2024-02-20 14:30:00"),
    (52, 2, "2024-02-21 16:45:00"),
    (53, 3, "2024-02-22 18:20:00"),
    (54, 4, "2024-02-23 20:05:00"),
    (55, 5, "2024-02-24 22:15:00"),
    (56, 6, "2024-02-25 09:00:00"),
    (57, 7, "2024-02-26 10:45:00"),
    (58, 8, "2024-02-27 12:30:00"),
    (59, 9, "2024-02-28 14:20:00"),
    (60, 10, "2024-02-29 16:10:00"),
]

cursor.executemany("INSERT INTO purchase_log (log_id, ticket_id, purchase_time) VALUES (?, ?, ?)", purchase_log_data)




# Commit the changes and close the connection
conn.commit()
conn.close()
