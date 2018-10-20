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

df = pd.read_excel('foodinsecurity.xlsx', sheetname = 'sheet1')
pprint(df)
