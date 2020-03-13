# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:02:41 2020

@author: Robert Spry
"""
from Station import Station
import unittest
#station_list=["Command,Science,Tactical,Engineering, Medical]

class TestStarship(unittest.TestCase):
    def setUp(self):
        self.test_station_instance=Station("Command")
        
    def test_score(self):
        self.assertTrue(self.test_station_instance.score==30)
        
    def test_crew_list(self):
        self.assertEqual(self.test_station_instance.crew_list,[])
    
    def test_number_of_crew(self):
        self.assertEqual(self.test_station_instance.number_of_crew,len(self.test_station_instance.crew_list))
    
    def test__str__(self):
        self.assertEqual(str(self.test_station_instance),"This is the Command station")
    
    def test__repr__(self):
        self.assertEqual(repr(self.test_station_instance),"This is the Command station with the following 0 people: [] and has score:30")
    

if __name__ == '__main__':
    unittest.main()          