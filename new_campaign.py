import sqlite_connection
import os


def new_campaign():
    response = False
    print("Starting new campaign")
    camp_name = input("Enter the name of your campign: ")
    sqlite_file = camp_name + ".sqlite"

    if os.path.exists(sqlite_file):
        print("Campaign already exists")
        exit(1)

    conn = sqlite_connection.get_sqlite_conn(sqlite_file)

    # Create the campaign info table
    conn.execute('''CREATE TABLE campaign_info(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    campaign_name VARCHAR,
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP);
    ''')

    sql = '''INSERT INTO campaign_info (campaign_name) VALUES ("%s");''' % camp_name
    conn.execute(sql)

    # Create the characters table
    conn.execute('''CREATE TABLE characters(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        end_date TIMESTAMP,
        gold INTEGER,
        job VARCHAR,
        life_style VARCHAR);
        ''')

    while(True):
        char_name = input("Enter a characters name or 0 to exit! ")
        if char_name == "0":
            break
        gold = input("Enter the characters gold: ")
        job = input("Enter the characters city job: ")
        life_style = input("Enter the characters life style while in the city: ")

        sql = '''INSERT INTO characters (name, gold, job, life_style) VALUES ("%s", %s, "%s", "%s");''' % (char_name, gold, job, life_style)
        conn.execute(sql)

    conn.commit()