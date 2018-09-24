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

import json
from pprint import pprint 

results_file = 'world-test-pypll.world-train-logic.results'
results = [line.strip() for line in open(results_file,'rb').read().splitlines()]

most_likely_toxidrome = lambda patient: patient[max(xrange(len(patient)), key=lambda index: patient[index]['probability'])]["toxidrome"]

parsed_results = {}

world = json.load(open("./data/world.json",'rb'))

for result in results:
	probability,toxidrome_patient = result.split()
	toxidrome, patient = toxidrome_patient.replace("("," ").replace(")"," ").strip().split()

 	if patient in parsed_results:
 		tmp = parsed_results[patient]
 		tmp += [{"toxidrome":toxidrome, "probability":float(probability)}]
 		parsed_results[patient] = tmp 

 	else:
 		parsed_results[patient] = [{"toxidrome":toxidrome, "probability":float(probability)}]


with open('./data/analysis.csv','w') as fout:
	print>>fout,"id,predicted,actual,difficulty"
	for name in parsed_results:
		predicted_toxidrome = most_likely_toxidrome(parsed_results[name])

		_,id = name.split("_")
		actual_toxidrome = world[id]["intended_toxidrome"]
		print>>fout,','.join([id,predicted_toxidrome,actual_toxidrome,str(world[id]["difficulty"])])

"""
Questions that the results file are supposed to answer:
1. What is the most likely toxidrome?

"""