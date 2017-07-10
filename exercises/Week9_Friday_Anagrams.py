'''
Friday morning exercise
Given a list of words L, find all the anagrams 
in L in the order in which they appear in L.

For example, given the input:
["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"]

The desired output would be:
["pool", "loco", "cool", "stain", "satin", "loop"]
in that order exactly.

'''

# Solution 1
from collections import defaultdict

def hasher(w):
    return "".join(sorted(w))

def anagram_finder(word_list):

    hash_dict = defaultdict(list)

    for word in word_list:
        hash_dict[hasher(word)].append(word)  # 1

    all_list = [anagram for l in hash_dict.values() for anagram in l if len(l) > 1]

    return [w for w in word_list if w in all_list]


if __name__ == '__main__':
    print(anagram_finder(["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"]))

#Solution 2 - Thanks Shahram

import numpy as np
def wordmismatch(W):
    W_L=[]
    for i in range(0,len(W)):
        for j in range(0,len(W)):
            w1=list(W[i].lower())
            w2=list(W[j].lower())
            if (i!=j):
                if (len(w1)==len(w2)):
                    if (np.sum(np.sort(w1)==np.sort(w2))==len(w1)):
                        if w1 not in W_L:
                            W_L.append(W[i])
                        if w2 not in W_L:
                            W_L.append(W[j])      
    X=np.unique(W_L)
    W_O=[]
    for w in W:
        if (w in X):
            W_O.append(w)
    return W_O

 #Solution 3 - Thanks M. Frantz
 def anagrams(wordlist):
    ang_list = []
    for i in wordlist:
        word_count = 0
        for x in wordlist:
            if sorted(list(i.lower())) == sorted(list(x.lower())):
                word_count += 1
        if word_count > 1:
            ang_list.append(i)
    return ang_list

#Solutions 4 -- Thanks Chris for interneting! Super Python!

def get_anagrams2(words):

    normalized = [''.join(sorted(w)) for w in words]

    d = Counter(normalized)

    return [w for w, n in izip(words, normalized) if d[n] > 1]

