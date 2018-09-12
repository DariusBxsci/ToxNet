
import sys

toxidromes = open(sys.argv[1],'r').read().split(":")[0].split("\n")
attributes = open(sys.argv[1],'r').read().split(":")[1].split("\n")

for t in toxidromes:
	for a in attributes:
		if len(t) > 1 and len(a) > 1:
			print (t + " => " + a)
