import nltk, sys
nltk.download('words')

from nltk.corpus import words
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

result = []

available_letters = process_word(sys.argv[1])
longest_match = 'a'
for word in word_list:
    if len(word) > 15:# or len(word) < len(longest_match):
        continue
    letters_in_word = process_word(word)
    if not letters_in_word:
        continue
    if is_subset(available_letters, letters_in_word):
        longest_match = word
        result.append(word)
        if (len(word) == 15):
            break # early exit because its not possible to find a longer match

result.sort(key=lambda x: len(x))
for word in result:
    print(word)
