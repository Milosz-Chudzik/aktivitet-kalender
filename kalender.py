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
        else:
            print("Funksjon for valgt måned er ikke implementert.")

start()
