import json, os, argparse
from pprint import pprint 

'''
	The predictions of the algorithm are compared against:
	1. known labels of the synthetic data ("ground truth")
	2. guesses of two toxicologists

	The purpose of this file is to convert the data representing (1) rom JSON into CSV 
	so that a later step can join (1) with (2) and the algorithm's predictions into one DataFrame
'''

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="input file")
args = parser.parse_args()

DIR_PATH = os.path.dirname(os.path.realpath(args.input))
db = json.load(open(args.input,'r'))

with open(os.path.join(DIR_PATH,'parsed-ground-truth.csv'),'w') as fout:
	print>>fout,",".join(["id","actual_toxidrome","difficulty"])
	for id,payload in db.iteritems():
		print>>fout,','.join([id,payload['intended_toxidrome'],str(payload['difficulty'])])