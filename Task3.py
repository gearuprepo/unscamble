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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Step 1: Part A Implementation [O(n) = n]
blrsrccount = 0
blrdestcount = 0
partacodes = []
for call in calls:
    srccallerprefix = call[0][0:5]
    if(srccallerprefix == '(080)'):
        blrsrccount = blrsrccount + 1
        destnumber = call[1]
        if destnumber[0] == '(':
            destprefix = destnumber[destnumber.find('(')+1:destnumber.find(')')]
            if(destprefix=='080'):
                blrdestcount = blrdestcount + 1
        elif destnumber[0:3] == '140':
            destprefix = 140
        else:
            destprefix = destnumber[0:4]
        partacodes.append(destprefix)

# Step 2: Part A - Sort [O(n) = nlogn]
partacodes.sort()

# Step 3: Part A - Remove Duplicate [O(n) = n]
partafinal = [partacodes[0]]
for code in partacodes:
    if code != partafinal[len(partafinal)-1]:
        partafinal.append(code)

# Step 4: Part A - Printing [O(n) = n]
print("The numbers called by people in Bangalore have codes:")
for code in partafinal:
    print(code)

# Step 5 - printing Part B [O(n) = 1]
print(str(round(blrdestcount/blrsrccount,2)*100)+" percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

# O(n) = 3n+nlogn+1