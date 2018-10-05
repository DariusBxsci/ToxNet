import os 

'''
	The predictions of the algorithm are compared against:
	1. known labels of the synthetic data ("ground truth")
	2. guesses of two toxicologists

	The purpose of this file is to convert the data representing (1) rom JSON into CSV 
	so that a later step can join (1) with (2) and the algorithm's predictions into one DataFrame
'''