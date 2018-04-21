import numpy
import math as m

def convertE2Q(a):
	r=[]
	r.append(m.sin(a[0])*m.cos(a[1])*m.cos(a[2])-m.cos(a[0])*m.sin(a[1])*m.sin(a[2]))
	r.append(m.cos(a[0])*m.sin(a[1])*m.cos(a[2])+m.sin(a[0])*m.cos(a[1])*m.sin(a[2]))
	r.append(m.cos(a[0])*m.cos(a[1])*m.sin(a[2])-m.sin(a[0])*m.sin(a[1])*m.cos(a[2]))
	r.append(m.cos(a[0])*m.cos(a[1])*m.cos(a[2])+m.sin(a[0])*m.sin(a[1])*m.sin(a[2]))
	return r
	
	
	
