#!/usr/bin/env python
# script to convert Santander Bank (Polish) CSV files
# to Denaro CSV format
# See Denaro documentation:

# 

# Santander CSV format:
# 0 Date of accounting; 1 Date of transaction; 2 Description; 3 Account owner; 4 Account number; 5 Amount (negative means an expense; 6 Balance after transaction; 7 ID
# Denaro CSV format:
# https://htmlpreview.github.io/?https://raw.githubusercontent.com/NickvisionApps/Denaro/main/NickvisionMoney.Shared/Docs/html/C/import-export.html 
# ID;Date;Description;Type;RepeatInterval;RepeatFrom;RepeatEndDate;Amount;RGBA;UseGroupColor;Group;GroupName;GroupDescription;GroupRGBA

import csv
from datetime import datetime

with open("santander-export.csv") as csvSrc:
        csvFile = csv.reader(csvSrc, delimiter=',', quotechar='"')
        for row in csvFile:
            amount = row[5].replace(",", ".")
            denaroLine = row[7] + ';' + \
                datetime.strptime(str(row[1]), "%d-%m-%Y").strftime("%m/%d/%Y") + ';' \
                + row[2] + ';'\
                + str(1 if (float(amount) < 0) else 0) + ';'\
                + '0;'\
                + '-1;'\
                + ';'\
                + amount + ';'\
                + ';'\
                + '0;'\
                + '-1;'\
                + ';'\
                + ';'\
                + ';'
                
            print(denaroLine)
