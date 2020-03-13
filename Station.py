#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:11:10 2020

@author: seanselzer
"""

class Station:
    
    def __init__(self, name):
        self.name = name
        self.score = 30
        self.crew_list = []
        self.number_of_crew = len(self.crew_list)
        
    def __str__(self):
        return "This is the {} station".format(self.name)
    
    def __repr__(self):
        return "This is the {} station with the following {} people: {} and has score:{}".format(self.name, self.number_of_crew, self.crew_list, self.score)