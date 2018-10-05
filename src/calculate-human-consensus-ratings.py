import json, os, argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="location of Tak, Alex combined results")
args = parser.parse_args()

human_ratings = pd.read_csv(os.path.join(args.input))

#125 out of 217 have full consensus
full_consensus = human_ratings.loc[human_ratings['tak_toxidrome']==human_ratings['barbuto_toxidrome']]

full_consensus = full_consensus.rename(columns={"tak_toxidrome":"human_toxidrome"})

full_consensus.to_csv(os.path.join(os.path.dirname(args.input),
				"human-ratings.csv"),columns=["id","human_toxidrome"], index=False)