import sqlite3


connexion = sqlite3.connect('databas.db')
con = connexion.cursor()
connexion.close()



def get_create():
  
  connexion = sqlite3.connect('databas.db')
  con = connexion.cursor()
  con.execute("DROP TABLE IF EXISTS cateogie_D")
  con.execute("DROP TABLE IF EXISTS cateogie_R")
  con.execute("CREATE TABLE IF NOT EXISTS categorie_D(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR)")
  con.execute("CREATE TABLE IF NOT EXISTS categorie_R(id INTEGER PRIMARY KEY AUTOINCREMENT , name VARCHAR)")
  connexion.commit()
  connexion.close()
 
  
  
  
def get_insert_categories():
  
 connexion = sqlite3.connect('databas.db')
 con = connexion.cursor()
 con.execute("INSERT INTO categorie_D(name)VALUES('manger'),('loyer'),('transport')")
 con.execute("INSERT INTO categorie_R(name)VALUES('busness'),('salaire'),('tontine')")
 connexion.commit()
 connexion.close()

def get_create_table_D() : 
   connexion = sqlite3.connect('databas.db')
   con = connexion.cursor()
   con.execute("DROP TABLE IF EXISTS depenses")
   con.execute("CREATE TABLE IF NOT EXISTS depenses(id INTEGER PRIMARY KEY AUTOINCREMENT , montant INTEGER, date TEXT , categorie_id INTEGER , FOREIGN KEY (categorie_id) REFERENCES categorie_D(id))")
   connexion.commit()
   connexion.close()
 
   
def get_insert_depenses():
  
 connexion = sqlite3.connect('databas.db')
 con = connexion.cursor()
 con.execute("DROP TABLE IF  EXISTS depenses")
 montant = int(input(" montant :: "))
 date= float(input(" Date :: "))
 categorie = int(input(" categories :: "))
 con.execute("INSERT INTO depenses (montant,date,categorie_id)VALUES(?,?,?)",(montant,date,categorie))
 connexion.commit()
 connexion.close()
  
   
   
def get_create_table_R():
   connexion = sqlite3.connect('databas.db')
   con = connexion.cursor()
   con.execute("DROP TABLE IF EXISTS revenue")
   con.execute("CREATE TABLE IF NOT EXISTS revenue(id INTEGER PRIMARY KEY  AUTOINCREMENT , montant INTEGER, date TEXT , categorie_id INTEGER ,FOREIGN KEY (categorie_id) REFERENCES categorie_R(id) )")
   connexion.commit()
   connexion.close()
  
   
def get_insert_revenue():
 connexion = sqlite3.connect('databas.db')
 con = connexion.cursor()
 con.execute("DROP TABLE IF EXISTS revenue")
 montant = int(input(" montant :: "))
 date= float(input(" Date :: "))
 categorie = int(input(" categories :: "))
 con.execute("INSERT INTO revenue (montant,date,categorie_id)VALUES(?,?,?)",(montant,date,categorie))
 connexion.commit()
 connexion.close()
      
  
  
get_create()
get_insert_categories()
get_create_table_D()
get_create_table_R()
 
def menu():
 print("DASBORD USER")
 print("\t\t\t\t")
 print(" 1 : ENRIGISTRE UNE DEPENSES ")
 print(" 2 ; ENRIGISTRE UNE REVENUE ")
 print(" 3 : VOIR L'ECART ENTRE DEPENSES AND REVENUE ")
 choix = int(input(" entrer une choix  :: "))
 if choix == 1 :
    get_insert_depenses()
    print("enrigistrement valider  !!!! ")
 elif  choix == 2 :
  get_insert_revenue()
  print("enrigistrement valider !!!! ")  
  
 
menu()
connexion.close()   