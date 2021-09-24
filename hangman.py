import nltk, sys
from word_comparator import WordComparator
from nltk.corpus import words
import re
nltk.download('words')
word_list = words.words()

comparator = WordComparator()

def get_matches(pattern : str, unavailable_letters: str, limit : int = 20):
    """Get words that match the given pattern.
    
    Given a string pattern where each unknown letter is replaced by '-', find words
    that match this pattern. The limit parameter specifies the maximum number of matches
    returned. Matches are sorted according to WordComparator.
    """
    word_len = len(pattern)
    alphabet = ''.join([char for char in "abcdefghijklmnopqrstuvwxyz" if char not in unavailable_letters])
    regex = re.compile("^{}$".format(pattern.replace('-', '[{}]'.format(alphabet))))
    result = []
    for word in word_list:
        if len(word) == word_len and regex.match(word.lower()):
            result.append(word)
            if len(result) >= limit:
                break
    return sorted(result,key=lambda x: comparator.evaluate_word(x), reverse=True)


