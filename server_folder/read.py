import sys
if(len(sys.argv) <3):
	print("Make sure you give root file and to which file write has to happen")
	sys.exit(0)

fs=sys.argv[1] #for accessing root file whose partitions were made before 
print(fs)
fs2=sys.argv[2] #for picking a file through which we can write
print(fs2)
#part=sys.argv[3]
#print(part)
#file1=open(fs,"r")
#lines=(file1.readlines())
file2=open(fs2,"w")
part=int(input("Enter number of partitions to fetch from: "))
for i in range (0, part):
	nfs=fs+str(i)
	neww="partition"+str(i)+"/"+nfs
	file1=open(neww,"r")
	lines=(file1.readlines())
	for line in lines:
		file2.write(line)
		print(line)

