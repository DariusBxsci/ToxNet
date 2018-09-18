#run everything in python 
#instead of minLearnShort.sh BASH script

#must run source env.sh first

import os, json  

from MLN import *
from mlnQueryTool import MLNInfer



#Hard coding is bad; should log from cofig file

DB_path = os.path.join(".","ToxMLN","toxic_DB")
mln = os.path.join(DB_path,"wts.pypll.toxic_complete-toxic_complete.mln")
mrf = os.path.join(DB_path,"toxic_complete.db")

queries = ["Anticholinergic","Cholinergic","Sedative_hypnotic","Opioid","Sympathomimetic"]

#inference
inf = MLNInfer()
mlnFiles = mln
output_filename = "results.txt"

allResults = {}

tasks = [("MC-SAT","PyMLNs")]

for method,engine in tasks:
	for query in queries:
		allResults[query] = inf.run(mln,mrf,method,query,engine,
			output_filename, saveResults=True, maxSteps=500)

json.dump(allResults,open("test.json",'wb'))