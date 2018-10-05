import json, os, argparse
import pandas as pd 
from pprint import pprint 

from statsmodels.stats.inter_rater import cohens_kappa
from sklearn_pandas import DataFrameMapper
'''
	The predictions of the algorithm are compared against:
	1. known labels of the synthetic data ("ground truth")
	2. guesses of two toxicologists

	The purpose of this file is to convert the data representing (2) from JSON into CSV 
	so that a later step can join (1) with (2) and the algorithm's predictions into one DataFrame
'''


parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="input directory")
args = parser.parse_args()

fellows = ['tak','barbuto']
filenames = ['included in program-%s.csv'%fellow for fellow in fellows]

dfs = [pd.read_csv(os.path.join(args.input, filename), skipinitialspace=True) 
			for filename in filenames] 

dfs[0] = dfs[0].rename(columns = {'censored':'tak-censored'})
dfs[1] = dfs[1].rename(columns = {'censored':'barbuto-censored'})

dfs[0]['tak_toxidrome'] = dfs[0]['tak_toxidrome'].astype("category")
dfs[1]['barbuto_toxidrome'] = dfs[1]['barbuto_toxidrome'].astype("category")

df = dfs[0].merge(dfs[1],on='id')
df.to_csv(os.path.join(args.input,'combined-fellow-ratings.csv'),index=False)

'''
#Quality check
print dfs[1]['barbuto_toxidrome'].value_counts()
print dfs[0]['tak_toxidrome'].value_counts()
'''
omitting_censored = df.loc[(df['tak-censored']=='no') | (df['barbuto-censored']=="no")]
omitting_censored = omitting_censored.loc[omitting_censored['tak_toxidrome']!="n/a"]
#At least one person rated it? Perhaps there are better ways 
#print len(df) #217
#print len(omitting_censored) #191
omitting_censored.to_csv(index=False)
crosstab = pd.crosstab(omitting_censored['tak_toxidrome'],omitting_censored['barbuto_toxidrome'])
crosstab.to_csv(os.path.join(args.input,"fellow-pivot-table.csv"))

crosstab = crosstab.drop(crosstab.index[2])
print crosstab

'''
                  Simple Kappa Coefficient
              --------------------------------
              Kappa                     0.8145
              ASE                       0.0314
              95% Lower Conf Limit      0.7530
              95% Upper Conf Limit      0.8760

                 Test of H0: Simple Kappa = 0

              ASE under H0              0.0332
              Z                         24.5027
              One-sided Pr >  Z         0.0000
              Two-sided Pr > |Z|        0.0000
'''
print cohens_kappa(crosstab)