# -*- coding: utf-8 -*-
import pymysql


# zainportowanie bazy danych
conn = pymysql.connect("localhost", "root2", "MySQL13", "dieta_box", charset='utf8mb4')
import pymysql


# interfejs dla klientów wyboru lokalizacji odbioru i dietaBoxu

#menu główne
class MySQLConnector:
    def __init__(self, passwd):
        self.conn = pymysql.connect("localhost", "root2", "MySQL13", "dieta_box", charset='utf8mb4')
        cur = conn.cursor()        
        login = str(input("Podaj login: "))
        haslo = str(input("Podaj hasło: "))        
        bdd = "SELECT login, haslo FROM uprawnienia WHERE login=%s and haslo=%s"
        cur.execute(bdd,(login,haslo))            
        self.c = self.conn.cursor()
        print("Połączenie ustanowione")
        if(cur.rowcount == 1):
            print("Zalogowano poprawnie")
            nav_s = ''
            while(nav_s != "Q"):
                nav_s = input("Co chcesz zrobić? (P)-Wybrać punkty odbioru, (O)-zapoznać się z ofertą, (K)-kupić dietę, (Q)- wyjście")
                if(nav_s == "P"):
                    self.selectP()
                elif(nav_s == "O"):
                    self.selectO()
                elif(nav_s == "K"):
                    self.selectK()                
            print("Połączenie zakończone")
            self.conn.close()    
            
        else:
            print("Błąd logowania")
        
   
# adresy punktów odbioru        
    def selectP(self):
        self.c.execute("SELECT nazwa_punktu, adres_punktu, miasto FROM punkty_odbioru ORDER BY miasto;")
        res = self.c.fetchall() 
        print("%-30s   |   %-30s   |   %-30s " % ("punkt odbioru", "adres punktu odbioru", "miasto"))
        print("----------------------------------------------------------------------------------------------------")        
        for p in res:
            nazwa_punktu = p[0]
            adres_punktu = p[1]
            miasto = p[2]
            print("%-30s   |   %-30s   |   %-30s" % (nazwa_punktu, adres_punktu, miasto))
        print("----------------------------------------------------------------------------------------------------")     

# opisy diet
    def selectO(self):
        self.c.execute("SELECT dieta, opis, cena_netto * 1.23 AS 'cena_brutto' FROM diety;")
        res = self.c.fetchall()        
        print("%-30s   |   %-140s   |   %-30s " % ("dieta", "opis diety", "cena brutto"))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for o in res:
            dieta = o[0]
            opis = o[1]
            cena_brutto = o[2]         
            print("%-30s   |   %-140s   |   %-30s " %  (dieta, opis, cena_brutto))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    




# wybór diet
    def selectK(self):
        nav_k = ''
        while(nav_k != "Q"):
            nav_k = input("Jaką dietę chcesz kupić? (1) dietę odchudzającą-egzotyczne smaki , (2) dietę odchudzjącą standardową, (3) dietę zdrowotną- wzmocnij serce, (4) dietę zdrowotną standardową, (5) dietę sportową - wytrzymałość, (6) dietę sportową - siła (Q)- wyjście")
            if(nav_k == "1"):
                self.select1()
                print("zamówiłeś dietę odchudzającą-egzotyczne smaki")
                print(" ")
            elif(nav_k == "2"):
                self.select2()
                print("Zamówiłeś dietę odchudzjącą standardową. Twoje zamówienie czeka na opłatę.")
                print(" ")
            elif(nav_k == "3"):
                self.select3()
                print("Zamówiłeś dietę zdrowotną- wzmocnij serce. Twoje zamówienie czeka na opłatę.")
                print(" ")
            elif(nav_k == "4"):
                self.select4()
                print("Zamówiłeś dietę zdrowotną standardową.Twoje zamówienie czeka na opłatę.")
                print(" ")
            elif(nav_k == "5"):
                self.select5()
                print("Zamówiłeś dietę dietę sportową - wytrzymałość. Twoje zamówienie czeka na opłatę.")
                print(" ")
            elif(nav_k == "6"):
                self.select6()
                print("Zamówiłeś dietę dietę sportową - siła. Twoje zamówienie czeka na opłatę.")
                print(" ")
 
                
        print("Połączenie zakończone")
        self.conn.close() 
     
    def select1(self):
        self.c.execute("SELECT dieta, cena_netto, cena_netto * 1.23 AS 'cena_brutto' FROM diety WHERE id_d=1;")
        res = self.c.fetchall()        
        for a in res:
            dieta = a[0]
            cena_netto = a[1]
            cena_brutto = a[2]
            print("%-30s   |   %-40s   |   %-30s " % ("dieta", "cena netto", "cena brutto"))
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("%-30s   |   %-40s   |   %-30s " %  (dieta, cena_netto, cena_brutto))
            print("---------------------------------------------------------------------------------------------------------------------------")
                
    def select2(self):
        self.c.execute("SELECT dieta, cena_netto, cena_netto * 1.23 AS 'cena_brutto' FROM diety WHERE id_d=2;")
        res = self.c.fetchall()        
        for a in res:
            dieta = a[0]
            cena_netto = a[1]
            cena_brutto = a[2]
            print("%-30s   |   %-40s   |   %-30s " % ("dieta", "cena netto", "cena brutto"))
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("%-30s   |   %-40s   |   %-30s " %  (dieta, cena_netto, cena_brutto))
            print("---------------------------------------------------------------------------------------------------------------------------")        

    def select3(self):
        self.c.execute("SELECT dieta, cena_netto, cena_netto * 1.23 AS 'cena_brutto' FROM diety WHERE id_d=3;")
        res = self.c.fetchall()        
        for a in res:
            dieta = a[0]
            cena_netto = a[1]
            cena_brutto = a[2]
            print("%-30s   |   %-40s   |   %-30s " % ("dieta", "cena netto", "cena brutto"))
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("%-30s   |   %-40s   |   %-30s " %  (dieta, cena_netto, cena_brutto))
            print("---------------------------------------------------------------------------------------------------------------------------")       

    def select4(self):
        self.c.execute("SELECT dieta, cena_netto, cena_netto * 1.23 AS 'cena_brutto' FROM diety WHERE id_d=4;")
        res = self.c.fetchall()        
        for a in res:
            dieta = a[0]
            cena_netto = a[1]
            cena_brutto = a[2]
            print("%-30s   |   %-40s   |   %-30s " % ("dieta", "cena netto", "cena brutto"))
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("%-30s   |   %-40s   |   %-30s " %  (dieta, cena_netto, cena_brutto))
            print("---------------------------------------------------------------------------------------------------------------------------")       

    def select5(self):
        self.c.execute("SELECT dieta, cena_netto, cena_netto * 1.23 AS 'cena_brutto' FROM diety WHERE id_d=5;")
        res = self.c.fetchall()        
        for a in res:
            dieta = a[0]
            cena_netto = a[1]
            cena_brutto = a[2]
            print("%-30s   |   %-40s   |   %-30s " % ("dieta", "cena netto", "cena brutto"))
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("%-30s   |   %-40s   |   %-30s " %  (dieta, cena_netto, cena_brutto))
            print("---------------------------------------------------------------------------------------------------------------------------")       

    def select6(self):
        self.c.execute("SELECT dieta, cena_netto, cena_netto * 1.23 AS 'cena_brutto' FROM diety WHERE id_d=6;")
        res = self.c.fetchall()        
        for a in res:
            dieta = a[0]
            cena_netto = a[1]
            cena_brutto = a[2]
            print("%-30s   |   %-40s   |   %-30s " % ("dieta", "cena netto", "cena brutto"))
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("%-30s   |   %-40s   |   %-30s " %  (dieta, cena_netto, cena_brutto))
            print("---------------------------------------------------------------------------------------------------------------------------")       
c1= MySQLConnector("MySQL13")   
  

 
