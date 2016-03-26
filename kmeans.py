
import sys
import math
import random
import copy
random.seed(12345566)


f = open(str(sys.argv[3]), 'w')


def euclidean(x1,y1,x2,y2):
	d=math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
	return d
	

def kmeans(centroidx, centroidy, x, y,k,l):
	count=0
	for h in range(25):	
		count=count+1;
		cluster=[]
		centroidx1=[]
		centroidy1=[]
		for i in range(l):
			d=[euclidean(centroidx[j],centroidy[j],x[i],y[i]) for j in range(k)]
			#print d
			ans= d.index(min(d))
			cluster.append(ans)	
		#print cluster
		
		
		
		centroidx1,centroidy1 = up_date(cluster,centroidx, centroidy,x,y,l,k)
		sum=0
		
		for i in range(k):
			if (centroidx1[i]==centroidx[i] and centroidy1[i]==centroidy[i]):
				sum=sum+1
		if (sum==k):
			break;
	

		centroidx = copy.deepcopy(centroidx1)
		centroidy = copy.deepcopy(centroidy1)
		
	output(cluster,k)
	
	#print count
	sse(cluster,centroidx,centroidy,x,y,k,l)	
		
def output(cluster,k):
		indices=[]
		for i in range(k):	
			indices.append([j for j, u in enumerate(cluster) if u == i])	
			#print i+1,[x+1 for x in indices[i]]
			print >> f, i+1,[x+1 for x in indices[i]]
def up_date(cluster,centroidx, centroidy,x,y,l,k):
	indices=[]
	cenx=[]
	ceny=[]
	for i in range(k):
		indices.append([j for j, u in enumerate(cluster) if u == i])
		m=indices[i]
		if (len(m) != 0):
			sx=[x[p] for p in m]
			sy=[y[p] for p in m]
			cenx.append(round(sum(sx)/len(m),3))
			ceny.append(round(sum(sy)/len(m),3))
		else:
			cenx.append(centroidx[i])
			ceny.append(centroidy[i])

	return (cenx,ceny)
		
			 
def sse(cluster,centroidx,centroidy,x,y,k,l):
	sum=0
	indices=[]
	for i in range(k):	
		indices.append([j for j, u in enumerate(cluster) if u == i])	
		x1=[x[d] for d in indices[i]]
		y1=[y[d] for d in indices[i]]
		for j in range(len(indices[i])):
			sum=sum + math.pow(euclidean(x1[j],y1[j],centroidx[i],centroidy[i]),2)
	print >>f,'SSE',sum

def main():
	
	
	k=int(sys.argv[1])
	#output_file=str(sys.argv[3])
	input_file = open(str(sys.argv[2]), "r")
	lines = input_file.readlines()
	data1= lines[0].split('\r')[1:]  
	data = []
	for item in data1:
		items = item.split('\t')
  		data.append([int(items[0]), float(items[1]), float(items[2])])

	l=len(data)
	x=[round(i[1],3) for i in data]
	y=[round(i[2],3) for i in data]
	centroidx=[]
	centroidy=[]
	r1=random.sample(x, k)
	r=[x.index(item) for item in r1]
	for j in r:
		centroidx.append(x[j])
		centroidy.append(y[j])

	#print centroidx
	#print centroidy
	kmeans(centroidx, centroidy, x, y,k,l)
	f.close()
	
if __name__ == "__main__": 
    main()


