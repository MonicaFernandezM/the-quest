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
        
        if len(self.records) == 0:
            self.records.append(record)
        else:
            for item in self.records:
                if record.score > item.score:
                    index = index(item)
                    self.records.insert(index, record)
            
        #if len(self.records) > 5:
            #self.records.remove(5)

        sql_connection = sqlite3.connect(self.database_name)
        sql_cursor = sql_connection.cursor()

        sql_command = "DELETE FROM scores"
        sql_cursor.execute(sql_command)
        sql_connection.commit()

        for record in self.records:
            sql_command_with_param = """INSERT INTO scores (name, score) VALUES (?, ?);"""
            data_tuple = (record.name, record.score)
            sql_cursor.execute(sql_command_with_param, data_tuple)
            sql_connection.commit()

        sql_connection.close()

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
