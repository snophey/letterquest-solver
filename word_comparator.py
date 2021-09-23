import nltk
from os.path import exists
from collections import Counter
from nltk.corpus import brown
from nltk.corpus import reuters
from nltk.stem import PorterStemmer
import pickle
import time

class WordComparator:
    COUNTER_FILE_NAME = "word_counts.dump"

    def __init__(self):
        print("Initializing word comparator...")
        start_time = time.time()
        self.word_counter = self.word_frequencies()
        print("Done. Initialization took {} seconds.".format(time.time() - start_time))
    
    def compare(self, word1 : str, word2 : str):
        if word1 == None or word2 == None:
            return word1 if word2 == None else word2
        return word1 if self.word_counter[word1] > self.word_counter[word2]  else word2
    
    def word_frequencies(self):
        if exists(WordComparator.COUNTER_FILE_NAME):
            return pickle.load(open(WordComparator.COUNTER_FILE_NAME, "rb"))
        else:
            counter = self.compute_word_frequencies()
            pickle.dump(counter, open(WordComparator.COUNTER_FILE_NAME, "wb"))
            return counter
    
    def compute_word_frequencies(self):
        nltk.download('brown')
        nltk.download('reuters')
        counter = Counter()
        counter.update(self.normalize_words(brown.words()))
        counter.update(self.normalize_words(reuters.words()))
        return counter
    
    def normalize_words(self, words : list):
        stemmer = PorterStemmer()
        return [stemmer.stem(word.lower()) for word in words]
    
    def serialize_counts(self):
        self.word_counter


