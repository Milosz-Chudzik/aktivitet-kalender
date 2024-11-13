import os
import sqlite3
import calendar

# Check if the database file exists and remove it if it's corrupted
db_path = 'kalender.db'
if os.path.exists(db_path):
    os.remove(db_path)

# Create a new SQLite connection and cursor
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS januar (
                dato TEXT PRIMARY KEY,
                ukedag TEXT,
                notater TEXT
            )''')

conn.commit()

# Continue with the rest of your code...

# Remember to close the connection when done




def display_calendar(year, month, notes):
    month_calendar = calendar.monthcalendar(year, month)
      
    print(" Mon  Tue  Wen  Thu  Fri Sat  Sun")
    
    for week in month_calendar:
        for day in week:
            if day == 0:
                print("    ", end="  ") 
            else:
                day_str = f"{day:>3}"
                if day in notes:
                    day_str += f"*({notes[day]})"
                print(f"{day_str} ", end=" ")
        print()  

def get_user_input():
    while True:
        try:
            year = int(input("Enter the year (e.g., 2024): "))
            month = int(input("Enter the month (1-12): "))
            
            if 1 <= month <= 12:
                return year, month
            else:
                print("Invalid month. Please enter a number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def add_note_to_day(notes):
    try:
        day = int(input("Enter the day you want to add a note to (1-31): "))
        if 1 <= day <= 31:
            note = input(f"Enter the note for day {day}: ")
            notes[day] = note
            print(f"Note added for day {day}.")
        else:
            print("Invalid day. Please enter a day between 1 and 31.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def load_notes_from_db(year, month):
    notes = {}
    cursor.execute('SELECT dato, notater FROM januar WHERE strftime("%Y", dato) = ? AND strftime("%m", dato) = ?', (str(year), f"{month:02d}"))
    rows = cursor.fetchall()
    for row in rows:
        day = int(row[0].split('-')[2])  # Extract the day from 'YYYY-MM-DD'
        notes[day] = row[1]
    return notes


while True:
    year, month = get_user_input()
    notes = load_notes_from_db(year, month)  # Load existing notes from the database
    display_calendar(year, month, notes)
    
    add_note = input("Would you like to add a note to a day? (y/n): ").lower()
    if add_note == 'y':
        add_note_to_day(notes, year, month)
    
    continue_prompt = input("Would you like to see another month? (y/n): ").lower()
    if continue_prompt != 'y':
        break


notes = {}  

while True:
    year, month = get_user_input()
    display_calendar(year, month, notes)
    
    add_note = input("Would you like to add a note to a day? (y/n): ").lower()
    if add_note == 'y':
        add_note_to_day(notes)
    
    continue_prompt = input("Would you like to see another month? (y/n): ").lower()
    if continue_prompt != 'y':
        break

conn.close()