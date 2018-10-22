# Place any necessary imports here
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


####################################################
# Part 0
####################################################

# Move your parsers.py file to your Problem Set 7
# directory. Once you've done so, you can use the 
# following code to have access to all of your parsing
# functions. You can access these functions using the 
# parsers.<function name> notation as in: 
# parsers.countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt')

import parsers.py

####################################################
# Part 1
####################################################

def populateDatabase(databaseName, wordCounts, metaData):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    for file in wordCounts:
        for word in file:
            c.execute(''' INSERT INTO SOTUWordCount_DT(filename, Word, Count) values ({0},{1},{2})'''
            c.execute( '''INSERT INTO US_Presidents_DT(Index, number, start, end, president, prior, party, Vice) values({0},{1},{2},{3},{4},{5},{6},{7},{8})'''
    c.execute()    
    conn.commit() 
    conn.close()
    return 0

populateDatabase("POTUS_SOTU.db", wordCounts)

####################################################
# Part 2
####################################################

def searchDatabase(databaseName, word): 
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute('''SELECT count, MAX(count) AS "Most Used Word" FROM Table1 GROUP BY word''')
    conn.commit() 
    conn.close()
    return 0
    
searchDatabase('POTUS_SOTU.db','congress')
  
def computeLengthByParty(databaseName): 
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute('''SELECT count, AVG(count) AS "Most Used Word by Party" FROM Table1 GROUP BY party''')
    conn.commit() 
    conn.close()
    return 0
    
computeLengthByParty('POTUS_SOTU.db')
    
#Not sure if these are right. I tried to use the syntax from the SQL powerpoint provided on canvas, but I am unable to check them since I was never able to upload the data to my database. 

#Wednesday

#Question 1
obesity_df = pd.read_csv('CDC_Obesity_Data.csv')

print(obesity_df['Question'].unique())

#Question 2
print(obesity_df["Data_Value"].sum())

#Question 3
X = obesity_df[obesity_df['Question'] == 'Percent of adults aged 18 years and older who have obesity']
X_0 = X.fillna(0)
Y = X_0['Data_Value']

sns.distplot(Y)

#Question 4
obesity_df.plot(kind='hist', x=['YearStart'], y=['Data_Value'])

#I thought these plots printed out a little more nicely in Jupyter, I've included the .ipynb file if you'd rather look at that. 