 #RUN USING: python2 generate_rules.py predicates.txt

import random
import sys
import datagen
from datagen import *
from random import choice, randint, shuffle

toxidromes = open(sys.argv[1],'r').read().split(":")[0].split("\n")
attributes = open(sys.argv[1],'r').read().split(":")[1].split("\n")

#generate mln
print ("//Toxidromes")
print ("\n".join(toxidromes))

print ("//Attributes")
print ("\n".join(attributes))

print ("//Formulas")

formulae_str = "\n".join(toxidromes) + "\n" + "\n".join(attributes) + "\n" + ""
for t in toxidromes:
	for a in attributes:
		if len(t) > 1 and len(a) > 1:
			formulae_str += "\n" + ("log(0.8) " + t + " => " + a)

print (formulae_str)

f = open("toxic_complete.mln",'w')
f.write(formulae_str)
f.close()

#generate db
#for a simple db, just create patient profiles with just one main symptom

toxidrome_attributes = { "Sympathomimetic": "Bradycardic", \
                    "Anticholinergic": "Hypotensive", \
                    "Cholinergic": "Tachypneic", \
                    "Sedative_hypnotic":"Agitated", \
                    "Opioid":"Hyperpneic" }

num_patients = 100
patients = []
world = datagen.World()
#create random patients
for p in range(num_patients):

    tox = random.choice(list(toxidrome_attributes.keys()))    
    patient = datagen.Object("patient")
    patient.linkto("Has",tox)

    for s in attributes:
        #if this is a main attribute of this patient's toxidrome
        attr_prob = 0
        if s == toxidrome_attributes[tox]:
            attr_prob = 0.95
        else:
            attr_prob = 0.5
    
        #the probability of a patient having a certain attribute depends on their toxidrome's main attribute
        if random.random() <= attr_prob:
            patient.linkto("Is",s)

        world.addObject(patient)

print(world.getDatabase())