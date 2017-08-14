# -*- coding: utf-8 -*-
import pymysql


# zainportowanie bazy danych
conn = pymysql.connect("localhost", "root2", "MySQL13", "dieta_box", charset='utf8mb4')
import pymysql
# interfejs dla klientów wyboru lokalizacji odbioru i dietaBoxu

#menu główne logowanie klienta 
#wybierz dowolny login i hasło dla klienta np. login: 'a_dzida', hasło: 'Dzida1!'

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
            nav_s = input("Co chcesz zrobić? (Z)-Zobaczyć punkty odbioru, (O)-opisy diet, (K)-kupić dietę, (Q)- powrót")
            while(nav_s != "Q" or nav_s != "q" or nav_s != "Z" or nav_s != "z" or nav_s != "O" or nav_s != "o" or nav_s != "K" or nav_s != "k"):
                nav_s = input("Co chcesz dalej wybrać? (Z)-Zobaczyć punkty odbioru, (O)-opisy diet, (K)-kupić dietę, (Q)- powrót");
                if(nav_s == "Z" or nav_s == "z"):
                    self.selectZ()
                elif(nav_s == "O" or nav_s == "o"):
                    self.selectO()
                elif(nav_s == "K" or nav_s == "k"):
                    self.selectK()
                elif(nav_s == "Q"or nav_s == "q"):
                    print("Połączenie zakończone")
                    self.conn.close()      
            
        else:
            print("---UWAGA---")  
            print("Błąd logowania")                
  
# (Z)-Zobaczyć punkty odbioru = adresy punktów odbioru        
    def selectZ(self):
        self.c.execute("SELECT id_o, nazwa_punktu, adres_punktu, miasto FROM punkty_odbioru;")
        res = self.c.fetchall() 
        print("%-10s   |   %-35s   |   %-30s   |   %-30s " % ("Id punktu", "klub sprotowy z punktem odbioru", "adres punktu odbioru", "miasto"))
        print("------------------------------------------------------------------------------------------------------------------------")        
        for p in res:
            id_o = p[0]
            nazwa_punktu = p[1]
            adres_punktu = p[2]
            miasto = p[3]
            print("%-10s   |   %-35s   |   %-30s   |   %-30s" % (id_o, nazwa_punktu, adres_punktu, miasto))
        print("------------------------------------------------------------------------------------------------------------------------")     

   

#  (O)-zapoznać się z ofertą = opisy diet
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



# (K) Kupno diety
    def selectK(self):
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
            self.select5()
            print("Zamówiłeś dietę dietę sportową - siła. Twoje zamówienie czeka na opłatę.")
            print(" ")    
                        
        elif(nav_k == "Q" or nav_k == "q"):
            print("Połączenie zakończone")
            self.conn.close() 
        else:
            print("------------------UWAGA------------------")  
            print("Wprowadzono niepoprawny kod, wybierz ponownie: ")  
            print(" ")                 




    # (1-6) Wybór poszczególnych diet    
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
            print(" ")       

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
            print(" ")       
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
            print(" ")         

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
            print(" ")            

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
            print(" ")        

    def select6(self):
        self.c.execute ("INSERT INTO zamówienia VALUES (8, 9 ,6 , 0, 'NIE','12-11-2017';")
        res = self.c.fetchall()   
              
        for a in res:
            dieta = a[0]
            cena_netto = a[1]
            cena_brutto = a[2]
            print("%-30s   |   %-40s   |   %-30s " % ("dieta", "cena netto", "cena brutto"))
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("%-30s   |   %-40s   |   %-30s " %  (dieta, cena_netto, cena_brutto))
            print(" ")       
            print("wprowadzono dane zamówienia:  ")  
            
 
            
            
c1= MySQLConnector("MySQL13")   




 
     
     
     
     
     














"""
    # DO POPRAWKI
    #(W)-Wybrać punkty odbioru = wybór punktu odbioru
        def selectW(self):
            nav_w = input("Jaki punt odbioru wybierasz? podaj id punktu (1)-Klub Sportowy S4 (Warszawa), (2)-Szkoła tańca FEN, (3)-Klub Sportowy (S4 Piastów), (4)-Oxygen Fitness, (5)-Cross Klub Ursus, (6)-Fight Klub Pitbul, (Q)- wyjście do menu głównego")
            while(nav_w != "Q" or nav_w != "q"):
                print("------------------UWAGA------------------")  
                print("Wprowadzono niepoprawny kod, wybierz ponownie: ")  
                # print(" ") 
                nav_w = input("Jaki punt odbioru wybierasz? podaj id punktu (1-6)")
                if(nav_w == "1"):
                    self.select1()
                    print("wybrałeś punkt: " + "(SELECT 'nazwa_punktu', 'adres_punktu', 'miasto' FROM punkty_odbioru WHERE 'id_o'=1 ;)")
                    print(" ")
                elif(nav_w == "2"):
                    self.select2()
                    print("wybrałeś punkt: " + "(SELECT 'nazwa_punktu', 'adres_punktu', 'miasto' FROM punkty_odbioru WHERE 'id_o'=2 ;)")
                    print(" ")
                elif(nav_w == "3"):
                    self.select3()
                    print("wybrałeś punkt: " + "(SELECT 'nazwa_punktu', 'adres_punktu', 'miasto' FROM punkty_odbioru WHERE 'id_o'=3 ;)")
                    print(" ")
                elif(nav_w == "4"):
                    self.select4()
                    print("wybrałeś punkt: " + "(SELECT 'nazwa_punktu', 'adres_punktu', 'miasto' FROM punkty_odbioru WHERE 'id_o'=4 ;)")
                    print(" ")
                elif(nav_w == "5"):
                    self.select5()
                    print("wybrałeś punkt: " + "(SELECT 'nazwa_punktu', 'adres_punktu', 'miasto' FROM punkty_odbioru WHERE 'id_o'=5 ;)")
                    print(" ")
                elif(nav_w == "6"):
                    self.select6()
                    print("wybrałeś punkt: ")
                    print("SELECT 'nazwa_punktu', 'adres_punktu', 'miasto' FROM punkty_odbioru WHERE 'id_o'=6 ;)")
                    self.c.execute("INSERT INTO zamówienia VALUES (8, 10, wyb_id_d, 6, 'NIE', 'NIE WYBRANO')")
                              
    
                    print("Połączenie zakończone")
                self.conn.close()    
           
    
    
    
    
       # def insertOdb(self):
      #      self.c.execute("INSERT INTO zamówienia VALUES (null, id_k, null, id_o, opłacono, od_kiedy)")
        #    self.conn.commit()
         #   print("wybrałeś punkt odbioru: " + id_o+ id) 
          #  nav_s = ''
"""