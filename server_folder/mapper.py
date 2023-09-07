import sys
import json

ans_dt = {}
for cols in sys.stdin:
    if(cols !="\n"):
    	dt = cols
    	for i in range (0,len(dt)):
    		if((dt[i]>='a' and dt[i]<='z') or ((dt[i]>='A' and dt[i]<='Z'))):
    			if (dt[i] in ans_dt ):
    				ans_dt[dt[i]] = int(ans_dt[dt[i]]) +1
    			else:
    				ans_dt[dt[i]] = 1
#ans_dt.sort()
for dt, repos in sorted(ans_dt.items()):
	print(dt, repos)



