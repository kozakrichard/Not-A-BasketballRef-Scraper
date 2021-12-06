### Does as the name says, combines all the csv files in your current working directory. 
### Be careful to change the name of the files as running this multiple times will overwrite data.
### Intended for combining stats across the seasons of the NBA into a single source. 

import os
import glob
import pandas as pd
#set working directory
cwd = os.getcwd()
os.chdir(cwd)

#find all csv files in the folder
#use glob pattern matching -> extension = 'csv'
#save result in list -> all_filenames
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv_totals.csv", index=False, encoding='utf-8-sig')
