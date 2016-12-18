class Parent(object):
	
	def override(self):
		print "PARENT override()"
	
	def implicit(self):
		print "PARENT implicit()"
	
	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	
	def override(self):
		print "CHILD override()"
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent() 
son = Child()

dad.implicit() # PARENT
son.implicit() # PARENT

dad.override() # PARENT
son.override() # CHILD

dad.altered() # PARENT
son.altered() # CHILD, PARENT, CHILD