import sys
ans_dt = {}
coll=sys.stdin

fs="part-000"
fs2="mixed"
file2=open(fs2,"r")
lines=(file2.readlines())
partitions=int(input("Enter number of partitions:"))
cnt=0
for line in lines:
	cnt+=1
	#print(line)
	#print()

print("Number of lines",cnt)
print("Number of partitions",partitions)
mixxer=cnt//partitions
fine=0
if(cnt%partitions !=0):
	fine=cnt%partitions

#making new files for partition:
party=0
k=0
old=0

print("Distributed into partitions into files:-")
for i in range (0, partitions):
	l=0
	if fine>0:
		l=1
	#print(i,"th partion has",mixxer+l,"lines")
	fine-=l
	party=old+mixxer+l-1
	#print("content of partition",i,"lasts from",old,"to",party+1)
	#print(lines[old:party+1])
	neww=fs+str(i)
	neww="server_folder"+"/"+"partition"+str(i)+"/"+neww
	file2=open(neww,"w")
	print(neww)
	for lii in lines[old:party+1]:
		file2.write(lii)
	#print()
	#print(len(lines[old:party+1]))
	old=party+1 
	
	
	

 
	"""
	if(cols !="\n"):
		dt = cols
		#print(dt)
		for i in range (0,len(dt)):
			#dt=dt[i]	
			#print(dt, len(cols))
			if((dt[i]>='a' and dt[i]<='z') or ((dt[i]>='A' and dt[i]<='Z'))):
				if (dt[i] in ans_dt ):
					ans_dt[dt[i]] = int(ans_dt[dt[i]]) +1
				else:
					ans_dt[dt[i]] = 1
#ans_dt.sort()
for dt, repos in sorted(ans_dt.items()):
	print(dt, repos)
"""
