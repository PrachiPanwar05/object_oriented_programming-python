#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person:
	def __init__(mysillyobject, name, age):
		mysillyobject.name=name
		mysillyobject.age=age

	def myfunc(abc):
		print("hello my name is "+ abc.name)
		print("hello my age is "+ abc.age)

p1=Person("Mary","35")
p1.myfunc()