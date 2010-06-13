import codecs,glob

for file in glob.glob('./*.txt'):
	input = codecs.open(file,'r','utf_16_le','strict')
	output = codecs.open(file.replace('txt','csv'),'w','utf_8','strict')
	counter = 0
	for line in input:
		if counter > 0 and len(line)>10 and not line.__contains__('row(s) affected)'):
			while line.count('@')<79:
		               	line = line.strip()+input.readline()
			output.write("%s\n" % line.replace(u'NULL','').replace(u'"','').strip())
		counter +=1
