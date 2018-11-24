# Copyright Da Real MC (2018)
import random

def generateBlackmail(username):
    blackmail = ["'s default text editor is Notepad",
    "'s mum circulates like a public key, servicing more requests than HTTP",
    "'s momma is so fat she loses data when not shut down cleanly",
    " listens to Jake Paul's \"It's Everday Bro\" on the daily",
    "'s momma is so fat she turned a binary tree into a linked list in constant time",
    "'s contributions get piped to /dev/null",
    " drinks lemonade at a free bar",
    " might be able to hack a program together, but will never hack social etiquette",
    "'s code has never compiled",
    " supports a No Deal Brexit",
    " will only ever be qualified in IT support",
    " believes Klute is a upmarket establishment",
    " needed 180 LMC mailboxes to convert into base 10"
    " enjoys working through Rob's CT notes",
    " thinks that Steve Jobs was a genius computer scientist",
    " mixes up Halloween and Christmas because Oct 31 equals Dec 25",
    " belives that HTML is a programming language"]

    return username + random.choice(blackmail)
