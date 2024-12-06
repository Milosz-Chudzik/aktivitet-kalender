import mysql.connector

mydb = mysql.connector.connect(
    host="10.2.2.119",
    user="[milosz]",
    password="[milosz2007]",
    database="Stats"
)


cursor = mydb.cursor()

def start():
    try:
        print("Velg fra menyen:")
        print("1. legge inn øvelser")
        print("2. oppdatere dine øvelser")
        print("3. se dine øvelser")
        print("4. Avslutt")
        valg = int(input("Skriv inn ditt valg: "))

        if valg == 1:
            legge_inn_ovelse()
        elif valg == 2:
            oppdater_ovelse()
        elif valg == 3:
            vis_ovelse()
        elif valg == 4:
            print("Avslutter...")
        else:
            print("Ugyldig valg, prøv igjen.")
            start()

    except ValueError:
        print("Ugyldig valg, prøv igjen.")
        start()

def legge_inn_ovelse():
    navn = input("navn på øvelsen: ")
    muskelgruppe = input("hvilken muskelgruppe trener øvelsen?: ")
    try:
        sql = f"SELECT * FROM ovelser WHERE ovelse = {navn}"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            sql = f"INSERT INTO ovelser (navn, muskelgruppe) VALUES ('{navn}', '{muskelgruppe}')"
            cursor.execute(sql)
            mydb.commit()
            print(f"øvelsen {navn} er lagret.")
            start()
    except:
        print("Noe gikk galt, prøv igjen.")
        legge_inn_ovelse()

def oppdater_ovelse():
    valg = int(input("hva er det du ønsker å endre? \ntrykk 1 for reps \ntrykk 2 for sets \ntrykk 3 for vekt \ntrykk 4 for å gå tilbake:"))
    if valg == 1:
        navn = input("navn på øvelsen: ")
        øvelse = input("hvilken øvelse skal du oppdatere: ")
        reps = int(input("nytt antall reps: "))
        sql = f"update bruker_ovelser where bruker_id "

    elif valg == 2:

    elif valg == 3:

    elif valg == 4:
        start()
    
    else: 
        print("Ugyldig valg, prøv igjen.")
        oppdater_ovelse()