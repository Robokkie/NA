#!/usr/bin/env python
# -*- coding:utf-8 -*-

# print 'team:%s,name:%s'%(self.team, self.name)

from function import Function
import function


if __name__=="__main__":
	
	print "please input the number that a,b,c,d for function"
	a,b,c,d = map(int, raw_input('input a,b,c,d=').split(","))
	func=Function(a,b,c,d)
	
	func.showinfo()

	while True:
		print "input l,r | l<r & f(l)*f(r)<0"
		l,r = map(float,raw_input('input l,r=').split(","))
	
		if (func.fnf(l)<func.fnf(r)) and (func.fnf(l)*func.fnf(r)<0):
			print "correct"
			break
		else:
			print "wrong numbers (l>r or f(l)*f(r)>=0)"

	th = float(raw_input('please input threshold:'))
	

	k=0
	results=[]
	while r-l >= th:
		k+=1
		print("{0:4d},{1:8.5f},{2:8.5f},{3:8.5f}".format(k,l,r,r-l))
		center = (l+r)/2.0
		results.append((k,center))
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

	function.write_csv("nibun_results.csv",results)