mysql-ib < schema.sql

rm adjustment*
rm fact*

wget http://source.data.gov.uk/data/finance/coins/2010-06-04/adjustment_table_extract_2009_10.zip
unzip adjustment_table_extract_2009_10.zip 
python munge.py 
mysql-ib COINS -e "LOAD DATA INFILE '/home/donny/COINS/adjustment_table_extract_2009_10.csv' INTO TABLE Adjustments FIELDS TERMINATED BY '@'"
rm adjustment*

wget http://source.data.gov.uk/data/finance/coins/2010-06-04/adjustment_table_extract_2008_09.zip
unzip adjustment_table_extract_2008_09.zip
python munge.py
mysql-ib COINS -e "LOAD DATA INFILE '/home/donny/COINS/adjustment_table_extract_2008_09.csv' INTO TABLE Adjustments FIELDS TERMINATED BY '@'"
rm adjustment*   

wget http://source.data.gov.uk/data/finance/coins/2010-06-04/fact_table_extract_2009_10.zip
unzip fact_table_extract_2009_10.zip 
python munge.py
mysql-ib COINS -e "LOAD DATA INFILE '/home/donny/COINS/fact_table_extract_2009_10.csv' INTO TABLE Facts FIELDS TERMINATED BY '@'"
rm fact*

wget http://source.data.gov.uk/data/finance/coins/2010-06-04/fact_table_extract_2008_09.zip
unzip fact_table_extract_2008_09.zip
python munge.py
mysql-ib COINS -e "LOAD DATA INFILE '/home/donny/COINS/fact_table_extract_2008_09.csv' INTO TABLE Facts FIELDS TERMINATED BY '@'"
rm fact*

mysql-ib COINS -e "LOAD DATA INFILE '/home/donny/COINS/Time.csv' INTO TABLE Time FIELDS TERMINATED BY ','"
mysql-ib COINS -e "LOAD DATA INFILE '/home/donny/COINS/AccountGroup.csv' INTO TABLE AccountGroup FIELDS TERMINATED BY ','"
