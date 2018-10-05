"""
0.616800  anticholinergic(patient_210)     
0.724800  anticholinergic(patient_211)     
0.569000  anticholinergic(patient_213)     
0.074800  opioid(patient_210)              
0.286200  opioid(patient_211)              
0.076400  opioid(patient_213)              
0.614200  serotonin_syndrome(patient_210)  
0.603200  serotonin_syndrome(patient_211)  
0.936200  serotonin_syndrome(patient_213)  
"""

import json, os, argparse
from pprint import pprint 

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="input path (file or directory)")
args = parser.parse_args()

if os.path.isdir(args.input):
	DIR_PATH = args.input
	results_filenames = [os.path.join(args.input,filename) for filename in os.listdir(args.input)
							if filename.endswith('.results')]
elif os.path.isfile(args.input):
	DIR_PATH = os.path.dirname(os.path.realpath(args.input))
	#Hole here. Not checking whether this file actually contains results
	results_filenames = [args.input]

results = [line.strip() for results_filename in results_filenames 
					for line in open(results_filename,'rb').read().splitlines()]

most_likely_toxidrome = lambda patient: patient[max(xrange(len(patient)), key=lambda index: patient[index]['probability'])]["toxidrome"]

parsed_results = {}

#world = json.load(open("./data/world.json",'rb'))

for result in results:
	probability,toxidrome_patient = result.split()
	toxidrome, patient = toxidrome_patient.replace("("," ").replace(")"," ").strip().split()

 	if patient in parsed_results:
 		tmp = parsed_results[patient]
 		tmp += [{"toxidrome":toxidrome, "probability":float(probability)}]
 		parsed_results[patient] = tmp 

 	else:
 		parsed_results[patient] = [{"toxidrome":toxidrome, "probability":float(probability)}]

json.dump(parsed_results,open(os.path.join(DIR_PATH,'parsed-mlnquery-results.json'),'w'))

with open(os.path.join(DIR_PATH,'mlnquery-results.csv'),'w') as fout:
	print>>fout,"id,toxidrome"
	for patient, toxidromes in parsed_results.iteritems():
		_,id = patient.split('_')
		predicted_toxidrome = most_likely_toxidrome(toxidromes)
		print>>fout,'%s,%s'%(id,predicted_toxidrome)