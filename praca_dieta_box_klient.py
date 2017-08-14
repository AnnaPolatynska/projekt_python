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
            self.menu()
        else:
            print("---UWAGA---")  
            print("Błąd logowania")              
            
    def menu(self):       
        nav_s = input("Co chcesz zrobić? (K)-klub Fitness, będący punktem odbioru, (D)-diety - opisy, (Q)- powrót")
        while(nav_s != "Q" or nav_s != "q" or nav_s != "K" or nav_s != "k" or nav_s != "D" or nav_s != "d"):
            nav_s = input("Co chcesz dalej wybrać? (K)-klub Fitness, będący punktem odbioru, (D)-diety - opisy, (Q)- powrót");
            if(nav_s == "K" or nav_s == "k"):
                self.selectK()
            elif(nav_s == "D" or nav_s == "d"):
                self.selectD()
            elif(nav_s == "Q"or nav_s == "q"):
                print("Połączenie zakończone")
                self.conn.close()      
            else:
                print("------------------UWAGA------------------")  
                print("Wprowadzono niepoprawny kod, wybierz ponownie: \n")                        
  
  
    #menu wybór diety    
    def selectD(self):             
        nav_d = input("Jesteś w menu wybór diety, co chcesz zrobić dalej?  (O)-opis diet, (B)-wybierz swój dieta-BOX, (M)-menu główne, (Q)- wyjście")
        if(nav_d == "O" or nav_d == "o"):
            self.selectO()
        elif(nav_d == "B"or nav_d == "b"):
            self.selectB()
        elif(nav_k == "M"or nav_k == "m"):
            self.menu()             
        elif(nav_d == "Q"or nav_d == "q"):
            print("Połączenie zakończone")
            self.conn.close() 
        else:
            print("------------------UWAGA------------------")  
            print("Wprowadzono niepoprawny kod, wybierz ponownie: \n")  
                        
  
  
  
  
  
#menu wybór punktu odbioru    
    def selectK(self):             
        nav_k = input("Jesteś w menu punkt odbioru, co chcesz zrobić dalej? (P)-pokaż dostępne punkty odbioru, (W)-wybrać punkt odbioru, (M)-menu główne, (Q)- wyjście")
        if(nav_k == "P" or nav_k == "p"):
            self.selectP()
        elif(nav_k == "W"or nav_k == "w"):
            self.selectW()
        elif(nav_k == "Q"or nav_k == "q"):
            print("Połączenie zakończone")
            self.conn.close() 
        elif(nav_k == "M"or nav_k == "m"):
            self.menu()        
        else:
            print("------------------UWAGA------------------")  
            print("Wprowadzono niepoprawny kod, wybierz ponownie: ")  
            print(" ")             
  
  
# (P)-Pokaż wszystkie punkty odbioru = adresy punktów odbioru  
    def selectP(self):
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

 
           
#(W)-Wybrać punkty odbioru = wybór punktu odbioru
    def selectW(self):
        nav_w = input("Jaki punt odbioru wybierasz? podaj id punktu (1)-Klub Sportowy S4 (Warszawa), (2)-Szkoła tańca FEN, (3)-Klub Sportowy (S4 Piastów), (4)-Oxygen Fitness, (5)-Cross Klub Ursus, (6)-Fight Klub Pitbul, (Q)- wyjście do menu punkt odbioru")
        while(nav_w != "Q" or nav_w != "q" or nav_w != 1 or nav_w != 2 or nav_w != 3 or nav_w != 4 or nav_w != 5 or nav_w != 6):
            print(" ") 
            nav_w = input("Jaki punt odbioru wybierasz? podaj id punktu (1-6) lub (Q)-wyjście do menu punkty odbioru")
            if(nav_w == "1"):
                self.update1()
                print("wybrałeś punkt: Klub Sportowy S4 (Warszawa)")
                print(" ")
            elif(nav_w == "2"):
                self.update2()
                print("wybrałeś punkt: Szkoła tańca FEN")
                print(" ")
            elif(nav_w == "3"):
                self.update3()
                print("wybrałeś punkt: Klub Sportowy (S4 Piastów)")
                print(" ")
            elif(nav_w == "4"):
                self.update4()
                print("wybrałeś punkt: Oxygen Fitness")
                print(" ")
            elif(nav_w == "5"):
                self.update5()
                print("wybrałeś punkt: Cross Klub Ursus")
                print(" ")
            elif(nav_w == "6"):
                self.update6()
                print("wybrałeś punkt: Fight Klub Pitbul")
                print(" ")
            elif(nav_w == "Q" or nav_w == "q"):
                self.selectK()
            else:
                print("------------------UWAGA------------------")  
                print("Wprowadzono niepoprawny kod, wybierz ponownie: ")  
                print(" ") 
                nav_w = input("Jaki punt odbioru wybierasz? podaj id punktu (1-6)")                
               
        print("Połączenie zakończone")
        self.conn.close()    
                   
             
    def update1(self):
        self.c.execute("UPDATE klient SET id_o=1 where nazwisko = 'Dzida';")
        self.conn.commit()
        print("dane zaktualizowane")                           
    def update2(self):
        self.c.execute("UPDATE klient SET id_o=2 where nazwisko = 'Dzida';")
        self.conn.commit()
        print("dane zaktualizowane")                    
    def update3(self):
        self.c.execute("UPDATE klient SET id_o=3 where nazwisko = 'Dzida';")
        self.conn.commit()
        print("dane zaktualizowane")            
    def update4(self):
        self.c.execute("UPDATE klient SET id_o=4 where nazwisko = 'Dzida';")
        self.conn.commit()
        print("dane zaktualizowane")            
    def update5(self):
        self.c.execute("UPDATE klient SET id_o=5 where nazwisko = 'Dzida';")
        self.conn.commit()
        print("dane zaktualizowane")              
    def update6(self):
        self.c.execute("UPDATE klient SET id_o=6 where nazwisko = 'Dzida';")
        self.conn.commit()
        print("dane zaktualizowane") 
 
 
 #(O)-zapoznać się z ofertą = opisy diet
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



# (B) Kupno diety-BOXu
    def selectB(self):
        nav_b = input("Jaką dietę chcesz kupić? (1) dietę odchudzającą-egzotyczne smaki , (2) dietę odchudzjącą standardową, (3) dietę zdrowotną- wzmocnij serce, (4) dietę zdrowotną standardową, (5) dietę sportową - wytrzymałość, (6) dietę sportową - siła (Q)- wyjście do menu dieta")
        if(nav_b == "1"):
            self.update_1()
            print("zamówiłeś dietę odchudzającą-egzotyczne smaki. Twoje zamówienie czeka na opłatę.")
            print(" ")
        elif(nav_b == "2"):
            self.update_2()
            print("Zamówiłeś dietę odchudzjącą standardową. Twoje zamówienie czeka na opłatę.")
            print(" ")
        elif(nav_b == "3"):
            self.update_3()
            print("Zamówiłeś dietę zdrowotną- wzmocnij serce. Twoje zamówienie czeka na opłatę.")
            print(" ")
        elif(nav_b == "4"):
            self.update_4()
            print("Zamówiłeś dietę zdrowotną standardową. Twoje zamówienie czeka na opłatę.")
            print(" ")
        elif(nav_b == "5"):
            self.update_5()
            print("Zamówiłeś dietę dietę sportową - wytrzymałość. Twoje zamówienie czeka na opłatę.")
            print(" ")
        elif(nav_b == "6"):
            self.update_6()
            print("Zamówiłeś dietę dietę sportową - siła. Twoje zamówienie czeka na opłatę.")
            print(" ")    
        elif(nav_b == "Q" or nav_k == "q"):
            self.selectD()
        else:
            print("------------------UWAGA------------------")  
            print("Wprowadzono niepoprawny kod, wybierz ponownie: \n")  
            nav_b = input("Jaką dietę wybierasz? Podaj id diety (1-6) lub (Q)-wyjście do menu głównego")
              
                           
         
# (1-6) Wybór przy kupnie poszczególnych diet    
    def update_1(self):
        self.c.execute("UPDATE zamówienia SET id_d=1 where id_k = 9;")
        self.conn.commit()
        print("zamówienie złożone")   
    def update_2(self):
        self.c.execute("UPDATE zamówienia SET id_d=2 where id_k = 9;")
        self.conn.commit()
        print("zamówienie złożone")  
    def update_3(self):
        self.c.execute("UPDATE zamówienia SET id_d=3 where id_k = 9;")
        self.conn.commit()
        print("zamówienie złożone")  
    def update_4(self):
        self.c.execute("UPDATE zamówienia SET id_d=4 where id_k = 9;")
        self.conn.commit()
        print("zamówienie złożone")  
    def update_5(self):
        self.c.execute("UPDATE zamówienia SET id_d=5 where id_k = 9;")
        self.conn.commit()
        print("zamówienie złożone") 
    def update_6(self):
        self.c.execute("UPDATE zamówienia SET id_d=6 where id_k = 9;")
        self.conn.commit()
        print("zamówienie złożone") 
            
           
            
c1= MySQLConnector("MySQL13")   




 
     
     
     
     
     














