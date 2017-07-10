"""
Tuesday Morning Exercise 

Rotation ciphers are very vulnerable to brute force attacks. 
There are only 25 possible ways to decrypt 
the message.

Example Encoded Message:ymjxvznwwjqnxhzyj

Possible Decoded Messages:

znkywaoxxkroyiazk, aolzxbpyylspzjbal, bpmaycqzzmtqakcbm,
cqnbzdraanurbldcn, drocaesbbovscmedo, espdbftccpwtdnfep,
ftqecguddqxueogfq, gurfdhveeryvfphgr, hvsgeiwffszwgqihs,
iwthfjxggtaxhrjit, jxuigkyhhubyiskju, kyvjhlziivczjtlkv,
lzwkimajjwdakumlw, maxljnbkkxeblvnmx, nbymkocllyfcmwony,
ocznlpdmmzgdnxpoz, pdaomqennaheoyqpa, qebpnrfoobifpzrqb,
rfcqosgppcjgqasrc, sgdrpthqqdkhrbtsd, thesquirreliscute,
uiftrvjssfmjtdvuf, vjguswkttgnkuewvg, wkhvtxluuholvfxwh,
xliwuymvvipmwgyxi

If you scan through the list you will see only a few that contain 
an english word longer than two characters. 
thesquirreliscute is the only one that could be completely 
seperated into english words to form the message
 "the squirrel is cute".

Your job for this morning exercise is to make a function that will give all possible decoded messages 
given the encoded message and suspected contents.

decode('ymjxvznwwjqnxhzyj','squirrel') # returns ['thesquirreliscute']
decode('lzwespnsdmwakafxafalq','max')  # returns ['maxftqotenxblbgybgbmr', 'themaxvalueisinfinity']
"""

#Solution 1
def decode(msg, contents):
    ords = [ord(c) for c in msg]
    a = ord('a')
    trans_list = []
    for i in range(1, 26):
        trans_list.append(''.join([chr(((num+i-a)%26)+a) for num in ords]))
    return [answer_string for answer_string in trans_list if contents in answer_string]


#Solution 2
from string import lowercase, maketrans, translate

def rotations(str):
    for i in range(1, 26):
        tbl = maketrans(lowercase, lowercase[i:] + lowercase[:i])
        yield translate(str, tbl)
        
def decode (str, contents):
    return [rotation for rotation in rotations(str) if contents in rotation]


#Solution 3 - Thanks Tiffany
def decode(text, suspect):
        
    # Generate a list of possible decoded messages, one for each single-shifted alphabet map.
    # Load the map into a deque, and rotate by n positions.
    map1 = 'abcdefghijklmnopqrstuvwxyz'
    msgList = []
    mapDeque = collections.deque(map1)
    for n in range(1,26):
        decodeMap = list(mapDeque)
        msgList.append(''.join([map1[x] for x in [decodeMap.index(text[i]) for i in range(0,len(text))]]))
        mapDeque.rotate(1)

    # From the list of possible decoded messages, search for the given 'suspected contents', and return a list of any of the
    # decoded messages that have the 'suspected contents' in it
    results = []
    for i in range(0,len(msgList)):
        if (string.find(msgList[i],suspect) >= 0):
            results.append(msgList[i])

    return results
