# This is my implementation of Bayes theorem

import numpy as np
import pandas as pd

import seaborn as sns
sns.set_style('white')
sns.set_context('talk')

import matplotlib.pyplot as plt

from empiricaldist import Pmf

cookie = Pmf.from_seq(['Bowl 1', 'Bowl 2'])

cookie['Bowl 1'] *= 0.75
cookie['Bowl 2'] *= 0.5
cookie.normalize()
print (cookie)




