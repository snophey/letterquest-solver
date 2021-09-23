import nltk, sys
from word_comparator import WordComparator
from nltk.corpus import words
nltk.download('words')
word_list = words.words()

if len(sys.argv) != 2:
    print("Usage: {} [list of available letters]".format(sys.argv[0]))
    sys.exit(1)

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
            result[index] = comparator.compare(result[index], word)

    result.reverse()
    return result

for word in longest_words_for_given_letters(process_word(sys.argv[1])):
    if word:
        print(word)
