import sys
vis=[0]*26
ans=[0]*26

fs=sys.argv[1] #for accessing root file whose partitions were made before 
print(fs)
fs2="mixxer" #for picking a file through which we can write
print(fs2)
#part=sys.argv[3]
#print(part)
#file1=open(fs,"r")
#lines=(file1.readlines())
file2=open(fs2,"w")
part=int(input("Enter number of partitions to fetch from: "))
for i in range (0, part):
	nfs=fs+str(i)
	neww="server_folder"+"/"+"partition"+str(i)+"/"+nfs
	file1=open(neww,"r")
	lines=(file1.readlines())
	for line in lines:
		#print(line)
		file2.write(line)

#print("Are we in")
fs="mixed"
file2=open(fs2,"r")
file3=open(fs,"w")
lines=(file2.readlines())
for line in lines:
	#lines=(file1.readlines())
	#for line in cols:
		#print(line)
		x,y= line.split(" ")
		y=int(y)		
		if(vis[ord(x)-ord('a')]==0):
			vis[ord(x)-ord('a')]=1
			ans[ord(x)-ord('a')]=y
		else:
			ans[ord(x)-ord('a')]+=y

for i in range (0,26):
	if(ans[i]!=0):
		print(chr(i+ord('a'))," ",ans[i] )
		zz=str(chr(i+ord('a')))+" "+str(ans[i])+("\n")
		file3.write(zz)

	