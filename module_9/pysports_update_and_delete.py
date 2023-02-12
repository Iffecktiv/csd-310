#Title: pysports_update_and_delete.py
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
def show_players(cursor,title):
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER join team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("\n --{} --".format(title))
    
    #Getting required results from players
    for player in players:
        print("Player ID: {}\n First Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))
        
#This shows whether connection is successful or not given the input
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    
    # To insert a new player
    add_player = ("INSERT INTO player(first_name, last_name, team_id) VALUES (%s, %s, %s)")
    # players' information
    player_data = ("Erik", "Ten Hag", 2)
    
    #adding new player information
    cursor.execute(add_player, player_data)
    db.commit()
    
    #showing records of old and new records
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")
    
    #New information
    update_player = ("UPDATE player SET team_id = 1, first_name = 'Marcus', last_name = 'Rashford' WHERE first_name = 'Erik'")
    cursor.execute(update_player)
    
    # information of players
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")
    
    delete_player = ("DELETE FROM player WHERE first_name = 'Marcus'")
    
    cursor.execute(delete_player)
    
    #information of players after delete
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")
    
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

    
    