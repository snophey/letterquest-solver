from fastapi import FastAPI
from longest_words import longest_words_for_given_letters, process_word

app = FastAPI()

@app.get("/lq/{alphabet}")
async def root(alphabet : str):
    return longest_words_for_given_letters(process_word(alphabet))
