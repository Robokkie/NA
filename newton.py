#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math

class function:
	def __init__(self, a,b,c,d):
		self.a=a
		self.b=b
		self.c=c
		self.d=d
	def fnf(self,x):
		return self.a*x*x*x+self.b*x*x+self.c*x+self.d
	def diff(self,x):
		return self.a*3*x*x+self.b*2*x+self.c
	def ddiff(self,x):
		return self.a*3*2*x+self.b*2
	def showinfo(self):
		print 'a,b,c,d = %d %d %d %d'%(self.a, self.b, self.c, self.d)

if __name__ == '__main__':

	print "please input the number that a,b,c,d for function"
	a,b,c,d = map(int, raw_input('input a,b,c,d=').split(","))
	func=function(a,b,c,d)

	func.showinfo()

	while True:
		print "input x,r | x<r & f(x)*f(r)<0"
		x,r = map(float,raw_input('input l,r=').split(","))
	
		answer = raw_input('Could you input correct numbers?(y/n):')
	
	
		if (answer=="y") and (func.fnf(x)<func.fnf(r)) and (func.fnf(x)*func.fnf(r)<0):
			print "correct"
			break
		else:
			print "wrong numbers (x>r or f(x)*f(r)>=0)"

	th = float(raw_input('please input threshold:'))


	k=0
	while True:
		k+=1
		xn = x - func.fnf(x)/func.diff(x)
		print("{0:4d},{1:8.5f},{2:8.5f}".format(k,x,xn-x))
		if(math.fabs(xn-x) < th):
			break
		else:
			x=xn
		if k%10 == 0:
			print "Showing the calculation process"
			answer = raw_input('Continue showing?(y/n):')
			if answer == "n":
				print "Finish the showing"
			else:
				print "number of process, approximation, diff approximation"

	if answer != "n":
		print "number of process = {0:4d}".format(k)
		print "the solution = {0:10.6f}".format(xn)