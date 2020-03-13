# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:16:10 2020

@author: Robert Spry
"""

class Starship:
    def __init__(self,name):
        self.power_level = 1000
        self.population = 0
        self.name = "Enterprise"
        self.shield_level = 100
    
    def __str__(self):
        return "A starship called {}".format(self.name)
#    
    def __repr__(self):
        return "A starship called {} with a power:{}, population: {} and shield level:{}".format(self.name,self.power_level,self.population,self.shield_level)
    