"""I've tracked my spending via ad hoc text files and shell scripts.  I
thought I should try entering the world of spreadsheets and databases,
and wrote this to convert the files.

 started 18:07, basically done 19:22
played around, then added sorting and date, 20:35

file names e.g. Jan2014, Apr2010, June2014
older files JAN2000, different format, skipped
"""

header= '"Date","Year","Month","Day","Amount","Category","Desc"\n'

import os
from os import listdir
import csv
import datetime

"""
grep F$ $1 | asum
grep R$ $1 | asum
grep RP$ $1 | asum
grep toilet $1 | asum
grep transport $1 | asum
grep laundry $1 | asum
grep medic $1 | asum
grep enter $1 | asum
grep phone $1 | asum
grep power $1 | asum
grep rent $1 | asum
grep fees $1 | asum
grep book $1 | asum
grep comic $1 | asum
grep video $1 | asum
grep photo $1 | asum
grep gift $1 | asum
grep text $1 | asum
grep IU $1 | asum
grep big $1 | asum
grep misc $1 | asum
"""

def categorize(s): #stripped string input, returns string
    """ str -> str
    given an entry, categorize it. Includes logic for flagging
    problems in the input."""

    category = ""; categorized=False; ambiguous=False
    if l[-1] == 'F':
        category= "grocery"
        categorized=True
    if l[-1] == 'R':
        if categorized: ambiguous = True
        category= "eat out"
        categorized=True
    if l[-2:] == 'RP':
        if categorized: ambiguous = True
        category= "eat out"
        categorized=True
    if "toilet" in l:
        if categorized: ambiguous = True
        category= "toilet"
        categorized=True
    if "transport" in l:
        if categorized: ambiguous = True
        category= "transport"
        categorized=True
    if "laundry" in l:
        if categorized: ambiguous = True
        category= "laundry"
        categorized=True
    if "medic" in l:
        if categorized: ambiguous = True
        category= "medical"
        categorized=True
    if "enter" in l:
        if categorized: ambiguous = True
        category= "entertainment"
        categorized=True
    if "phone" in l:
        if categorized: ambiguous = True
        category= "phone"
        categorized=True
    if "power" in l:
        if categorized: ambiguous = True
        category= "power"
        categorized=True
    if "rent" in l:
        if categorized: ambiguous = True
        category= "rent"
        categorized=True
    if "fees" in l:
        if categorized: ambiguous = True
        category= "fees"
        categorized=True
    if "book" in l:
        if categorized: ambiguous = True
        category= "book"
        categorized=True
    if "comic" in l:
        if categorized: ambiguous = True
        category= "comic"
        categorized=True
    if "video" in l:
        if categorized: ambiguous = True
        category= "video"
        categorized=True
    if "photo" in l:
        if categorized: ambiguous = True
        category= "photo"
        categorized=True
    if "gift" in l:
        if categorized: ambiguous = True
        category= "gift"
        categorized=True
    if "text" in l:
        if categorized: ambiguous = True
        category= "textbook"
        categorized=True
    if "IU" in l:
        if categorized: ambiguous = True
        category= "IU"
        categorized=True
    if "big" in l:
        if categorized: ambiguous = True
        category= "bigmisc"
        categorized=True
    if "misc" in l:
        if categorized: ambiguous = True
        category= "misc"
        categorized=True

    #unneeded in the final run, but were useful in cleaning up the input
    if category=="":
        print("uncategorized",l)
    if ambiguous:
        print("ambiguous",l)

    return category
    

def transmonth(m):
    """ str -> int
    month name->numeric translation function for my filenames"""

    months={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'June':6,'July':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    return months[m]

#main
with open("money.csv","w") as outfile:
    outfile.write(header)
    outlines=[]
    csvwriter = csv.writer(outfile,dialect='unix')
    for fn in os.listdir():
        if "csv" in fn: continue  #avoid reading this code
        if fn.upper() == fn: continue #skipping older files in different format
        year = int(fn[-4:])
        month = fn[:-4]
        print("FILE",year,month,fn)  #progress tracker
        with open(fn,"r") as f:
            for l in f:
                l=l.strip()  
                if l=="": continue
                cat = categorize(l)
                fields = l.split()
                amount=float(fields[0])
                desc = " ".join(fields[1:])
                date = datetime.date(int(year),transmonth(month),1)
                out=[date,year,month,1,amount,cat,desc]
                #print(out)
                outlines.append(out)

    #done with files, sort by date
    outlines.sort(key=lambda k:k[0])
    for l in outlines:
        l[0]=str(l[0])  #csv needs everything to be strings
        csvwriter.writerow(l)
