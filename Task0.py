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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
firsttexts = str("First record of texts, "+texts[0][0]) + ' texts '+str(texts[0][1])+' at time '+str(texts[0][2])
firstcalls = "Last record of calls, "+str(calls[calls.__len__()-1][0]) + ' texts '+str(calls[calls.__len__()-1][1])+' at time '+str(calls[calls.__len__()-1][2]+", lasting "+calls[calls.__len__()-1][3]+" seconds")

print(firsttexts)
print(firstcalls)

#O(n) = 1
