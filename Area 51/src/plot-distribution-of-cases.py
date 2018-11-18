import json
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd 

df = pd.read_json('./data/world.json').transpose()
sns.set(style="whitegrid")


fig = plt.figure()
ax = fig.add_subplot(111)

sns.countplot(y="intended_toxidrome", data=df, color='k', hue='difficulty')
sns.despine(left=True, bottom=True)

ax.set_ylabel("")
ax.set_xlabel("Intended Toxidrome")

a=[item.get_text() for item in ax.get_yticklabels()]
conversion = {'sympathomimetic': "Sympathomimetic",
				'sedative_hypnotic': "Sedative-Hypnotic",
				'cholinergic':"Cholinergic",
				'anticholinergic':"Anticholinergic",
				'opioid':"Opioid",
				"serotonin_syndrome":"Serotonin Syndrome"}

new_ticklabels = [conversion[label] for label in a]
ax.set_yticklabels(new_ticklabels)

plt.tight_layout()
plt.savefig("./imgs/intended-toxidrome-distribution//CTN-0006.png",dpi=400)