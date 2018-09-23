#make world
#trying to not use genDB, nothing works even after installing Jython
import random

from pprint import pprint 

person = {"type":"patient",
		   "name":"",
		   "intended_toxidrome":"",
		   "presentation":[]}

nPatients = 2


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


db = {}

for n in xrange(nPatients):
	 db[n] = person 
	 intended_toxidrome = random.choice(toxidromes.keys())
	 db[n]["intended_toxidrome"] = intended_toxidrome

pprint(db)