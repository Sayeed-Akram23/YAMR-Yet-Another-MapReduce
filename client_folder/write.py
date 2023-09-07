import sys
import os

fs = sys.argv[1]

# Open the input file
file1 = open(fs, "r")
lines = file1.readlines()

# Counting the number of lines
cnt = 0
for line in lines:
    cnt += 1

print("Number of lines", cnt)

partitions = int(input("Enter number of partitions: "))
print("Number of partitions", partitions)

# Calculate lines per partition and any remaining lines
mixer = cnt // partitions
fine = 0
if (cnt % partitions != 0):
    fine = cnt % partitions

# Create directories for partitions if they don't exist
for i in range(partitions):
    directory = f"files{i}"
    os.makedirs(directory, exist_ok=True)

print("Distributed into partitions into files:-")

party = 0
k = 0
old = 0

for i in range(partitions):
    l = 0
    if fine > 0:
        l = 1

    fine -= l
    party = old + mixer + l - 1

    # Construct the new file path
    neww = f"files{i}/{fs}{i}"

    print(neww)

    # Open the new file for writing
    with open(neww, "w") as file2:
        for lii in lines[old:party + 1]:
            file2.write(lii)

    old = party + 1
