#Title: mysql_test.py
#Author: Ifeoluwa Adeniji
#Date: 5 Feb 2023

#Connects MySQL with Python
import mysql.connector
from mysql.connector import errorcode

#Configuration data for database
config = {
    "host" : input("\nHost: "),
    "user" : input("\nUsername: "),
    "password" : input("\nPassword: "),
    "database" : input("\nDatabase: "),
    "raise_on_warnings" : True
    }

#Shows whether connection is successful or not given the input
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()
    print("-- DISPLAYING TEAM RECORD --")
    
    for team in teams:
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))
    cursor.execute("SELECT player_id, first_name, last_name FROM player")
    
    players = cursor.fetchall()
    print ("\n-- DISPLAYING PLAYER RECORDS --")
    
    for player in players:
        print(" Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], players[3]))

    input("\nPress any key to continue... ")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\nThe supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\nThe specified database does not exist.")
    else:
        print(err)
        
finally:
    db.close()