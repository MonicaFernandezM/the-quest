#!/usr/bin/env python

import sqlite3

def main():
    database_name = "the_quest"
    
    #create_table(database_name)
    #clear_data(database_name) # To clean DB
    print_stats(database_name) # To query DB

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

main()