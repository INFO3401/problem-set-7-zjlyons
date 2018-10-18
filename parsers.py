################################################################################
# PART #1
################################################################################

# I worked with Steven, Harold, Justin, and Luke. 

import csv
import pandas as pd

wordcount = {}

def countWordsUnstructured(filename):
    file = open(filename)
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return(wordcount)
    
# Test your part 1 code below.
    
countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Trump_2017.txt')

################################################################################
# PART 2
################################################################################
    
def generateSimpleCSV(targetfile,wordCounts): 
    with open (targetfile,'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Word', 'Count'])
        for key, value in wordCounts.items():
            csv_writer.writerow([key,value])
    csv_file.close()
    return(csv_file)
    
generateSimpleCSV('wordcounts.csv', wordcount)

    
################################################################################
# PART 3
################################################################################

import os
from os import listdir
from os import chdir

def countWordsMany(directory): 
    dir_list = os.listdir(directory)
    wordCountDict = {}
    for file in dir_list:
        eachWordCount = countWordsUnstructured(directory + '/' + file)
        wordCountDict[file] = eachWordCount
    return wordCountDict

all_dicts = countWordsMany('./SOTU')


################################################################################
# PART 4
################################################################################
def generateDirectoryCSV(wordCounts, targetfile): 
    CSVfile=open(targetfile, 'w')
    CSVfile.write("filename, Word, Count\n")
    for wordfile, dict in wordCounts.items():
        for word, count in dict.items():
            CSVfile.write(wordfile + ',' + str(word) + ',' + str(count) + "n")
    CSVfile.close()
    return 

generateDirectoryCSV(all_dicts, 'targetfile.csv')
    
################################################################################
# PART 5
################################################################################
def generateJSONFile(wordCounts, targetfile): 
    file = open(targetfile, "w")
    file.write(str(wordCounts).replace("\'", "\""))
    
    file.close
    return file

generateJSONFile(all_dicts,'targetfile.json')
    

################################################################################
# PART 6
################################################################################
def searchCSV(csvfile, word): 
    largest_file= ""
    largest_count=0
    with open(csvfile, 'rt') as csv_file:
        file_read = csv.reader(csv_file, delimiter = ',')
        for line in file_read:
            if line[1] == word:
                if int(line[2]) > largest_count:
                    largest_count=int(line[2])
                    largest_file=line[0]
      
        return largest_file
        
        
print(searchCSV("targetfile.csv", "Congress"))

import json

def searchJSON(JSONfile, word): 
    largest_file= ""
    largest_count=0
    with open(JSONfile) as json_file:
        read_data= json.load(json_file, delimiter = ':')
        for file in read_data:
            if word in read_data[file] and read_data[file][word] > largest_count:
                largest_count=read_data[file][word]
                largest_file=file
        return largest_file
        json_file.close()


print(searchJSON("targetfile.json", "Congress"))
    

    
#Schema

#Table 1 : "SOTU_word_count"
    # "filename" (text)
    # "word" (text)
    # "count" (integer)
    
#Table 2 : "US_President_data"
    # "index" (integer)
    # "number" (integer)
    # "start" (date)
    # "end" (date)
    # "president" (text)
    # "prior" (text)
    # "party" (text)
    # "vice" (text)



#The tables can be joined by the president's name, and the date of speech/date of presidency. 

import sqlite3

conn = sqlite3.connect('POTUS_SOTU.db')
c = conn.cursor()

c.execute('''CREATE TABLE wordCounts (filename, word, count)''')
c.execute('''CREATE TABLE presidentInfo(index, number, start, end, president, prior, party, vice )''')

conn.commit()
conn.close()
