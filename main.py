from fastapi import FastAPI
from longest_words import longest_words_for_given_letters, process_word
from hangman import get_matches

app = FastAPI()

@app.get("/words/{alphabet}")
async def longest_words(alphabet : str):
    return longest_words_for_given_letters(process_word(alphabet))

@app.get("/hangman/{pattern}/{used_letters}/{limit}")
async def hangman(pattern : str, used_letters : str, limit : int = 20):
    return get_matches(pattern, used_letters, limit)
