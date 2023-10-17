import os
import sys

poly_names = sys.argv[1]
gtfin_name = sys.argv[2]
chrs_name = sys.argv[3]
gtfout_name = gtfin_name.split(".gtf")[0]
gtfout_name = gtfout_name + "_poly.gtf"

f = open(poly_names)
poly = f.readlines()

fchrs = open(chrs_name)
chrs = fchrs.readlines()
chrs = [i.strip() for i in chrs]
print(chrs)
chrs_polys = { c : sorted([[int(w.split()[1]), int(w.split()[2]), w.split()[3]] for w in poly if w.split()[0] == c], reverse=True) for c in chrs}

gtfin = open(gtfin_name, "r+")
gtf = gtfin.readlines()
chrs_gtf = {c : [line.split("\t") for line in gtf if line.split()[0] == c] for c in chrs}

for c in chrs:
	for pi in chrs_polys[c]:
		pistart = pi[0]
		piend = pi[1]
		pilength = len(pi[2])
		pidel = piend - pistart
		for feature in chrs_gtf[c]:
			fstart = int(feature[3])
			fend = int(feature[4])
			if pistart < fstart:
				fstart = fstart + pilength - pidel
			if pistart < fend:
				fend = fend + pilength - pidel
			feature[3] = str(fstart)
			feature[4] = str(fend)
	print(c)



gtfout = open(gtfout_name, "a")

for c in chrs:
	gtfout.write("".join(["\t".join(i) for i in chrs_gtf[c]]))

gtfout.close()

