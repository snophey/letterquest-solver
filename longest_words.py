import nltk, sys
from word_comparator import WordComparator
from nltk.corpus import words
nltk.download('words')
word_list = words.words()

def process_word(word):
    result = [0 for i in range(0, 26)]
    word = word.lower()
    for c in word:
        code = ord(c) - ord('a')
        if (code < 0 or code >= len(result)):
            return None # signalize that the word contains invalid characters
        result[code] += 1
    return result

def is_subset(superset, subset):
    assert (len(superset) == len(subset))
    for i in range(len(superset)):
        if superset[i] < subset[i]:
            return False
    return True

comparator = WordComparator()
def longest_words_for_given_letters(available_letters : list):
    result = [None for i in range(0,15)]
    for word in word_list:
        if len(word) > 15:
            continue
        letters_in_word = process_word(word)
        if not letters_in_word:
            continue
        if is_subset(available_letters, letters_in_word):
            index = len(word)-1
            result[index] = comparator.better_word(result[index], word)

    result.reverse()
    return [elem for elem in result if elem is not None]