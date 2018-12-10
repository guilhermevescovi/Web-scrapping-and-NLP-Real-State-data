# NH is the prime number be the Max length of our Hash table When ever we build hash function we mode it with NH so our hash function always return value below NH

HN=32452843
from collections import Counter


def calculationhashwithoutsequence(string):
    hash=1
    frq=dict(Counter(string).most_common())
    #we create pairs of every word with its frequency
    for i in range(32,128): # ASCII range of visible characters
        if(chr(i) in frq):
            hash+=frq[chr(i)] #if word exists in the string make its frency on index of its ASCII
        hash=((hash*20)+1)%HN #there would be max 20 frequency of any character so we take 20 as section size 
    return hash

def calculationhashwithsequence(string):
    hash=1
    index=0
    for i in list(string):
        hash+=ord(i)*(index+1) # for every word we multiply its index with its ASCII
        hash=((hash*128*20)+1)%HN #the max of product of index and ASCII is 128*20 so we take section size
        index+=1
    return hash