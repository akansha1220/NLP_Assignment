
from nltk.tokenize import word_tokenize, sent_tokenize
import textstat
import re
from nltk.corpus import stopwords


try:
    def calculate_positive_score(text, positive_words):
        tokens = word_tokenize(text.lower())
        return sum(1 for word in tokens if word in positive_words)


    def calculate_negative_score(text, negative_words):
        tokens = word_tokenize(text.lower())
        return sum(1 for word in tokens if word in negative_words)


    #  in this function pastive the positive and negative score and finding the polarity score using the formula
    def calculate_polarity_score(positive_score, negative_score):
        return round((positive_score - negative_score) / ((positive_score + negative_score) + 0.000001),2)

    #  in this function postive the positive and negative score and finding the subjectivity score using the formula
    def calculate_subjectivity_score(text, positive_score, negative_score):
        tokens = word_tokenize(text)
        total_words = len(tokens)
        return round((positive_score + negative_score) / (total_words + 0.000001),2)

    #  in this function passing the text and finding the average length of text
    def calculate_avg_sentence_length(text):
        sentences = sent_tokenize(text)
        words = word_tokenize(text)
        return round(len(words) / len(sentences),2)


    #  in this function passing the text and finding the complex words
    def calculate_percentage_complex_words(text):
        words = word_tokenize(text)
        complex_words = [word for word in words if textstat.syllable_count(word) > 2]
        return round(len(complex_words) / len(words),2)

    #  in this function passing the text and finding the fog index
    def calculate_fog_index(avg_sentence_length, percentage_complex_words):
        return round(0.4 * (avg_sentence_length + percentage_complex_words),2)

    #  in this function passing the text and finding the average words in a sentense
    def calculate_avg_words_per_sentence(text):
        sentences = sent_tokenize(text)
        words = word_tokenize(text)
        return round(len(words) / len(sentences))

    #  in this function passing the text and finding the number of complex words
    def calculate_complex_word_count(text):
        words = word_tokenize(text)
        return sum(1 for word in words if textstat.syllable_count(word) > 2)


    #  in this function passing the text and finding the total number of words in text
    def calculate_word_count(text):
        word = set(stopwords.words('english'))
        tok_words = word_tokenize(text.lower())
        words = [i for i in tok_words if i not in word]
        return len(words)

    #  in this function passing the text and finding the syllables in a word
    def calculate_syllables_per_word(text):
        words = word_tokenize(text)
        return round(sum(textstat.syllable_count(word) for word in words) / len(words),2)

    #  in this function passing the text and finding the average word length of text
    def calculate_personal_pronouns(text):
        return len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))


    #  in this function passing the text and finding the total number of personal pronouns score
    def calculate_avg_word_length(text):
        words = word_tokenize(text)
        return round(sum(len(word) for word in words) / len(words),2)

except Exception as e:
    print(e)

# this function calling the all the calculated function 
def analyze_text(article_text, positive_words, negative_words):

    positive_score = calculate_positive_score(article_text, positive_words)
    negative_score = calculate_negative_score(article_text, negative_words)
    polarity_score = calculate_polarity_score(positive_score, negative_score)
    subjectivity_score = calculate_subjectivity_score(article_text, positive_score, negative_score)
    avg_sentence_length = calculate_avg_sentence_length(article_text)
    percentage_complex_words = calculate_percentage_complex_words(article_text)
    fog_index = calculate_fog_index(avg_sentence_length, percentage_complex_words)
    avg_words_per_sentence = calculate_avg_words_per_sentence(article_text)
    complex_word_count = calculate_complex_word_count(article_text)
    word_count = calculate_word_count(article_text)
    syllables_per_word = calculate_syllables_per_word(article_text)
    personal_pronouns = calculate_personal_pronouns(article_text)
    avg_word_length = calculate_avg_word_length(article_text)
    
    
    return {
        'Positive Score': positive_score,
        'Negative Score': negative_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score,
        'Avg Sentence Length': avg_sentence_length,
        'Percentage of Complex Words': percentage_complex_words,
        'Fog Index': fog_index,
        'Avg Number of Words per Sentence': avg_words_per_sentence,
        'Complex Word Count': complex_word_count,
        'Word Count': word_count,
        'Syllables per Word': syllables_per_word,
        'Personal Pronouns': personal_pronouns,
        'Avg Word Length': avg_word_length
    }