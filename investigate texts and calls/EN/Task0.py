"""
Intro to Python Project 1, Task 0

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
TASK 0:
what is the first record of texts and what is the last record of calls
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
text_tmpl = "First record of texts, %s texts %s at time %s"
call_tmpl = "Last record of calls, %s calls %s at time %s, lasting %s seconds"
first_text = texts[0]
print(text_tmpl % (first_text[0], first_text[1], first_text[2]))
last_call = calls[-1]
print(call_tmpl % (last_call[0], last_call[1], last_call[2], last_call[3]))

