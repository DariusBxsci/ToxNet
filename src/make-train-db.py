import json 

db = json.load(open('./data/world.json','rb'))

def convert_to_MLN(aDict):
	return "//%s\n"% aDict['name'] + '%s(%s)\n'%(aDict['intended_toxidrome'],aDict['name'])+'\n'.join(['log(%.02f) %s(%s)'%(odds,symptom,aDict["name"]) 
									for symptom, odds in aDict['presentation'].items()]) + '\n'

with open('./data/world-train.db','wb') as outfile:
	print>>outfile,'\n'.join([convert_to_MLN(info) for id,info in db.iteritems()])
