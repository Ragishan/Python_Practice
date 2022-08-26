#creating a file handle with open() with read attribute
"""
fhand = open("mbox.txt", "r")
print(fhand)
"""
#creating a for loop to read the total number of lines in the file
"""
fhand=open('mbox.txt','r')
count = 0
for lines in fhand:
    count+=1
print(count)
"""

#read the contents of the file and extracting email and store same in a panda dataframe
"""
import pandas as pd  
import numpy as np 
import re

fhand = open('mbox.txt')
newc = []
for i in fhand:
    i = i.rstrip()
    if re.match("From: (.*)@(.*).(.*)",i):
        newc.append(i.lstrip('From: '))
df = pd.DataFrame(newc,columns= ["Emails"])
print(df)
"""
        
#Read the contents of the file and define a method to extract emails -> 
# store the emails in a pandas framework -> save it in a file -> 
# append the file if already exists else always create a new one
"""
import pandas as pd
import re 


def extract_mails(file_hand): #extracting emails method
    emails = []
    for i in file_hand:
        i = i.rstrip() # to remove the trailing newline char
        #if re.search('From: (.*)@(.*).(.*)',i): 
         #   emails.append(i.lstrip('From: '))
        emails.append(re.findall(r'[\w\.-]+@[\w\.-]+', i)) #this is for files like 100-contacts.csv
    return emails

fname = input('Enter a filename: ') #user input for a filename and checking if such file exists or not
try:
    fhand = open(fname)
except:
    print('Please enter a correct filename- ' + fname + ' does not exist')
    exit()

email_ids = extract_mails(fhand) #storing emails extracted for the file
emaildf = pd.DataFrame(email_ids,columns= ["Extracted_Emails"]) 
emaildf.to_csv("extracted_emails.csv",index=False, header=False, sep=',',mode='a') #writing the data frame to a file using append mode. Keep index and header false in append mode--obviously

"""

# Read the contents of a file -> print out everything is UPPER CASE
"""
fhand =  open('mbox-short.txt')
for i in fhand:
    print(i.upper())
"""

# Prompt for a filename -> Read the file and find X-DSPAM-Confidence:0.8475 -> Strip floating number ->
# Find and print average of all these numbers
"""

import re

fname = input("Please enter a file name: ")
fhand = open(fname)
conf_list = []
new_conf_list = []
total = 0
average = 0.0
for i in fhand:
    if re.match('X-DSPAM-Confidence:(.*)',i):
        i = i.rstrip()
        i = i.lstrip('X-DSPAM-Confidence: ')
        conf_list.append(i)

for x in range(len(conf_list)):
    new_conf_list.append(float(conf_list[x]))

for y in range(len(new_conf_list)):

    total += new_conf_list[y]

average = total / len(conf_list)    
print('Average spam confidence: ' + str(average))
"""
