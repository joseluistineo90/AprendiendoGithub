#coding:utf-8
#!/usr/bin/env python

class Persona(object):
	def __init__(self):
		pass

	def setNombre(self,nombre):
		self.nombre = nombre
	
	def saludar(self):
		print 'Hola ', self.nombre
	

if __name__== "__main__":
	p = Persona()
	p.setNombre('Martin Algañaraz')
	p.saludar()
	
