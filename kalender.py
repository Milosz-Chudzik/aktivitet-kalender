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
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE january
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()
        

def vis_februar_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 2)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE february
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()


def vis_mars_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 3)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE march
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()


def vis_april_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 4)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE april
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()


def vis_mai_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 5)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE may
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()


def vis_juni_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 6)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE june
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()


def vis_juli_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 7)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE july
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()


def vis_august_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 8)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE august
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()


def vis_september_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 9)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE september
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()


def vis_oktober_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 10)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE october
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()

def vis_november_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 11)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE november
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()


def vis_desember_2024():
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2024, 12)
    if input("vil du skrive ett notat ja/nei: ").lower() == "ja":
        dato = valgtDato()
        # if dato not in range(1, 1000000000000):  
        #     print("Ugyldig dato!")
        
        # else: 
        notat = input("Skriv notat: ")
        sql = f"""
        UPDATE december
        SET notes = '{notat}'
        WHERE date = '{dato}'
        """
        mycursor.execute(sql)
        mydb.commit()
        print(f"Notat lagret for {dato}.")
            


    else:
        if input("vil du gå tilbake ja/nei") == "ja":
            start()

def start():
    måned = velg_månede()  
    if måned not in range(1, 13):  
        print("Ugyldig måned!")
        start()
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

start()
