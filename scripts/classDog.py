#!/usr/bin/env python

# import the necessary packages
import sys

class Dog(object):
	species = "Canis familiaris"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return "{} is {} years old".format(self.name, self.age)

	def speak(self, sound):
		return "{} is {} years old says {}".format(self.name, self.age, sound)

class GoldenRetriever(Dog, object):
	def __init__(self, name, age):
		if sys.version_info[0] < 3:
			super(GoldenRetriever, self).__init__(name, age)
		else:
			super(GoldenRetriever, self).__init__(name, age)

B = GoldenRetriever("Hason", 2)
print(B)

