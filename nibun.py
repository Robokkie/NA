#!/usr/bin/env python
# -*- coding:utf-8 -*-

# print 'team:%s,name:%s'%(self.team, self.name)

class function:
	def __init__(self, a,b,c,d):
		self.a=a
		self.b=b
		self.c=c
		self.d=d
	def fnf(self,x):
		return self.a*x*x*x+self.b*x*x+self.c*x+self.d
	def diff(self,x):
		return self.a*3*x*x+self.b*2*x*x+self.c
	def showinfo(self):
		print 'a,b,c,d = %d %d %d %d'%(self.a, self.b, self.c, self.d)

print "please input the number that a,b,c,d for function"
a,b,c,d = map(int, raw_input('input a,b,c,d=').split(","))
func=function(a,b,c,d)

func.showinfo()

while True:
	print "input l,r | l<r & f(l)*f(r)<0"
	l,r = map(float,raw_input('input l,r=').split(","))
	
	answer = raw_input('Could you input correct numbers?(y/n):')
	
	
	if (answer=="y") and (func.fnf(l)<func.fnf(r)) and (func.fnf(l)*func.fnf(r)<0):
		print "correct"
		break
	else:
		print "wrong numbers (l>r or f(l)*f(r)>=0)"

th = float(raw_input('please input threshold:'))


k=0
while r-l >= th:
	k+=1
	print("{0:4d},{1:8.5f},{2:8.5f},{3:8.5f}".format(k,l,r,r-l))
	center = (l+r)/2.0
	if(func.fnf(l)*func.fnf(center)>0):
		l=center
	else:
		r=center
	if k%10 == 0:
		print "Showing the calculation process"
		answer = raw_input('Continue showing?(y/n):')
		if answer == "n":
			print "Finish the showing"
		else:
			print "number of process, left, right, left-right"

if answer != "n":
	print "number of process = {0:4d}".format(k)
	print "the solution = {0:10.6f}".format((l+r)/2.0)
