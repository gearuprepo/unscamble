"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#Step 1: Jon the telephone numbers across calls and text O(n) = 2n
count = 0
summarylist = []
for entry in texts:
    summarylist.append(entry[0])
    summarylist.append(entry[1])

for entry in calls:
    summarylist.append(entry[0])
    summarylist.append(entry[1])

#Printing by convering to set to elimindate duplicates O(n) = n [Assuming conversion of list to hashset is linear]
print("There are "+ str(set(summarylist).__len__()) +" different telephone numbers in the records.")

# O(n) = 2n + n