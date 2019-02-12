# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:02:36 2019

@author: Савчук Елена
"""

import pyarrow.parquet as parquet
# Used to train the baseline model

from sklearn.linear_model import LogisticRegression, LogisticRegressionCV

from sklearn.model_selection import GridSearchCV, StratifiedKFold







