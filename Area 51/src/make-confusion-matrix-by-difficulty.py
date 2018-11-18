import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

from pandas_ml import ConfusionMatrix

df = pd.read_csv('./data/analysis.csv')

for difficulty in [0,1,2]:
	sub_df = df.loc[df['difficulty']==difficulty]


	cmat = ConfusionMatrix(sub_df['predicted'],sub_df['actual'])
	#cmat.print_stats()


	#print dir(cmat)

	fig = plt.figure()
	ax = fig.add_subplot(111)

	sns.heatmap(cmat.to_dataframe(),square=True, annot=True, fmt="d", cmap=plt.cm.bone_r)
	plt.xticks(rotation=90)
	plt.yticks(rotation=0)


	a=[item.get_text() for item in ax.get_yticklabels()]
	b=[item.get_text() for item in ax.get_xticklabels()]
	conversion = {'sympathomimetic': "Sympathomimetic",
					'sedative_hypnotic': "Sedative-Hypnotic",
					'cholinergic':"Cholinergic",
					'anticholinergic':"Anticholinergic",
					'opioid':"Opioid",
					"serotonin_syndrome":"Serotonin Syndrome"}

	new_ticklabels = [conversion[label] for label in b]
	ax.set_yticklabels(new_ticklabels)
	new_ticklabels = [conversion[label] for label in b]
	ax.set_xticklabels(new_ticklabels)

	plt.tight_layout()
	plt.savefig('./imgs/internal_validation-difficulty-%d.png'%difficulty,dpi=300)


