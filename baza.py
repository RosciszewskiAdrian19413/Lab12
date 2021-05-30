import sqlite3

if __name__ == "__main__":

    conn = sqlite3.connect('database.db')
    print("Otwarto Baze Danych.")
    
    conn.execute('CREATE TABLE pracownicy (imienazwisko TEXT, nrpracownika TEXT, adres TEXT)')
    print("Utworzono Tabele pracownicy")
    
    conn.close()
    print("Zamknieto Baze Danych")
    
    
    conn = sqlite3.connect('database.db')
    print("Otwarto Baze Danych.")
    cur = conn.cursor()
    
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Adrian Kowalski','1','Gdansk') )
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Pawel Kowalski','2','Gdansk') )
    conn.commit()
    
    cur.execute('SELECT * FROM pracownicy ORDER BY nrpracownika')
    print(cur.fetchall())
    
    conn.close()
    print("Zamknieto Baze Danych.")