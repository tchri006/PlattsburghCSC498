import os.path
import csv
import sqlite3
from sqlite3 import Error
from os import path

def create_csv(csv_name, db_name):                          #Create CSV file and input data from database
    try:
        conn = sqlite3.connect(db_name)                     #Connect to the database
        c = conn.cursor()                                   #Create cursor object
        header = []                                         #Create header list
        for column in c.execute('''SELECT * FROM concerts''').description:  #Get column names
            header.append(column[0])                        #Add column names to list
        c.execute('''
        SELECT * FROM concerts
        ''')                                                #Select all data from the concerts table in the database
        data = c.fetchall()                                 #Fetch all data selected from table
        with open(csv_name, 'w') as csvfile:                #Open CSV file
            writer = csv.writer(csvfile, delimiter = ',',   #Create writer object with comma delimiter
            quotechar = '"',                                #Use " as quote character
            lineterminator = '\n'                           #Use the newline character as the line terminator
            )
            writer.writerow(header)                         #Write header to the CSV file
            writer.writerows(data)                          #Write the data to the CSV file
    except Error as e:                                      #Exception handling
        print(e)
    finally:
        conn.close                                          #Close database


def main():
    database = input("Please enter the name of the database file to use: ")                         #Prompt user to enter the name of the database they wish to use
    while not ".db" in database:
        database = input("The file " + database + " is not a database. Please enter a database: ")  #If the filename entered is not a database, prompt user to enter another
    while not path.exists(database):
        database = input("The file " + database + " does not exist. Please enter another: ")        #If the file entered does not exist, prompt the user to enter another

    csv_name = input("Please enter the name of the csv file to create: ")                           #Prompt user to enter the name of the CSV file they wish to create
    while not ".csv" in csv_name:
        csv_name = input("The file " + csv_name + " is not a csv file. Please enter a csv: ")       #If the filename entered is not a CSV file, prompt user to enter another
    create_csv(csv_name, database)                                                                  #Create the CSV file
    
    print(csv_name + " has been created.")


if __name__ == '__main__':
    main()