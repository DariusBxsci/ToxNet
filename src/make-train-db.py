import json, os


filenames = [os.path.join('.','data','world-%s.json'%condition) for condition in ['test','train']]

for filename in filenames:
	db = json.load(open(filename,'rb'))

	def convert_to_MLN(aDict):
		return "//%s\n"% aDict['name'] +'\n'.join(['%s(%s)'%(symptom,aDict["name"]) 
										for symptom in aDict['presentation']]) + '\n'

	with open(filename.replace('.json','.db'),'wb') as outfile:
		print>>outfile,'\n'.join([convert_to_MLN(info) for id,info in db.iteritems()])
