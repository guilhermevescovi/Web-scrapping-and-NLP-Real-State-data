# Question #2 hashfunction to find duplicates
HN=32452843
from collections import Counter
def calculationhashwithoutsequence(string):
    hash=1
    frq=dict(Counter(string).most_common())
    for i in range(32,128):
        if(chr(i) in frq):
            hash+=frq[chr(i)]
        hash=((hash*20)+1)%HN
    return hash

def calculationhashwithsequence(string):
    hash=1
    index=0
    for i in list(string):
        hash+=ord(i)*(index+1)
        hash=((hash*128*20)+1)%HN
        index+=1
    return hash

#text= open('passwords2.txt', 'r')
#lines=text.readlines(1000000)
#text.close()
#text= open('passwords3.txt', 'w')
#text.writelines(lines)

hashmap=[None]*HN
duplicates=0
falsepositives=0
with open('passwords2.txt', 'r') as text:
    for line in text:
        line=line.strip()
        index=calculationhashwithsequence(line)
        #line="".join(sorted(list(line)))
        if(hashmap[index] is None):
            hashmap[index]=dict()
        if(line in hashmap[index]):
            hashmap[index][line]+=1
            duplicates+=1
        else:
            hashmap[index][line]=1
            if(len(hashmap[index])>1):
                falsepositives+=1

   


print("Number of duplicates are: ",duplicates," and fasle positives are: ",falsepositives)