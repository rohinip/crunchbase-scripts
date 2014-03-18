# Import Libraries
import sys
import os
import json
import urllib
import urllib2
import requests
import csv
import argparse

# Basic information from user
parser = argparse.ArgumentParser(description='Enter your Crunchbase API key and company list CSV')
parser.add_argument('-k', '--key', help='type in your Crunchbase API key', required=True)
parser.add_argument('-c', '--csv', help='type in the path to the CSV file', required=True)
args = parser.parse_args()
 
# Global Variables
apiKey = args.key
ipath = args.csv
opath = 'updated_' + ipath
ifile  = open(ipath, 'rU')
ofile  = open(opath, 'wb')
reader = csv.reader(ifile)
writer = csv.writer(ofile)

# Read CSV
rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            # For Company column, get the crunchbase response
            if colnum == 1:
                if ", Inc." in col:
                    col = col.replace (", Inc.", "-inc")
                elif "." in col:
                    col = col.replace (".", "-")
                col = col.replace (" ", "+")
                requestURL = 'http://api.crunchbase.com/v/1/company/%s.js?api_key=%s' % (col, apiKey) 
                r = requests.get(requestURL)
                responseBody = json.loads(r.text) #nothing has been done to take care of nulls or if the name has characters (such as periods) in it
            # For the Employees column
            elif colnum == 6:
                try:
                    col = responseBody[u'number_of_employees']
                except:
                    col = "0"
                row[colnum] = col
            # For the Total Raised column
            elif colnum == 7: 
                try:
                    col = responseBody[u'total_money_raised']
                except:
                    col = "$0"
                row[colnum] = col
            # For the Acquired By column
            elif colnum == 8:
                try:
                    col = responseBody[u'acquisition'][0][u'acquiring_company']
                except:
                    col = "none"
                row[colnum] = col
            # For the City column
            elif colnum == 9: 
                try:
                    col = responseBody[u'offices'][0][u'city']
                except: 
                    col = "na"
                row[colnum] = col
            print '%-15s: %s' % (header[colnum], col)
            colnum += 1
        print row
        writer.writerow(row)
        print '---------------------------'

    rownum += 1

ifile.close()
ofile.close()
