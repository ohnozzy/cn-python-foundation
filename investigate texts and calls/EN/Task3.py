"""
Intro to Python Lab 1, Task 3

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo.
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls.
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
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


def extract_code(phone_num):
    '''extract codes from phone_num.
       The function returns two outputs, phone_type and code.
       phone_type:
       0: fixed line
       1: Mobile
       2: Telemarketer
       None: unknown type (code is also None in this case)
    '''
    if phone_num.startswith('(') and phone_num.find(')') > 0:
        return 0, phone_num[1:phone_num.find(')')]
    elif ' ' in phone_num:
        return 1, phone_num.split(' ')[0]
    elif phone_num.startswith('140'):
        return 2, '140'
    else:
        return None, None

list_code = set()
total_call = 0
bangalore_call = 0

for call in calls:
    c_phone_t, c_code = extract_code(call[0])
    if c_phone_t == 0 and c_code == '080':
        rec_phone_type, rec_code = extract_code(call[1])
        total_call += 1
        if rec_phone_type is not None:
            list_code.add(rec_code)
        if rec_phone_type == 0 and rec_code == '080':
            bangalore_call += 1

print("The numbers called by people in Bangalore have codes:")
for c in list_code:
    print(c)

tmpl = ("%.2f percent of calls from fixed lines in Bangalore are calls"
        "to other fixed lines in Bangalore.")
print(tmpl % (float(bangalore_call)*100/float(total_call)))

