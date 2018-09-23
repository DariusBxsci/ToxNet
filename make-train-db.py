import json 

db = json.load(open('./world.json','rb'))

def convert_to_MLN(aDict):
	return "//%s\n"% aDict['name'] + '\n'.join(['log(%.02f) %s(%s)'%(odds,symptom,aDict["name"]) 
									for symptom, odds in aDict['presentation'].items()])

with open('world-train.db','wb') as outfile:
	print>>outfile,'\n'.join([convert_to_MLN(info) for id,info in db.iteritems()])
