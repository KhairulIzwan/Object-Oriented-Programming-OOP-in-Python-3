#!/usr/bin/env python

# import the necessary packages
import sys

class Rectangle(object):
	def __init__(self, length, width, **kwargs):
		self.length = length
		self.width = width
		super(Rectangle, self).__init__(**kwargs)
		

	def area(self):
		return self.length * self.width

	def perimeter(self):
		return 2 * self.length + 2 * self.width

class Square(Rectangle, object):
	def __init__(self, length, **kwargs):
		super(Square, self).__init__(length=length, width=length, **kwargs)
#		if sys.version_info[0] < 3:
#			super(Square, self).__init__(length, length)
#		else:
#			super(Square, self).__init__(length, length)
		
class Cube(Square, object):
	def surface_area(self):
		face_area = super(Cube, self).area()
#		if sys.version_info[0] < 3:
#			face_area = super(Cube, self).area()
#		else:
#			face_area = super(Cube, self).area()
		return face_area * 6

	def volume(self):
		face_area = super(Cube, self).area()
#		if sys.version_info[0] < 3:
#			face_area = super(Cube, self).area()
#		else:
#			face_area = super(Cube, self).area()
		return face_area * self.length

class Triangle:
	def __init__(self, base, height, **kwargs):
		self.base = base
		self.height = height

	def tri_area(self):
		return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle, object):
	def __init__(self, base, slant_height, **kwargs):
		self.base = base
		self.slant_height = slant_height
		kwargs["height"] = slant_height
		kwargs["length"] = base
		super(RightPyramid, self).__init__(base=base, **kwargs)

	def area(self):
		base_area = super(RightPyramid, self).area()
		perimeter = super(RightPyramid, self).perimeter()
		return 0.5 * perimeter * self.slant_height + base_area
		
	def area_2(self):
		base_area = super(RightPyramid, self).area()
		triangle_area = super(RightPyramid, self).tri_area()
		return triangle_area * 4 + base_area
	
square = Square(3)
print(square.area())

cube = Cube(3)
print(cube.area())
print(cube.surface_area())
print(cube.volume())

pyramid = RightPyramid(2, 4)
print(pyramid.area())
print(pyramid.area_2())
