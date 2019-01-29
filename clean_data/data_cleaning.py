#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: data_cleaning.py
Author: Gene Jiang
Email: zhengrong.jiang@chiefclouds.com
Github: https://github.com/yourname
Description: 
"""

import numpy as np
import pandas as pd

loaddata = pd.DataFrame(pd.read_csv('test.csv'))

print(loaddata.duplicated())

