import pandas as pd

datafile = '../data/zscoredata.xls'
zscoredfile = '../tmp/zscoreddata.xls'

data = pd.read_excel(datafile)
data = (data-data.mean(axis=0))/(data.std(axis=0))

data.columns = ['Z'+i for i in data.columns]

data.to_excel(zscoredfile)