import pygame as pg 

class Record():
     def __init__(self, score, name):
         self.score = score
         self.name = name 

class Records():
    def __init__(self):
         self.records = []
    
    def add_record(self, record):
        self.records.append(record)
        #save in data base
        pass

    def get_records(self):
        return self.records
        # get from data base
