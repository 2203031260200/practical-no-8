fh=open("output 8.txt",'w')
a= [1,9,6,4,2,0,2,42]
fh.write("before swapping :"+str(a))
a.sort()
fh.write("after swapping:"+str(a))
b=[1,2,5,3,7,9,19,13]
fh.write("before swapping:"+str(b))
b.sort(reverse=True)
fh.write("after swapping:"+str(b))
fh.close
