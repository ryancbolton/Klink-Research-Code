# This program will hopefully sort data excel files
import csv
genes = []
row = []
indicator = []

# read in genes from file
filename = "raw DCM minus 9 dpi.csv"
with open(filename) as fin:
    reader = csv.reader(filename)
    next(reader, None)
    for line in fin:
        data = line.split(',')
        # indicator.append(data[0])
        # genes.append(data[1])
        genes.append(line.strip())

# sort genes
genes.sort()
genes.pop()
line = line.strip()
# line = float(line)
# sorted(genes, key=lambda x: int(x[1]))
print(genes)
row.append(genes[0])
# write sorted genes to output file
filename2 = "genes_sorted.txt"

with open(filename2, 'w') as fout:
    #print(row) # is treating each line as an element in 'genes' instead of each value/indicator
    for gene in genes:
        fout.write(gene + '\n')

with open(filename2, 'r') as fout:
    for line in fout:
        line = line.split(',')
        row.append(line)
#for item in row:
    #row = item.split(',')

indicator = [row[0] for item in row]
    #indicator.append(row[0])
print(row)
print(indicator)
