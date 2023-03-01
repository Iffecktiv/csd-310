#Title: whatabbook.py
#Author: Ifeoluwa Adeniji
#Date: 28 Feb 2023
#Description: WhatABook program

# This connects our MySQL with python. It also imports
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "host" : input("\nHost: "), #localhost
    "user" : input("\nUsername: "), #whatabook_user
    "password" : input("\nPassword: "), #MySQL8IsGreat!
    "database" : input("\nDatabase: "), #whatabook
    "raise_on_warnings" : True
    }

def show_menu():
    print("\n-- Main Menu--")

    print(" 1. View Books\n 2. View Store Locations\n 3. My Account\n 4. Exit Program")

    try:
        choice = int(input("\n Please enter a number from 1-4: "))

        return choice
    except ValueError:
        print("\n error detected, program terminated...\n")

        sys.exit(0)
#This shows us the books from the store
def show_books(_cursor):
    # inner join query 
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # get the results from the cursor object 
    books = _cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")
    
    # iterate over the player data set and display the results 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\ DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

#This checks the user id
def validate_user():

    try:
        user_id = int(input("\n Please enter your customer id: "))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id
    
    except ValueError:
        print("\n Invalid number, program terminated...\n")

        sys.exit(0)
# This shows the account menu
def show_account_menu():

    try:
        print("\n      -- Customer Menu --")
        print(" 1. Wishlist\n 2. Add Book\n 3. Main Menu")
        account_option = int(input("\n Please enter a number from 1-4: "))

        return account_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    """ query the database for a list of books added to the users wishlist """

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n-- DISPLAYING WHATABOOK WISHLIST ITEMS --")

    for book in wishlist:
        print("Book Name: {}\n Author: {}\n".format(book[4], book[5]))
        
#This shows the books that are not on the user's wishlist
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details " "FROM book " "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n-- DISPLAYING WHATABOOK AVAILABLE BOOKS --")

    for book in books_to_add:
        print("Book Id: {}\nBook Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

# try/catch block for handling potential MySQL database errors
try:
    
    db = mysql.connector.connect(**config) 

    cursor = db.cursor() 
    print("\n  Welcome to the WhatABook Application! ")

    user_selection = show_menu() # show the main menu 

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        # if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user selects option 3, call the validate_user method to validate the entered user_id 
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    # commit the changes to the database 
                    db.commit() 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please try again...")

                # show the account menu 
                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please try again...")
            
        # show the main menu
        user_selection = show_menu()

    print("\nProgram terminated...")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)
#close the connection to MySQL
finally:

    db.close()