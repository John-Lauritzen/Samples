from pathlib import Path

#Define path to scan
directory = Path('html-test')
#Create Dictionary to store results
results = dict()
#Create list of html files in directory and sub-directories
htmlfiles = list(directory.rglob('*.html'))
#Iterate over list
for file in htmlfiles:
    #Open file
    temphtml = open(file, mode='r')
    #Create counter
    count = 0
    #Check each line
    for line in temphtml:
        if 'type@shavlik.com' in line:
            count += 1
    #Add record to dictionary if results were found
    if count > 0:
        results[file] = count
#Print results
print(results)


