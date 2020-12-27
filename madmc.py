import numpy as np
def alea(n,m):
	#genere des exemple aleatoirement
	return m/4*numpy.random.randn(n, 2)+m

def algoNaif(data):
	res=[]
	for i in range(len(data)):
		state=False
		for j in range(len(data)):
			if compare(data[i],data[j]):
				state = True
		if state== False :
			res.append(data[i])
	return res

def compare(a,b):
	if b[0]<a[0] and b[1]<=a[1] :
		return True
	if b[0]<=a[0] and b[1]<a[1] :
		return True
def algoSecond(data):
    res=[]
    a=0
    data = np.array(data)
    data = data[np.argsort(data[:,0])[::-1]]
    n=len(data)
    for i in range(n):
        data=data[a:len(data),]
        m=len(data)
        min1=np.argmin(data[:,1])
        res.append(data[min1])
        a=min1+1
        if min1==m-1:
            break
    return res