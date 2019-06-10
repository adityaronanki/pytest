__author__ = 'Khali'

notes = '''
1. Read instructions for each function carefully.
2. Try to use builtins and data structures instead of writing your own.
3. If something about the function spec is not clear, use the corresponding test
   for clarification
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists, only use string functions
# assume words are separated by spaces. you can use control flow statements
# your code goes here
def prune_either_or(sentence):
    str1=""
    if((sentence.find('either') !=-1)  and (sentence.find('or')!=-1)):
        x=sentence.split()
        for y in range(0,len(x)):
            if(x[y]=='either'):
                continue
            elif(x[y]=='or'):
                break
            else:
                str1=str1+x[y]+" "
        str1=str1.rstrip()
        return str1
    else :
        return sentence


# Create a palindrome of twice the length of the word passed in.
# e.g. app -> appppa, bat -> battab etc.
# hint: look up extended slice notation.
def create_palindrome(word):
    if word == None:
        return None
    else:
       return word+word[::-1]

# returns a dict which maps a -> 1, b -> 2 ... z->26 and A -> 1, B ->2 ... Z->26
# no control flow.
def get_encoding_dict():
    thisdict={
        'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8,
        'i':9,
        'j':10,
        'k':11,
        'l':12,
        'm':13,
        'n':14,
        'o':15,
        'p':16,
        'q':17,
        'r':18,
        's':19,
        't':20,
        'u':21,
        'v':22,
        'w':23,
        'x':24,
        'y':25,
        'z':26,
        'A':1,
        'B':2,
        'C':3,
        'D':4,
        'E':5,
        'F':6,
        'G':7,
        'H':8,
        'I':9,
        'J':10,
        'K':11,
        'L':12,
        'M':13,
        'N':14,
        'O':15,
        'P':16,
        'Q':17,
        'R':18,
        'S':19,
        'T':20,
        'U':21,
        'V':22,
        'W':23,
        'X':24,
        'Y':25,
        'Z':26,

    }
    return thisdict


def test_either_or_pruning():
    assert "We can go to a movie" == prune_either_or("We can either go to a movie or a hotel")
    assert "We can go either way" == prune_either_or("We can go either way")
    assert "" == prune_either_or("either or")
    assert "either way is fine" == prune_either_or("either way is fine")

def test_create_palindrome():
    assert "battab" == create_palindrome("bat")
    assert "abba" == create_palindrome("ab")
    assert "" ==create_palindrome("")
    assert None == create_palindrome(None)

def test_get_encoding_dict():
    d = get_encoding_dict()
    assert len(d) == 52
    for key in d:
        assert ord(key.lower()) - ord('a') + 1 == d[key]

three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___
