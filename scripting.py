#run everything in python 
#instead of minLearnShort.sh BASH script

#must run source env.sh first

import os 

from MLN import *


#Hard coding is bad; should log from cofig file

DB_path = os.path.join(".","ToxMLN","toxic_DB")
mln = MLN(os.path.join(DB_path,"wts.pypll.toxic_complete-toxic_complete.mln"))
mrf = mln.groundMRF(os.path.join(DB_path,"toxic_complete.db"))

queries = []