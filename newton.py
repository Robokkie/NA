#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math

from function import Function
import function

if __name__ == '__main__':

	print "please input the number that a,b,c,d for function"
	a,b,c,d = map(int, raw_input('input a,b,c,d=').split(","))
	func=Function(a,b,c,d)

	func.showinfo()

	while True:
		print "input x,r | x<r & f(x)*f(r)<0"
		x,r = map(float,raw_input('input x,r=').split(","))
	
		if (func.fnf(x)<func.fnf(r)) and (func.fnf(x)*func.fnf(r)<0):
			print "correct"
			break
		else:
			print "wrong numbers (x>r or f(x)*f(r)>=0)"

	th = float(raw_input('please input threshold:'))


	k=0

	print "number of process, approximation, diff"

	print("{0:4d},{1:8.5f},{2}".format(k,x,"---"))
	
	approximations=[]

	while True:
		k+=1
		xn = x - func.fnf(x)/func.diff(x)
		print("{0:4d},{1:8.5f},{2:8.5f}".format(k,xn,xn-x))
		temp=(k,x)
		approximations.append(temp)
		if(math.fabs(xn-x) < th):
			break
		else:
			x=xn

	print "number of process = {0:4d}".format(k)
	print "the solution = {0:10.6f}".format(xn)

	function.write_csv("newton_results.csv",approximations)