#!/usr/bin/env python

# import the necessary packages

class CarClass():
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage
		
	def __str__(self):
		return "The {} car has {} miles.".format(self.color, self.mileage)
		
print(CarClass)
print(CarClass("blue", 10000))
		
