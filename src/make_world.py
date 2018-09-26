#make world
import random, json, os  
from pprint import pprint 

person = {"type":"patient",
		   "name":"",
		   "intended_toxidrome":"",
		   "difficulty":"",
		   "random_number":"",
		   "presentation":[]}

nPatients = 240
n_max_features = 5
DATA_PATH = os.path.join('.','data')

toxidromes = {'serotonin_syndrome':['tachycardic',
									 'hypertensive',
									 'clonus',
									  'hyperreflexia',
									  'hyperthermic'],
				'sympathomimetic':["tachycardic",
								"hypertensive",
								"mydriatic",
								"diaphoretic",
								"agitated",
								"decreased_bowel_sounds",
								"tachypneic",
						  		"!clonus"],
				'sedative_hypnotic':["!hypertensive",
									"somnolent",
									"decreased_bowel_sounds",
									"bradypneic",
						    "!clonus"],
				'cholinergic':["bradycardic",
								"miotic",
								"diaphoretic",
								"increased_bowel_sounds",
					      "!clonus"],
				'anticholinergic': ["tachycardic",
									"hypertensive",
									"mydriatic",
									"dry_skin",
									"delirious",
									"decreased_bowel_sounds",
						   "!clonus"],
				'opioid':["!hypertensive",
							"miotic",
							"somnolent",
							"decreased_bowel_sounds",
							"bradypneic",
					 "!clonus"]
							}

def make_presentation(intended_toxidrome,db):
	#Assume that all presentations have five variables
	#Between 1 and 4 of of the five variables are pulled from the intended toxidrome
	#The rest are pulled randomly from the other toxidromes
	#If 1 variable is present from the intended toxidrome, then the presentation is hard; four, easy; medium is in between


	difficulty = random.choice(xrange(0,3))
	presentation = ""

	n_intended_features = n_max_features - difficulty
	n_distractor_features = difficulty

	intended_features = random.sample(toxidromes[intended_toxidrome],n_intended_features)
	distractor_features = []

	for _ in xrange(n_distractor_features):
		source_toxidrome = random.choice(toxidromes.keys())
		feature = random.choice(toxidromes[source_toxidrome])

		distractor_features += [feature]
		#Features in distractors carry one-quarter as much weight

	return (difficulty, list(set(intended_features + distractor_features)))

db = {n:person.copy() for n in xrange(2*nPatients)}

for n in xrange(2*nPatients):
	intended_toxidrome = random.choice(toxidromes.keys())

	db[n]["name"] = "patient_%d"%n
	db[n]["intended_toxidrome"] = intended_toxidrome
	db[n]["difficulty"], db[n]["presentation"] = make_presentation(intended_toxidrome,db)
	db[n]["random_number"] = random.random() #Can vectorize this if needed	

json.dump(db,open(os.path.join(DATA_PATH,"world.json"),"wb"))

json.dump({key:value for key,value in db.iteritems() if value["random_number"] > 0.5},
	  open(os.path.join(DATA_PATH,"world-train.json"),"wb"))

json.dump({key:value for key,value in db.iteritems() if value["random_number"] < 0.5},
	  open(os.path.join(DATA_PATH,"world-test.json"),"wb"))
