#make world
#trying to not use genDB, nothing works even after installing Jython
import random, json 

from pprint import pprint 

person = {"type":"patient",
		   "name":"",
		   "intended_toxidrome":"",
		   "difficulty":"",
		   "presentation":[]}

nPatients = 10
n_max_features = 5

toxidromes = {'sympathomimetic':{"tachycardic": 0.6,
								"hypertensive":0.6,
								"mydriatic": 0.6,
								"diaphoretic": 0.6,
								"decreased_bowel_sounds":0.6,
								"tachypneic":0.6},
				'sedative_hypnotic':{"eucardic":0.6,
									"normotensive":0.6,
									"normal_size_pupils":0.6,
									"diaphoretic":0.6,
									"decreased_bowel_sounds":0.6,
									"bradypneic":0.6},
				'cholinergic':{"bradycardic":0.6,
								"hypotensive":0.6,
								"miotic":0.6,
								"diaphoretic":0.6,
								"increased_bowel_sounds":0.6},
				'anticholinergic': {"tachycardic":0.6,
									"hypertensive":0.6,
									"mydriatic":0.6,
									"dry_skin":0.6,
									"decreased_bowel_sounds":0.6},
				'opioid':{"eucardic":0.6,
							"normotensive":0.6,
							"miotic":0.6,
							"diaphoretic":0.6,
							"decreased_bowel_sounds":0.6,
							"bradypneic":0.6}
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

	intended_features = random.sample(toxidromes[intended_toxidrome].items(),n_intended_features)
	distractor_features = []

	for _ in xrange(n_distractor_features):
		source_toxidrome = random.choice(toxidromes.keys())
		feature = random.choice(toxidromes[source_toxidrome].items())
		distractor_features += [feature]

	return (difficulty, dict(intended_features + distractor_features))

db = {n:person.copy() for n in xrange(nPatients)}

for n in xrange(nPatients):
	 db[n]["name"] = "patient_%d"%n
	 intended_toxidrome = random.choice(toxidromes.keys())
	 db[n]["intended_toxidrome"] = intended_toxidrome
	 db[n]["difficulty"], db[n]["presentation"] = make_presentation(intended_toxidrome,db)

json.dump(db,open("./world.json","wb"))