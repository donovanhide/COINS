#!/usr/bin/env python 
import os
import subprocess
import codecs
import glob

def munge(file):
        input = codecs.open(file,'r','utf_16_le','strict')
        output = codecs.open(file.replace('txt','csv'),'w','utf_8','strict')
        counter = 0
        for line in input:
                if counter > 0 and len(line)>10 and not line.__contains__('row(s) affected)'):
                        while line.count('@')<79:
                                line = line.strip()+input.readline()
                        output.write("%s\n" % line.replace(u'NULL','').replace(u'"','').strip())
                counter +=1

def run(command):
	print(command)
	os.popen(command)	

def delete(pattern):
	for file in glob.glob(pattern):
		os.remove(file)
		

def load(file,table,separator):
	run('mysql-ib COINS -e "LOAD DATA INFILE \'%s\' INTO TABLE %s  FIELDS TERMINATED BY \'%s\'"' % (os.path.join(os.getcwd(),file),table,separator))

dumps = [
          { 
            'table'   : 'Adjustments',
            'prefix'  : 'adjustment_table_extract_'
          },
          {
            'table'   : 'Facts',
            'prefix'  : 'fact_table_extract_'
          }
        ]
years = ['2009_10','2008_09','2007_08','2006_07','2005_06']

run('mysql-ib < schema.sql')
load('Time.csv','Time',',')
load('AccountGroup.csv','AccountGroup',',')

for dump in dumps:
  for year in years:
    prefix = dump['prefix']
    delete('%s*'% prefix)
    zipFile = "%s%s.zip" %(prefix,year)
    txtFile = "%s%s.txt" %(prefix,year)
    csvFile = "%s%s.csv" %(prefix,year)
    run('wget  http://source.data.gov.uk/data/finance/coins/2010-06-04/%s' % zipFile)
    run('unzip %s'% zipFile)
    munge(txtFile)
    load(csvFile,dump['table'],'@')
    delete('%s*'% prefix)
