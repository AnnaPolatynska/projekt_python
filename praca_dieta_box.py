# -*- coding: utf-8 -*-
import pymysql


# zainportowanie bazy danych
conn = pymysql.connect("localhost", "root2", "MySQL13", "dieta_box", charset='utf8mb4')
import pymysql




# interfejs dla pracownika wprowadzajego do bazy danych dieta_box dane klientów

class MySQLConnector:
    def __init__(self, passwd):
        self.passwd = passwd
        self.conn = pymysql.connect("localhost", "root2", "MySQL13", "dieta_box", charset='utf8mb4')
        self.c = self.conn.cursor()
        print("Połączenie ustanowione")
        nav = ''
        while(nav != "Q"):
            nav = input("Co chcesz zrobić? (S)-select, (I)-insert, (U)-update, (Q)- wyjście")
            if(nav == "S"):
                self.select()
            elif(nav == "I"):
                self.insert()
            elif(nav == "U"):
                self.update()                
        print("Połączenie zakończone")
        self.conn.close()    
    def select(self):
        self.c.execute("select id_k, imię, nazwisko, telefon, miasto, e_mail FROM klient NATURAL LEFT JOIN uprawnienia;")
        res = self.c.fetchall()        
        print("%-3s %-15s %-15s %-15s %-15s %-15s" % ("id", "imię", "nazwisko", "telefon", "miasto", "e_mail"))       
        print("---------------------------------------------------------------------------------------------------------------------------")
        for v in res:
            id_k =v [0]
            imie = v[1]
            nazwisko = v[2]
            telefon = v[3]
            miasto = v[4]
            e_mail = v[5]
            print("%-3s %-15s %-15s %-15s %-15s %-15s" % (id_k, imie, nazwisko, telefon, miasto, e_mail))
    def insert(self):
        self.c.execute("INSERT INTO klient VALUES (10, 'Malinowski','Zygmunt', '612-198-424','Piastów')")
        self.conn.commit()
        print("wprowadzono dane: 10,  Zygmunt, Malinowski, 612-198-424, Piastów")
    def update(self):
        self.c.execute("UPDATE klient SET imię='Zbigniew' where nazwisko = 'Malinowski';")
        self.conn.commit()
        print("dane zaktualizowane")        


c1 = MySQLConnector("MySQL13")



   