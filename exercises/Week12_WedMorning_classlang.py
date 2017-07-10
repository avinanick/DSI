'''
Design a data structure that supports the following 
two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a 
regular expression string containing only 
letters a-z or .. A-Z 

. means it can represent any one letter.

For example:

add_word("bad")
add_word("dad")
add_word("mad")
search("pad") == False
search("bad") == True
search(".ad") == True
search("b..") == True
'''

#Solution 1
import re

class WordDictionary:
    def __init__(self):
        self.word_list = []
  
    def add_word(self, word):
        self.word_list.append(word)
  
    def search(self, word):
        regex = "^" + word + "$"
        return bool([string for string in self.word_list if re.match(regex, string)])

#Solution 2 -- Thanks Tiffany! 

class Stuff:
    
    def __init__(self):
        self.wordList=[]
    
    def addWord(self, word):
        self.wordList.append(word)
        
    def search(self, word):
        return True in [re.search(word,w) != None for w in self.wordList]
