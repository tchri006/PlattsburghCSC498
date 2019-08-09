import os.path
import csv
import sqlite3
from os import path
from sqlite3 import Error

def db_create(db_name):                             #Create database
    try:
        conn = sqlite3.connect(db_name)             #Connect to database
        c = conn.cursor()                           #create cursor object
        c.execute('''CREATE TABLE concerts(         
            YEAR int, 
            DAY text, 
            DATE text, 
            TIME text, 
            ARTIST text, 
            "APPEARING WITH" text, 
            VENUE text, 
            "PRICE, Student" real, 
            "PRICE, public" real)'''
            )                                       #Create table named 'concerts' with entries for year, day, date, time, artist, appearing with, venue, student price, and public price
    except Error as e:                              #Exception handling
        print(e)
    finally:        
        conn.commit()                               #Commit changes
        conn.close()                                #Close database

def db_input_data(db_name, csv_name):               #Add data from csv file
    try:
        conn = sqlite3.connect(db_name)             #Connect to database
        c = conn.cursor()                           #Create cursor object
        with open(csv_name, newline = '') as csvfile:                               #Open csv file
            reader = csv.reader(csvfile, delimiter = ',', quotechar = '"')          #Create reader object with comma delimiter and " quote character
            next(reader, None)                                                      #Skip header row
            for row in reader:
                c.execute('''
                    INSERT INTO concerts(YEAR, DAY, DATE, TIME, ARTIST, "APPEARING WITH", VENUE, "PRICE, Student", "PRICE, public")
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', row[:9]
                    )                                           #Insert data from csv into the 'concerts' table
    except Error as e:              #Exception handling
        print(e)
    finally:
        conn.commit()               #Commit changes
        conn.close()                #Close database

def main():
    csv = input("Enter the name of the csv file to use: ")          #Prompt user to enter name of csv file to be used
    while not ".csv" in csv:
        csv = input("The file " + csv + " is not a csv file. Please enter a csv: ")     #If filename does not contain ".csv" ask user for another filename
    while not path.exists(csv):
        csv = input("The file " + csv + " does not exist. Please enter another: ")      #If the file entered does not exist ask user for another filename

    database = input("Enter the name of the database to edit: ")    #Prompt user to enter name of database file to be edited
    while not ".db" in database:
        database = input("The file " + database + " is not a database. Please enter a database: ")  #If filename does not contain ".db" ask user for another filename
    if not path.exists(database):
        print("That file does not exist. A database will be created.")      #If the file entered does not exist, tell user it will be created
        db_create(database)                                                 #Create the database
        print("The database " + database + " has been created.")            #Tell user the database has been created
    db_input_data(database, csv)                #Input data from the specified csv file to the specified database
    print("Data from " + csv + " has been added to " + database + ".")

if __name__ == '__main__':
    main()
