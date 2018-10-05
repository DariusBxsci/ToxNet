import json
from collections import defaultdict

world = json.load(open('./data/world-train-pure.json','r'))
toxidromes = defaultdict(list)

def convert_to_MLN(aDict):
	return "//%s\n"% aDict['name'] +'\n'.join(['%s(%s)'%(symptom,aDict["name"]) 
									for symptom in aDict['presentation']]) + '\n' + '%s(%s)'%(aDict['intended_toxidrome'],aDict["name"]) + '\n'

for _,patient in world.iteritems():
	toxidromes[patient['intended_toxidrome']].append(patient)

for toxidrome in toxidromes:
	with open('./data/%s.db'%toxidrome,'w') as fout:
		for patient in toxidromes[toxidrome]:
			print>>fout,convert_to_MLN(patient)+'\n'