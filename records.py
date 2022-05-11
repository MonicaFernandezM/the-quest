import pygame as pg 
import sqlite3

class Record():
     def __init__(self, name, score):
         self.name = name 
         self.score = score
         
class Records():
    def __init__(self):
         self.records = []
         self.database_name = "the_quest"
    
    def add_record(self, record):
        if self.is_bigger(self.database_name, record.score):
            self.insert_scores(self.database_name, record.score, record.name)
            if self.database_size(self.database_name) > 5:
                index = self.find_smallest(self.database_name)
                self.remove_value(self.database_name, index)
            self.records = []
            return self.get_records()

    def get_records(self):
        sql_connection = sqlite3.connect(self.database_name)
        sql_cursor = sql_connection.cursor()

        sql_command = """SELECT * FROM scores"""
        sql_cursor.execute(sql_command)
        for row in sql_cursor.fetchall():
            self.records.append(Record(row[0], row[1], row[2]))
    
        sql_connection.commit()
        sql_connection.close()

        return self.records

    def insert_scores(self, database_name, score, name):
        sql_connection = sqlite3.connect(database_name)
        sql_cursor = sql_connection.cursor()

        sql_command = """INSERT INTO scores (name, score) VALUES (?, ?);"""
        data_tuple = (name, score)
        sql_cursor.execute(sql_command, data_tuple)
        sql_connection.commit()

        for row in sql_cursor.fetchall():
            print("Scores: {0} {1} {2}".format(row[0], row[1], row[2]))

        sql_connection.close()

    def find_smallest(self, database_name):
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

    def remove_value(self, database_name, index):
        sql_connection = sqlite3.connect(database_name)
        sql_cursor = sql_connection.cursor()

        sql_command = "DELETE FROM scores WHERE id = ?"

        sql_cursor.execute(sql_command, (index,))
        sql_connection.commit()
        sql_connection.close()

    def is_bigger(self, database_name, score):
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

