# -*- coding: utf-8 -*-
import pymysql


# zainportowanie bazy danych
conn = pymysql.connect("localhost", "root2", "MySQL13", "dieta_box", charset='utf8mb4')
import pymysql




# interfejs dla pracownika wprowadzajego do bazy danych dieta_box dane klientów
# logowanie przez dane pracowników z MySQL np. login: 'w_kepinski', hasło: 'Kepin1!'
class MySQLConnector:
    def __init__(self, passwd):
        self.conn = pymysql.connect("localhost", "root2", "MySQL13", "dieta_box", charset='utf8mb4')
        cur = conn.cursor()
        login = str(input("Podaj login: "))
        haslo = str(input("Podaj hasło: "))        
        bdd = "SELECT login, haslo FROM uprawnienia_prac WHERE login=%s and haslo=%s"
        cur.execute(bdd,(login,haslo))            
        self.c = self.conn.cursor()
        print("Połączenie ustanowione")
        if(cur.rowcount == 1):
            print("Zalogowano poprawnie")
            nav = input("Co chcesz zrobić? (K)-baza klientów, (Z)-baza zamówień, (Q)- wyjście")
            while(nav != "K" or nav != "k" or nav != "Z" or nav != "z" or nav != "q" or nav != "Q"):
                nav = input("Co chcesz dalej wybrać? (K)-baza klientów, (Z)-baza zamówień, (Q)- wyjście")
                if(nav == "K" or nav == "k"):
                    self.selectKlient()
                elif(nav == "Z"or nav == "z"):
                    self.selectZamowienia()
                elif(nav == "Q"or nav == "q"):
                    print("Połączenie zakończone")
                    self.conn.close()
        else:
            print("---UWAGA---")  
            print("Błąd logowania")


#menu praca na kliencie     
    def selectKlient(self):             
        navk = input("Co chcesz zrobić z danymi klienta? (S)-select, (I)-insert, (U)-update, (Q)- wyjście")
        if(navk == "S" or navk == "s"):
            self.selectS()
        elif(navk == "I"or navk == "i"):
            self.insertI()
        elif(navk == "U"or navk == "u"):
            self.updateU()    
        elif(navk == "Q"or navk == "q"):
            print("Połączenie zakończone")
            self.conn.close() 
        else:
            print("------------------UWAGA------------------")  
            print("Wprowadzono niepoprawny kod, wybierz ponownie: ")  
            print(" ")             
   
#menu praca na zamówieniu 
    def selectZamowienia(self):             
        navz = input("Co chcesz zrobić z zamówieniem ? (T)-tabela zamówień, (D)-dopisz zamówienie, (N)-nadpisz brakujące dane w zamówieniu, (Q)- wyjście")
        if(navz == "T" or navz == "t"):
            self.selectT()
        elif(navz == "D"or navz == "d"):
            self.insertD()
        elif(navz == "N"or navz == "n"):
            self.updateN() 
        elif(navz == "Q"or navz == "q"):
            print("Połączenie zakończone")
            self.conn.close() 
        else:
            print("------------------UWAGA------------------")  
            print("Wprowadzono niepoprawny kod, wybierz ponownie: ")  
            print(" ")
       

    # Zamówienia możliwość podejrzenia i poprawy zamówień uszeregowanych wg daty realizacji
    def selectT(self):
        self.c.execute("SELECT opłacono, id_d, dieta, od_kiedy, DATE_ADD(od_kiedy, INTERVAL 1 MONTH) AS do_kiedy, id_k, imię, nazwisko, id_o, nazwa_punktu, adres_punktu FROM diety NATURAL LEFT JOIN zamówienia NATURAL LEFT JOIN klient NATURAL LEFT JOIN punkty_odbioru WHERE opłacono IS NOT NULL ORDER BY od_kiedy;")
        res = self.c.fetchall()        
        print("%-8s | %-10s | %-30s | %-15s | %-15s | %-10s | %-15s | %-15s | %-10s | %-20s | %-15s" % ("opłata", "id diety", "dieta", "od kiedy", "do kiedy", "id kl.", "imię", "nazwisko", "id odb.", "nazwa punktu", "adres punktu"))       
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for v in res:
            opłacono =v [0]
            id_d=v [1]
            dieta=v [2]
            od_kiedy=v [3]
            do_kiedy=v [4]
            id_k=v [5]
            imie = v[6]
            nazwisko = v[7]
            id_o = v[8]
            nazwa_punktu = v[9]
            adres_punktu = v[10]
            print("%-8s | %-10s | %-30s | %-15s | %-15s | %-10s | %-15s | %-15s | %-10s | %-20s | %-15s" %  (opłacono, id_d, dieta, od_kiedy, do_kiedy, id_k, imie, nazwisko, id_o, nazwa_punktu, adres_punktu))
    
   
# baza zamówień- dopisanie nowego zamówienia w przypadku składania zamówienia telefonicznego przez klienta
    def insertD(self):
        self.c.execute("INSERT INTO zamówienia VALUES (8, 6, 4, 'NIE', '2017-11-01');")
        self.conn.commit()
        print("wprowadzono dane: id zamówienia:8, id klienta:6, id diety:4, opłacono:NIE, od kiedy: 2017-11-01")
# baza zamówień- nadpisanie np statusu płatności zamówienia w przypadku opłaty zamówienia przez klienta   
    def updateN(self):
        self.c.execute("UPDATE zamówienia SET opłacono='TAK' where id_k = 8;")
        self.conn.commit()
        print("dane dotyczące płatności zaktualizowane")  


   

# baza klientów - lista
    def selectS(self):
        self.c.execute("select id_k, imię, nazwisko, telefon, miasto, e_mail FROM klient NATURAL LEFT JOIN uprawnienia;")
        res = self.c.fetchall()        
        print("%-3s %-15s %-15s %-15s %-15s %-15s" % ("id klienta", "nazwisko", "imię", "telefon", "miasto", "id odbioru"))       
        print("---------------------------------------------------------------------------------------------------------------------------")
        for v in res:
            id_k =v [0]
            nazwisko = v[1]
            imie = v[2]
            telefon = v[3]
            miasto = v[4]
            id_o = v[5]
            print("%-3s %-15s %-15s %-15s %-15s %-15s" % (id_k, nazwisko, imie, telefon, miasto, id_o))
  
  

# baza klientów - dopisanie nowego klienta
    def insertI(self):
        self.c.execute("INSERT INTO klient VALUES (10, 'Malinowski','Zygmunt', '612-198-424','Piastów', 2);")
        self.c.execute("INSERT INTO uprawnienia VALUES (12, 10, 'Zygmunt', 'Malinowski', 'klient', 'Malina@o2.pl', 'H_malinowski', 'Mali1!' );")
        self.conn.commit()
        print("wprowadzono dane: id klienta:11,  Imię: Zygmunt, Nazwisko: Malinowski, telefon: 512-198-789,, Miasto: Piastów, id punktu: 2")
        print("wprowadzono dane: ID uprawnień: 13, uprawnienia: klient, e_mail:Malina@o2.pl, login: H_malinowski, haslo: Mali1!")
# baza klientów - zaktualizowanie istniejącego klienta        
    def updateU(self):
        self.c.execute("UPDATE klient SET imię='Henryk' where nazwisko = 'Malinowski';")
        self.conn.commit()
        print("dane zaktualizowane")        


c1 = MySQLConnector("MySQL13")



   