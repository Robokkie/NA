#!/usr/bin/env python
# -*- coding:utf-8 -*-

# print 'team:%s,name:%s'%(self.team, self.name)

class function:
	def __init__(self, a,b,c,d):
		self.a=a
		self.b=b
		self.c=c
		self.d=d
	def fnf(a,b,c,d,x):
		return a*x*x*x+b*x*x+c*x+d
	def showinfo(self):
		print 'a,b,c,d = %d %d %d %d'%(self.a, self.b, self.c, self.d)

print "please input the number that a,b,c,d for function"
a,b,c,d = map(int, raw_input('input a,b,c,d=').split(","))
func=function(a,b,c,d)

func.showinfo()

while True:
	print "input e,f | f(e)*f(f)<0"
	e,f = map(int,raw_input('input e,f=').split(","))
	break