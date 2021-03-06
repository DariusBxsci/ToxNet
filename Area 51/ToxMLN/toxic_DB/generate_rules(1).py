 #RUN USING: python2 generate_rules.py predicates.txt

import random, sys, json 

toxidromes = open(sys.argv[1],'r').read().split(":")[0].split("\n")
attributes = open(sys.argv[1],'r').read().split(":")[1].split("\n")

answer_key = {}

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

f = open("toxic_complete_MC2.mln",'w')
f.write(formulae_str)
f.close()

#generate db
#for a simple db, just create patient profiles with just one main symptom
num_patients = 100
patients = []

toxidrome_attributes = { "Sympathomimetic(person)": "Bradycardic(person)", \
                       "Anticholinergic(person)": "Hypotensive(person)", \
                       "Cholinergic(person)": "Tachypneic(person)", \
                       "Sedative_hypnotic(person)":"Agitated(person)", \
                       "Opioid(person)":"Hyperpneic(person)" }

#create random patients
for p in range(num_patients):
    tox = random.choice(list(toxidrome_attributes.keys()))
    patient = []

    answer_key[p] = tox
    for s in attributes:
        #if this is a main attribute of this patient's toxidrome
        attr_prob = 0
        if s == toxidrome_attributes[tox]:
            attr_prob = 0.95
        else:
            attr_prob = 0.5
    
        #the probability of a patient having a certain attribute depends on their toxidrome's main attribute
        if random.random() <= attr_prob:
            patient.append(s.replace("person","patient_"+str(p)))

    patient.append(tox.replace("person","patient_"+str(p)))
    patients.append(patient)

db_str = ""
for p in patients:
    db_str += "\n" + "\n".join(p)

print (db_str)

f = open("toxic_complete.db",'w')
f.write(db_str + "\n\n")

#include Semantic Closures
f.write("0 Bradycardic(x) <=> !Tachycardic(x). \n")
f.write("0 Bradycardic(x) <=> !Eucardic(x). \n")
f.write("0 Normotensive(x) <=> !Hypertensive(x). \n")
f.write("0 Normotensive(x) <=> !Hypotensive(x). \n")
f.write("0 Decreased_bowel_sounds(x) <=> !Increased_bowel_sounds(x). \n")
f.write("0 Mydriatic(x) <=> !Miotic(x). \n")
f.write("0 Eupneic(x) <=> !Hyperpneic(x). \n")
f.write("0 Eupneic(x) <=> !Hypopneic(x). \n")
f.write("0 Tachypneic(x) <=> !Bradypneic(x). \n")

f.close()

json.dump(answer_key, open('answer_key_MC.json','wb'))


