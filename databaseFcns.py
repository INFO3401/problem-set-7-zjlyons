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
    
    # Write a function that will populate your database
    # with the contents of the word counts and us_presidents.csv
    # to your database. 
    # Inputs: A string containing the filepath to your database,
    #         A word count dictionary containing wordcounts for 
    #         each file in a directory,
    #         A metadata file containing a dictionary of data
    #         extracted from a supplemental file
    # Outputs: None
    #return 0

# Test your code here

####################################################
# Part 2
####################################################

#def searchDatabase(databaseName, word): 
    # Write a function that will query the database to find the 
    # president whose speech had the largest count of a specified word.
    # Inputs: A database file to search and a word to search for
    # Outputs: The name of the president whose speech contained 
    #          the highest count of the target word
    #return 0

#def computeLengthByParty(databaseName): 
    # Write a function that will query the database to find the 
    # average length (number of words) of a speech by presidents
    # of the two major political parties.
    # Inputs: A database file to search and a word to search for
    # Outputs: The average speech length for presidents of each 
    #          of the two major political parties.
    #return 0
    

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
