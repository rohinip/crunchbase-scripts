crunchbase-scripts
==================

Steps: 
1. From the VC pages on crunchbase.com (e.g., http://www.crunchbase.com/financial-organization/andreessen-horowitz) copy the "Investments" list into an Excel spreadsheet
2. Insert a new column #2 and use the '=LEFT(A2, LEN(A2)-2)' command to remove the last 2 (or 3 or 4) characters from the Company column so that you don't have any superscripts references in this new Company Name column
3. Add columns in the spreadsheet to track Number of Employees, Total Money Raised, Acquiring Company (if they were acquired), and Office Location
4. Save that spreadsheet as a CSV
5. Run the crunchbase.py script with your Crunchbase API key and the CSV you've just created
6. The output will be stored as the same name of the CSV with "_updated" appended to it

Usage:
python crunchbase.py -k [apikey] -c [filename].csv