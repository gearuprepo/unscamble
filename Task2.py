"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
maxtime = ['',0]
maxdict = {}
# Step 1: Form a Dict with incoming+outgoing calls per number with sum of total time O(n) = n
for call in calls:
    outgoing = call[0]
    incoming = call[1]
    talktime = call[3]

    if maxdict.get(outgoing)!= None :
       maxdict[outgoing] = maxdict[outgoing] + int(talktime)
    else:
        maxdict[outgoing] = int(talktime)

    if maxdict.get(incoming)!= None :
       maxdict[incoming] = maxdict[incoming] + int(talktime)
    else:
        maxdict[incoming] = int(talktime)

# Step 2: Find the max based on the talk time O(n) = n
for entry in maxdict:
    if maxtime.__len__()>0:
        if maxtime[1]<maxdict.get(entry):
            maxtime[0] = entry
            maxtime[1] = maxdict.get(entry)
    else:
        maxtime[0] = entry
        maxtime[1] = maxdict.get(entry)

print(maxtime[0]+" spent the longest time, "+str(maxtime[1])+" seconds, on the phone during September 2016.")

#Task 2: O(n) = 2n