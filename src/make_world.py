#make world
#trying to not use genDB, nothing works even after installing Jython
import random, json 

from pprint import pprint 

person = {"type":"patient",
		   "name":"",
		   "intended_toxidrome":"",
		   "difficulty":"",
		   "presentation":[]}

nPatients = 240
n_max_features = 5
'''
toxidromes = {'serotonin_syndrome':{'tachycardic',
									 'hypertensive',
									 'clonus',
									  'hyperreflexia',
									  'hyperthermia',
				'sympathomimetic':{"tachycardic": 0.6,
								"hypertensive",
								"mydriatic": 0.6,
								"diaphoretic": 0.6,
								"decreased_bowel_sounds",
								"tachypneic",
				'sedative_hypnotic':{"eucardic",
									"normotensive",
									"normal_size_pupils",
									"diaphoretic",
									"decreased_bowel_sounds",
									"bradypneic",
				'cholinergic':{"bradycardic",
								"hypotensive",
								"miotic",
								"diaphoretic",
								"increased_bowel_sounds",
				'anticholinergic': {"tachycardic",
									"hypertensive",
									"mydriatic",
									"dry_skin",
									"decreased_bowel_sounds",
				'opioid':{"eucardic",
							"normotensive",
							"miotic",
							"diaphoretic",
							"decreased_bowel_sounds",
							"bradypneic"
							}
'''

toxidromes = {'serotonin_syndrome':['tachycardic',
									 'hypertensive',
									 'clonus',
									  'hyperreflexia',
									  'hyperthermic'],
				'sympathomimetic':["tachycardic",
								"hypertensive",
								"mydriatic",
								"diaphoretic",
								"decreased_bowel_sounds",
								"tachypneic"],
				'sedative_hypnotic':["eucardic",
									"normotensive",
									"normal_size_pupils",
									"diaphoretic",
									"decreased_bowel_sounds",
									"bradypneic"],
				'cholinergic':["bradycardic",
								"hypotensive",
								"miotic",
								"diaphoretic",
								"increased_bowel_sounds"],
				'anticholinergic': ["tachycardic",
									"hypertensive",
									"mydriatic",
									"dry_skin",
									"decreased_bowel_sounds"],
				'opioid':["eucardic",
							"normotensive",
							"miotic",
							"diaphoretic",
							"decreased_bowel_sounds",
							"bradypneic"]
							}

def make_presentation(intended_toxidrome,db):
	#Assume that all presentations have five variables
	#Between 1 and 4 of of the five variables are pulled from the intended toxidrome
	#The rest are pulled randomly from the other toxidromes
	#If 1 variable is present from the intended toxidrome, then the presentation is hard; four, easy; medium is in between


	difficulty = random.choice(xrange(1,4))
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

	return (difficulty, intended_features + distractor_features)

db = {n:person.copy() for n in xrange(nPatients)}

for n in xrange(nPatients):
	 db[n]["name"] = "patient_%d"%n
	 intended_toxidrome = random.choice(toxidromes.keys())
	 db[n]["intended_toxidrome"] = intended_toxidrome
	 db[n]["difficulty"], db[n]["presentation"] = make_presentation(intended_toxidrome,db)

json.dump(db,open("./data/world.json","wb"))