import mysql.connector
import calendar


mydb = mysql.connector.connect(
    host="10.2.2.119",
    user="[milosz]",
    password="[milosz2007]",
    database="år"
)


mycursor = mydb.cursor()

def velg_månede():
    return int(input("Velg en måned (1-12): "))

def valgtDato():
    dato = input("velg en dato feks 2024-01-01: ")
    if dato == "":
        dato = '2024-01-01'
    return dato

def vis_januar_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 1)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE january
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM january WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()
        

def vis_februar_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 2)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE february
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM february WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()


def vis_mars_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 3)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE march
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM march WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()


def vis_april_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 4)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE april
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM april WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()


def vis_mai_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 5)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE may
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM may WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()

def vis_juni_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 6)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE june
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM june WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()


def vis_juli_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 7)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE july
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM july WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()


def vis_august_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 8)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE august
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM august WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()


def vis_september_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 9)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE september
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM september WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()


def vis_oktober_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 10)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE october
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM october WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()

def vis_november_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 11)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE november
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM november WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()


def vis_desember_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 12)
    valg = int(input("vil du skrive ett notat skriv 1, vis du vil se ett notat skriv 2: "))

    if valg == 1:
        dato = valgtDato()
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE december
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")

    elif valg == 2:
        dato = valgtDato()
        sql = f"SELECT notes FROM december WHERE date = '{dato}'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result is None:
            print("Det finnes ingen notat for denne datoen.")
        else:
            print(f"Notat for {dato}: {result[0]}")

        
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start_kalender()

def start_kalender():
    måned = velg_månede()  
    if måned not in range(1, 13):  
        print("Ugyldig måned!")
        start_kalender()
    else:
        if måned == 1:
            vis_januar_2024()
        elif måned == 2:
            vis_februar_2024()
        elif måned == 3:
            vis_mars_2024()
        elif måned == 4:
            vis_april_2024()
        elif måned == 5:
            vis_mai_2024()
        elif måned == 6:
            vis_juni_2024()
        elif måned == 7:
            vis_juli_2024()
        elif måned == 8:
            vis_august_2024()
        elif måned == 9:
            vis_september_2024()
        elif måned == 10:
            vis_oktober_2024()
        elif måned == 11:
            vis_november_2024()
        elif måned == 12:
            vis_desember_2024()
        else:
            print("Funksjon for valgt måned er ikke implementert.")

start_kalender()
