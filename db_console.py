#!/usr/bin/env python

import sqlite3

def main():
    database_name = "the_quest"
    
    #create_table(database_name)
    #clear_data(database_name) # To clean DB
    print_stats(database_name) # To query DB
    #insert_scores(database_name, 12, "Sabrina")
    #insert_scores(database_name, 12, "Cristina")
    #insert_scores(database_name, 24, "Monica")
    print(find_smallest(database_name))
    remove_value(database_name, 17)
    print_stats(database_name)
    print(is_bigger(database_name, 11))
    print(is_bigger(database_name, 17))
    print(is_bigger(database_name, 32))
    print(database_size(database_name))

def create_table(database_name):
    print("Trying to create table")
    try:
        sql_command = """CREATE TABLE `scores` (
        id integer PRIMARY KEY ASC AUTOINCREMENT NOT NULL DEFAULT '0',
        name text NOT NULL default '',
        score integer unsigned NOT NULL default '0'
        );"""

        sql_connection = sqlite3.connect(database_name)
        sql_cursor = sql_connection.cursor()
        sql_cursor.execute(sql_command)
        sql_connection.commit()
        sql_connection.close()
        print("Done\n")
    except:
        print("Failed. Probably DB exists\n")
        pass

def clear_data(database_name):
    print("Deleting table")
    sql_connection = sqlite3.connect(database_name)
    sql_cursor = sql_connection.cursor()

    sql_command = "DELETE FROM scores"

    sql_cursor.execute(sql_command)
    sql_connection.commit()
    sql_connection.close()
    print("Done\n")

def print_stats(database_name):
    sql_connection = sqlite3.connect(database_name)
    sql_cursor = sql_connection.cursor()

    sql_command = """SELECT * FROM scores"""

    sql_cursor.execute(sql_command)
    for row in sql_cursor.fetchall():
        print("Scores: {0} {1} {2}".format(row[0], row[1], row[2]))

    sql_connection.commit()
    sql_connection.close()

def insert_scores(database_name, score, name):
    sql_connection = sqlite3.connect(database_name)
    sql_cursor = sql_connection.cursor()

    sql_command = """INSERT INTO scores (name, score) VALUES (?, ?);"""
    data_tuple = (name, score)
    sql_cursor.execute(sql_command, data_tuple)
    sql_connection.commit()

    for row in sql_cursor.fetchall():
        print("Scores: {0} {1} {2}".format(row[0], row[1], row[2]))

    sql_connection.close()

def find_smallest(database_name):
    smallest_value = 9999
    smallest_index = 0 
    sql_connection = sqlite3.connect(database_name)
    sql_cursor = sql_connection.cursor()    

    sql_command = """SELECT * FROM scores"""

    sql_cursor.execute(sql_command)
    for row in sql_cursor.fetchall():
        if smallest_value > row[2]:
            smallest_value = row[2]
            smallest_index = row[0]
        #print("Scores: {0} {1} {2}".format(row[0], row[1], row[2]))

    sql_connection.commit()
    sql_connection.close()
    return smallest_index

def remove_value(database_name, index):
    sql_connection = sqlite3.connect(database_name)
    sql_cursor = sql_connection.cursor()

    sql_command = "DELETE FROM scores WHERE id = ?"

    sql_cursor.execute(sql_command, (index,))
    sql_connection.commit()
    sql_connection.close()

def is_bigger(database_name, score):
    sql_connection = sqlite3.connect(database_name)
    sql_cursor = sql_connection.cursor()    

    sql_command = """SELECT * FROM scores"""

    sql_cursor.execute(sql_command)
    for row in sql_cursor.fetchall():
        if score > row[2]:
            return True 

    sql_connection.commit()
    sql_connection.close()
    return False

def database_size(database_name):
    sql_connection = sqlite3.connect(database_name)
    sql_cursor = sql_connection.cursor()    

    sql_command = """SELECT COUNT(*) FROM scores"""

    sql_cursor.execute(sql_command)
    numberOfRows = sql_cursor.fetchone()[0]

    sql_connection.commit()
    sql_connection.close()
    return numberOfRows

main()