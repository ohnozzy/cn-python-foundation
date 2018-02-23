"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo.
Full submission instructions are available on the Project Preparation page.
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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
phone = set()
o_tmpl = 'There are %d different telephone numbers in the records.'
for text_msg in texts:
    phone.add(text_msg[0])
    phone.add(text_msg[1])

for call_msg in calls:
    phone.add(call_msg[0])
    phone.add(call_msg[1])

print(o_tmpl % len(phone))

