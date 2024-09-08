import os
from dotenv import load_dotenv

load_dotenv()



class Config(object):
    #application config
    lang_array = ["en", "hi"]
    INPUT_FILE_PATH = os.environ['INPUT_FILE_PATH']
    STOPWORD_FILE_PATH = os.environ['STOPWORD_FILE_PATH']
    POSITIVE_FILE_PATH = os.environ['POSITIVE_FILE_PATH']
    NEGATIVE_FILE_PATH = os.environ['NEGATIVE_FILE_PATH']
    OUTPUT_FILE_PATH = os.environ['OUTPUT_FILE_PATH']
    EXTRACTED_FILE_PATH = os.environ['EXTRACTED_FILE_PATH']