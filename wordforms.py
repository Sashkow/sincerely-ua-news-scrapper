import csv
import itertools
import pandas as pd
import datetime

dict_path = 'dict-ua/dict_corp_lt.txt'
df = pd.read_csv(dict_path, sep=' ')
df.columns = ['wordform', 'word', 'flags']


def generate_wordforms(word):


    # before = datetime.datetime.now()
    # print(df['word'].searchsorted(word))
    # print(datetime.datetime.now() - before)

    before = datetime.datetime.now()
    # find wordform
    wordform = df[(df['wordform']==word) & (df['flags'].str.contains('v_naz'))]
    # find fordform's form coded as flags excluding flag for grammatical case
    flags = wordform['flags'].values[0]
    if not ':v_naz' in flags:
        return [word]
    flags = flags.replace(':v_naz', '')
    # find initial form of the word
    theword = wordform['word'].values[0]
    # find all wordforms of the word with appropriate flags
    wordforms = df[(df['word'] == theword) & (df['flags'].str.contains(flags))]
    print(datetime.datetime.now() - before)

    return wordforms['wordform'].values

    # print(type(df['flags'].str.contains('v_naz')))

def generate_phraseforms(phrase):
    """
    if not naz or in quotes then no wordforms
    """
    quotes = False
    words = phrase.split(' ')
    words[0] = words[0].lower()
    for word in words:
        if '"' in word:
            quotes = not quotes
            continue
        if not quotes:
            print(word)
            wordforms = df[df['wordform'] == word]
            wordformso


            print(type(wordforms))

            for i, wordform in wordforms.iterrows():
                print(wordform)
                print("naz" in str(wordform['flags']))

def replace_quotes():
    quotes = ['«', '»', '„', '“', '‟', '”', '"', '❝', '❞', '⹂', '〝', '〞', '〟', '＂']
    with open('parties', 'r') as f:
        parties = f.read()

    for quote in quotes:
        parties = parties.replace(quote, '"')
    print(parties)





