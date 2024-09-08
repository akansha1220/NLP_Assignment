import os
import data_analysis as da
import pandas as pd
from nltk.tokenize import word_tokenize
import data_analysis as da
from config import Config

config = Config()


def remove_stopwords(text):
    try:
        with open(config.STOPWORD_FILE_PATH,'r') as f:
            stop_word = f.read()
        tokens = word_tokenize(text)
        words = [word for word in tokens if word.lower() not in stop_word]
        return " ".join(words)
    except Exception as e:
        print(f"Unable to read file issue occure at {e}")



# function to iterate over the extracted files one by one 
def read_input_file(positive_words, negative_words): 
    try:
        results_stopwords = []  
        results_nostopwords = []  

        data = pd.read_excel(config.INPUT_FILE_PATH)
        total_row = data.shape  
        
        for i in range(total_row[0]):
            with open(f"{config.EXTRACTED_FILE_PATH}/{data.URL_ID[i]}.txt", 'r',encoding='utf-8') as f:
                article_text = f.read()
                
               
             
            #callin the analyze-text funtion
            analysis_withstopwords = da.analyze_text(article_text, positive_words, negative_words)
            results_stopwords.append({**data.loc[i,:].to_dict(), **analysis_withstopwords})
       

             # first remove the stop words and do tokenization
            tokenize_text =remove_stopwords(article_text)
            analysis_nostopwords = da.analyze_text(tokenize_text, positive_words, negative_words)
            results_nostopwords.append({**data.loc[i,:].to_dict(), **analysis_nostopwords})

        # returning the result dictonary
        return [results_stopwords,results_nostopwords]


    except Exception as e:
        print(e)
    

# here extracting the positive and negative words from the repective files 
with open(config.POSITIVE_FILE_PATH, 'r') as f:
    positive_words = f.read().splitlines()
        
with open(config.NEGATIVE_FILE_PATH, 'r') as f:
        negative_words = f.read().splitlines()



# here callling the read file function    
result = read_input_file(positive_words, negative_words)
result_df = pd.DataFrame(result[0])
result_df.to_excel(f'{config.OUTPUT_FILE_PATH}/Output.xlsx', index=False)
result_df2 = pd.DataFrame(result[1])
result_df2.to_excel(f'{config.OUTPUT_FILE_PATH}/Output_NoStopwords.xlsx', index=False)
print("Analysis complete and results saved.")
