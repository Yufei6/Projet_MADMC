import numpy as np
def alea(n,m):
	#genere des exemple aleatoirement
	return m/4*numpy.random.randn(n, 2)+m

def algoNaif(z,n):
	res=[]
	for i in range(n):
		state=False
		for j in range(n):
			if compare(z[i],z[j]):
				state = True
		if state== False :
			res.append(z[i])

def compare(a,b):
	if b[0]<a[0] and b[1]<=a[1] :
		return True
	if b[0]<=a[0] and b[1]<a[1] :
		return True