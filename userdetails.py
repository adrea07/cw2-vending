
import sqlite3
def user_details():
    db = sqlite3.connect('LOGIN')
    cur = db.cursor()
    username = input("CREATE username: ")
    password = input("CREATE password: ")
    email = input("ENTER email id: ")
    mobile = input("ENTER mobile number: ")
    address = input("ENTER address: ")
    cur.execute("DROP TABLE IF EXISTS LOGIN")

    cur.execute("CREATE TABLE IF NOT EXISTS LOGIN(USERNAME TEXT PRIMARY KEY,  PASSWORD TEXT, EMAIL_ID TEXT, MOBILE_NO INT, ADDRESS TEXT)")
    # cur.execute("Insert INTO login VALUES (2050,'heels',65,5)")
    try:
        cur.execute("""
            INSERT INTO LOGIN (USERNAME, PASSWORD, EMAIL_ID, MOBILE_NO, ADDRESS) 
            VALUES (?, ?, ?, ?, ?)
        """, (username, password, email, mobile, address))
        db.commit()  # Commit the changes
        print("User details saved successfully!")
        print(f"\n Welcome {username}")
    except sqlite3.IntegrityError:
        print("Error: Username already exists. Please choose a different username.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

def read_user(username):
    db = sqlite3.connect('LOGIN')
    cur = db.cursor()
    cur.execute("SELECT * FROM LOGIN WHERE username = ?", (username,))
    user = cur.fetchone()
    user_list = list(user)
    user_add = user_list[4]
    db.commit()
    db.close()
    return user_add



def existing_user():
    db = sqlite3.connect('LOGIN')
    cur = db.cursor()
    attempts = 3  
    while attempts > 0:
        username = input('Enter username: ')
        password = input('Enter password: ')

        cur.execute("SELECT * FROM LOGIN WHERE username = ? AND password = ?", (username, password))
        user = cur.fetchone()
        if user:
            print("\nAccess granted")
            print(f"Welcome back {username}!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"\nAccess Denied. Remaining attempts: {attempts}")
            else:
                print("\nLOGIN locked.")
    

    db.commit()
    db.close()
    return username

