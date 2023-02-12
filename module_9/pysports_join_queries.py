#Title: pysports_join_queries.py
#Author: Ifeoluwa Adeniji
#Date: 12 Feb 2023

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
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER join team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("-- DISPLAYING TEAM RECORD --")
    
    for player in players:
        print("Player ID: {}\n First Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))
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