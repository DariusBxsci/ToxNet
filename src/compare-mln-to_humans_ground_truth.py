import json, os, argparse

import pandas as pd
import itertools

from statsmodels.stats.inter_rater import cohens_kappa
import numpy as np 

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="input directory")
args = parser.parse_args()

#These should not be hard coded
human_ratings = pd.read_csv(os.path.join(args.input,'human-ratings.csv'))
ground_truth = pd.read_csv(os.path.join(args.input,'parsed-ground-truth.csv'))
mln_guesses = pd.read_csv(os.path.join(args.input,'mlnquery-results.csv'))

dfs = {'human':human_ratings,'synthetic':ground_truth, 'model':mln_guesses}

df = reduce(lambda left,right: pd.merge(left,right,on='id'), dfs.values())
df.to_csv(os.path.join(args.input,'amalgamated.csv'),index=False)


print df['difficulty'].value_counts()


#Human Model
cross_tab = pd.crosstab(df['human_toxidrome'],df['predicted_toxidrome'])
cross_tab.to_csv(os.path.join(args.input,'contingency_table_human_predicted.csv'))
#print cross_tab
as_array = cross_tab.values
#print np.diag(as_array).sum(), float(as_array.sum()) #0.381355932203
#print cohens_kappa(cross_tab)
'''
                  Simple Kappa Coefficient
              --------------------------------
              Kappa                     0.2532
              ASE                       0.0515
              95% Lower Conf Limit      0.1523
              95% Upper Conf Limit      0.3542

                 Test of H0: Simple Kappa = 0

              ASE under H0              0.0401
              Z                         6.3188
              One-sided Pr >  Z         0.0000
              Two-sided Pr > |Z|        0.0000
'''


#Human Synthetic 
cross_tab = pd.crosstab(df['human_toxidrome'],df['actual_toxidrome'])
cross_tab.to_csv(os.path.join(args.input,'contingency_table_human_synthetic.csv'))
as_array = cross_tab.values
#print np.diag(as_array).sum(), float(as_array.sum())
#0.161016949153
#print cohens_kappa(cross_tab)
'''
                  Simple Kappa Coefficient
              --------------------------------
              Kappa                     -0.0058
              ASE                       0.0410
              95% Lower Conf Limit      -0.0861
              95% Upper Conf Limit      0.0746

                 Test of H0: Simple Kappa = 0

              ASE under H0              0.0408
              Z                         -0.1413
              One-sided Pr >  Z         0.5562
              Two-sided Pr > |Z|        0.8876

'''

#Synthetic Model
cross_tab = pd.crosstab(df['actual_toxidrome'],df['predicted_toxidrome'])
cross_tab.to_csv(os.path.join(args.input,'contingency_table_synthetic_predicted.csv'))
as_array = cross_tab.values
#print np.diag(as_array).sum(),float(as_array.sum())
#0.134453781513
#print cohens_kappa(cross_tab)
'''
                  Simple Kappa Coefficient
              --------------------------------
              Kappa                     -0.0394
              ASE                       0.0359
              95% Lower Conf Limit      -0.1097
              95% Upper Conf Limit      0.0309

                 Test of H0: Simple Kappa = 0

              ASE under H0              0.0394
              Z                         -1.0021
              One-sided Pr >  Z         0.8418
              Two-sided Pr > |Z|        0.3163
'''
