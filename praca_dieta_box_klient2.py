# -*- coding: utf-8 -*-
import pymysql


# zainportowanie bazy danych
conn = pymysql.connect("localhost", "root2", "MySQL13", "dieta_box", charset='utf8mb4')
import pymysql





class MySQLConnector:
    def __init__(self, passwd):
        self.passwd = passwd
        self.conn = pymysql.connect("localhost", "root2", "MySQL13", "dieta_box", charset='utf8mb4')
        self.c = self.conn.cursor()
        print("Połączenie ustanowione")
        nav_k = ''
        while(nav_k != "Q"):
            nav_k = input("Co chcesz zrobić? (P)-Wybrać punkty odbioru, (D)-Kupić dietę, (Q)- wyjście")
            if(nav_k == "P"):
                self.selectP()
            elif(nav_k == "D"):
                self.selectD()   
        print("Połączenie zakończone")
        self.conn.close()    
    def selectP(self):
        self.c.execute("SELECT nazwa_punktu, adres_punktu, miasto FROM punkty_odbioru ORDER BY miasto;")
        res = self.c.fetchall()        
        for p in res:
            nazwa_punktu = p[0]
            adres_punktu = p[1]
            miasto = p[2]
            print("%-30s %-30s %-30s" % (nazwa_punktu, adres_punktu, miasto))
    def selectD(self):
        self.c.execute("SELECT dieta, opis, cena_netto * 1.23 AS 'cena_brutto' FROM diety;")
        res = self.c.fetchall()        
        for d in res:
            dieta = d[0]
            opis = d[1]
            cena_brutto = d[2]
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("%-30s   |   %-140s   |   %-30s " % ("dieta", "   opis diety   ", "cena brutto"))
            print("%-30s   |   %-140s   |   %-30s " %  (dieta, opis, cena_brutto))
    
    
    

    
    
  
c1 = MySQLConnector("MySQL13")