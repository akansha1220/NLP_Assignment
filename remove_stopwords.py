import os
# this file we will remove the stop words 

# first append the stopwords in a single file

file_name = ['StopWords_Auditor.txt','StopWords_DatesandNumbers.txt','StopWords_Currencies.txt','StopWords_Generic.txt','StopWords_GenericLong.txt','StopWords_Geographic.txt','StopWords_Names.txt']

for i in file_name:
    with open(f"input/StopWords/{i}",'r') as f:
        stop_words = f.read()

        with open('Input/StopWords/all_stopwords.txt','+a') as file:
            file.write(stop_words)