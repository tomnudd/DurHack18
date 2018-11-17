import nltk
import wikipedia

blackmailWords = {"sex", "masturbation", "murder", "minecraft", "serial killer", "fetish", "leather", "kink", "cult"}
blackmailDict = {}

def askQuestion(string):
    """
    :param string:
    :returns a tuple of a list of wikipedia summaries releavant to the question and a boolean indicating whether the question can be used as blackmail:
    """
    isBlackmail = 0
    blackmailDict.clear()
    for word in blackmailWords:
        blackmailDict.update({word:0})
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
                adviceLst.append(wikipedia.summary(title[0]))
                page = wikipedia.WikipediaPage(title[0])
                findBlackmail(page.content)

    for word in blackmailWords:
        if blackmailDict[word] > len(nouns) *3:
            isBlackmail = 1
    return [adviceLst, isBlackmail]

def findBlackmail(content):
    # adapted from user Boa on https://stackoverflow.com/questions/33587667/extracting-all-nouns-from-a-text-file-using-nltk
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(content)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

    for noun in nouns:
        for word in blackmailWords:
            if word == noun.lower():
                blackmailDict[word] += 1

def test():
    print(askQuestion("Am I ready to have sex?"))
