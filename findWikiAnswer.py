import nltk
# https://www.nltk.org/index.html
import wikipedia
import re

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

blackmailWords = {"sex", "masturbation", "murder", "minecraft", "serial killer", "fetish", "leather", "kink", "cult","baby","sexy","foreplay"}
blackmailDict = {}

def askQuestion(string):
    """
    :param string:
    :returns a tuple of a list of wikipedia summaries releavant to the question and a boolean indicating whether the question can be used as blackmail:
    """
    string = string.replace("?","")
    blackmailCount = 0
    adviceLst = list()
    if "who" in string:
        string = string.replace("who", "")
        string = string.replace("is", "")
        try:
            nouns = [string]
            title = wikipedia.search(string, 1, True)
            if title[0] is not None:
                adviceLst.append(wikipedia.summary(title[0]))
                page = wikipedia.WikipediaPage(title[0])
                blackmailCount = findBlackmailFromWiki(page.content)
        except:
            adviceLst.append("This question is beneath me, foolish mortal")
            blackmailCount *= 3

# adapted from user Boa on https://stackoverflow.com/questions/33587667/extracting-all-nouns-from-a-text-file-using-nltk
    # function to test if something is a noun
    else:
        is_noun = lambda pos: pos[:2] == 'NN'
        # do the nlp stuff
        tokenized = nltk.word_tokenize(string)
        nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

        for noun in nouns:
            try:
                title = wikipedia.search(noun, 1, True)
                if title[0] is not None:
                    adviceLst.append(wikipedia.summary(title[0]))
                    page = wikipedia.WikipediaPage(title[0])
                    blackmailCount += findBlackmailFromWiki(page.content)
                else:
                    adviceLst.append("This question is beneath me, foolish mortal")
                    blackmailCount *= 3
            except:
                adviceLst.append("This question is beneath me, foolish mortal")
                blackmailCount *= 3


    if blackmailCount > 3:
        blackmailCount = 3
    i = 0
    if len(adviceLst) == 0:
        adviceLst.append("Do not concern yourself with such matters.")
        blackmailCount = 2
    else:
        while i < len(adviceLst):
            advice = formatAdvice(adviceLst[i])
            adviceLst[i] = advice
            i += 1
    return [adviceLst, int(blackmailCount), nouns]

def findBlackmailFromWiki(content):
    blackmailCount = 0
    
    # adapted from user Boa on https://stackoverflow.com/questions/33587667/extracting-all-nouns-from-a-text-file-using-nltk
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(content)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

    for noun in nouns:
        for word in blackmailWords:
            if word == noun.lower():
                blackmailCount += 1
    return blackmailCount/4

def findBlackmail(content):
    blackmailLevel = 0
    # adapted from user Boa on https://stackoverflow.com/questions/33587667/extracting-all-nouns-from-a-text-file-using-nltk
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(content)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

    for noun in nouns:
        for word in blackmailWords:
            if word == noun.lower():
                blackmailLevel += 1
    if blackmailLevel > 3:
        blackmailLevel = 3
    return blackmailLevel

def formatAdvice(advice):
    temp = re.split('([.?!])', advice, 2)
    if len(temp) > 3:
        advice = temp[0] + temp[1] + temp[2] + temp[3]
    return advice

