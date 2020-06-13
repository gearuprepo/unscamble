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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Function to fetch the column irrespective of the area code.
def fetchcol(ls,col):
    retval = []
    for item in ls:
        appendtxt = item[col]
        if item[col][0]=='(':
            appendtxt = item[col].split(")")[1]
        retval.append(appendtxt)
    return retval

""" Step 1: Fetch the columns for both calls and text O(n) = 8n 
            Per call O(n) = fetchcols = n + list to set is assumed to be n
            Per call O(n) = 2n
            Total O(n) = 4 * 2n
"""
callssrc = set(fetchcol(calls,0))
callsdest = set(fetchcol(calls,1))
textssrc = set(fetchcol(texts,0))
textsdest = set(fetchcol(texts,1))

"""Step 2 : Union the destcalls, dest and src text sets  O(n) = 2n
        Per Union O(n) = n [reference#1]
        Total O(n) = 2 * n
 """
compareset = callsdest.union(textssrc).union(textsdest)

"""Step 3: Use set differnece update to remove the items in callsrc that are available in the compareset
            O(n) = n [refence#1]
"""
callssrc.difference_update(compareset)


"""
Step 4: Lexographical Sorting : O(n) = nlogn
"""
sortedlist = list(callssrc)
sortedlist.sort()

# Step 5: Print O(n) = n
print("These numbers could be telemarketers: ")
for element in sortedlist:
    print(element)

"""O(n) =  11n + nlogn"""