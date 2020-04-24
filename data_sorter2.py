# This program will hopefully sort data excel files
import csv
import re
genes = []
row = []
indicators = []
genetype = []

infile = "raw DCM minus 9 dpi.csv"
with open(infile, encoding='utf-8-sig') as fin:  # 'encoding' removes ï»¿ from displaying before 'indicator'
    reader = csv.reader(infile)
    for line in fin:
        # print(line[0]) prints first letter of each indicator in indicator column of excel sheet (A, G, P, S, etc)
        genes.append(line)

outfile = "genes_sorted.txt"
with open(outfile, 'w') as fout:
    for line in genes:
        matchobject = re.search('[A-Za-z]*_at', line)
        item = line.split(',')
        indicators.append(line)  # each item index is a column in the excel sheet, each item is a row
    '''for item in indicators:  # could possibly manipulate this code to sort numerical values for each column
        column = item.split(',')
        indicators.append(column)'''
    if matchobject:
        genevalue = genes[0]  # each line/item in genes is a row of the excel list, genes[0] is the indicator, pek-0 row
        genevalue = genevalue.split(',')
        genetype.append(genevalue)  # indicators list now has all
        indictname = indicators[0]  # indictname = indicators[0] = first element of list 'indicators' (Pek-0 dpi-R1)
        # fout.write(indictname + '\n')
        fout.write(line + '\n')
print(indictname)
print(indicators)
print(genevalue)
print(genetype)
