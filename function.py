#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv

class Function:
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
		print "{0}x^3 + {1}x^2 + {2}x + {3}".format(self.a,self.b,self.c,self.d)

def write_csv(filename, rows):
	with open(filename,'w') as csv_file:
		writer=csv.writer(csv_file)
		csv_header=("n", "xn")
		writer.writerow(csv_header)
		for row in rows:
			writer.writerow(row)