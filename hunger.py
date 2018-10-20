#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:10:41 2018

@author: ramyaprasad
"""

from pprint import pprint
import pandas as pd
import sys
import re

def Main():
    countyhungerdata = pd.read_excel('foodinsecurity.xlsx', sheet_name = 'CountyData')
    #countyhungerdata = CountyData(countyhungerdata)
    pprint(countyhungerdata)
    #pprint(countyhungerdata)



#def CountyData(countydatadf):
    #return(countydatadf)
    
if __name__== "__main__":
  Main()
