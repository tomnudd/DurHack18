import nltk
import wikipedia

def askQuestion(string):
    adviceLst = list()

# adapted from user Boa on https://stackoverflow.com/questions/33587667/extracting-all-nouns-from-a-text-file-using-nltk
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(string)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    for noun in nouns:
            title = wikipedia.search(noun, 1, True)
            if title[0] is not None:
                adviceLst.append(wikipedia.summary(title))
    print(adviceLst)
    return adviceLst

def test():
    askQuestion("The world is ugly, but you're beautiful to me. The cat is cute.")
