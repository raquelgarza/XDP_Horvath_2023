import os
import sys
import shutil

poly_names = sys.argv[1]
fa_path = sys.argv[2]
chrs_name = sys.argv[3]

f = open(poly_names)
poly = f.readlines()

fchrs = open(chrs_name)
chrs = fchrs.readlines()
chrs = [i.strip() for i in chrs]
print(chrs)
chrs_polys = { c : sorted([[int(w.split()[1]), int(w.split()[2]), w.split()[3]] for w in poly if w.split()[0] == c], reverse = True) for c in chrs}


for c in chrs:
	fname = os.path.join(fa_path, "{}.fa".format(c))
	fname_out = os.path.join(fa_path, "{}_poly.fa".format(c))
	shutil.copy(fname, fname_out)
	for i in chrs_polys[c]:	
		fchr = open(fname_out, "r")
		file = fchr.readlines()[1:]
		fchr.close()
		file = [i.strip() for i in file]
		file = "".join(file)
		start = i[0]
		end = i[1]
		seq = i[2].strip()
		new_file = "{prev}{seq}{after}".format(prev=file[0:start], seq=seq, after=file[end:])
		new_file = [new_file[i:i+50] + "\n" for i in range(0, len(new_file), 50)] # cut line every 50bp
		new_file.insert(0, ">{}\n".format(c))
		fout = open(fname_out, "w")
		fout.writelines(new_file)
		fout.close()
		print(fname_out)
