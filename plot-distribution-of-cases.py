import json
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd 

df = pd.read_json('./world.json').transpose()
sns.set(style="whitegrid")


fig = plt.figure()
ax = fig.add_subplot(111)

sns.countplot(x="intended_toxidrome", data=df)
sns.despine(left=True, bottom=True)

ax.set_ylabel("")
ax.set_xlabel("Intended Toxidrome")

a=[item.get_text() for item in ax.get_xticklabels()]
conversion = {'sympathomimetic': "sympathomimetic",
				'sedative_hypnotic': "sedative/hypnotic",
				'cholinergic':"cholinergic",
				'anticholinergic':"anticholinergic",
				'opioid':"opioid"}

new_ticklabels = [conversion[label] for label in a]
ax.set_xticklabels(a)

plt.tight_layout()
plt.savefig("./intended-toxidrome-distribution.png",dpi=400)