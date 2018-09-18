#make world

from datagen import *
#Entities are people, symptoms, perhaps toxidromes
world = World()

LIST_OF_ALL_POSSIBLE_SYMPTOMS = []

class Person(Object):
	def (self,world,intended_toxidrome,kwargs**):
	Object.(self,"person")
	
	self.intended_toxidrome = intended_toxidrome

	for key,value in kwargs.items():
		setattr(self,key,value)

class Toxidrome(Object):
	def (self,)