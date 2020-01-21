# coding: utf-8
# Name: Suzanna (Neely) Yates
#
#

import random

def createDictionary(filename):
    """
    Inputs filename
    Outputs a dictionary of the file.
    """
    f = open(filename)
    text = f.read()
    f.close()
    LoW = text.split()

    d = {}
    pw = "$"
    for nw in LoW:
        if pw not in d: 
            d[pw] = [nw]
        else:
            d[pw] += [nw]
        pw = nw
        if nw[-1] in ".!?":
            pw = "$"
    return d

def generateText(d, N):
    """
    Inputs the dictionary and number of words. 
    Outputs the text.
    """
    first_word = random.choice(d["$"])
    result = first_word
    word = first_word
    for i in range(N-1):
        if word[-1] in ".!?": 
            word = random.choice(d["$"])
            result += " " + word
        else:
            word = random.choice(d[word]) 
            result += " " + word
    return result