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
    excel_data = 'foodinsecurity.xlsx'
    #countyhungerdata = pd.read_excel('foodinsecurity.xlsx', sheet_name = 'CountyData')
    countyhungerdata = CountyData(excel_data, 'CountyData')
    pprint(countyhungerdata)


def CountyData(excel_data, sheet_name):
    columns = ['County', 'Population', 'Rate', 'Individuals', '% below 165% poverty', '% between 165% and 185% poverty', '% above 185% poverty']
    countydatadf =pd.read_excel(excel_data, sheet_name = sheet_name, names = columns)
    countydatadf.drop(['% below 165% poverty', '% between 165% and 185% poverty', '% above 185% poverty'], axis = 1, inplace = True)
    countydatadf.drop([254], axis = 0, inplace = True)
    countydatadf.sort_values(['Individuals'],ascending = False, inplace = True)
    countydatadf.reset_index(drop = True, inplace = True)
    
    return(countydatadf)
    
if __name__== "__main__":
  Main()
