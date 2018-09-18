#run everything in python 
#instead of minLearnShort.sh BASH script

from MLN import *


#Hard coding is bad; should log from cofig file
mln = MLN("wts.pypll.toxic_complete-toxic_complete.mln")
mrf = mln.groundMRF("toxic_complete.db")

queries = []