import json 

db = json.load(open('./data/world.json','rb'))

def convert_to_MLN(aDict):
	return "//%s\n"% aDict['name'] + '%s(%s)\n'%(aDict['intended_toxidrome'],aDict['name'])+'\n'.join(['%s(%s)'%(symptom,aDict["name"]) 
									for symptom in aDict['presentation']]) + '\n'

with open('./data/world-train.db','wb') as outfile:
	print>>outfile,'\n'.join([convert_to_MLN(info) for id,info in db.iteritems()])
