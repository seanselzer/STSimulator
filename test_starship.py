# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:03:06 2020

@author: Robert Spry
"""
from Starship import Starship
import unittest

class TestStarship(unittest.TestCase):
    def setUp(self):
        self.test_starship_instance=Starship("Enterprise")
        
    def test_inital_power_level(self):
        self.assertTrue(self.test_starship_instance.power_level==1000)
            
    def test_inital_population(self):
        self.assertTrue(self.test_starship_instance.population==0)
        
    def test_name(self):
        self.assertTrue(isinstance(self.test_starship_instance.name,str))
        
    def test_inital_shield_level(self):
        self.assertTrue(self.test_starship_instance.shield_level==100)
        
    def test__str__(self):
        self.assertEqual(str(self.test_starship_instance), "A starship called Enterprise")
        
    def test__repr__(self):
        self.assertEqual(repr(self.test_starship_instance), "A starship called Enterprise with a power:1000, population: 0 and shield level:100")
        

if __name__ == '__main__':
    unittest.main()          