def scramble(unscrambled):
    import string, random, re
    splitter = re.compile(r'\s')
    words = splitter.split(u''.join(ch for ch in unscrambled if ch not in
set(string.punctuation)))
    for word in words:
        if len(word) < 4: continue
        mid = list(word[1:-1])
        random.shuffle(mid)
        scrambled = u'%c%s%c' % (word[0], ''.join(mid), word[-1])
        unscrambled = unscrambled.replace(word, scrambled, 1)
   
    return unscrambled
        
filename=input("enter the file name:")
with open(filename, 'r') as f:
     data = f.readlines()
file = open('testfile.txt','w')
str1=''
for line in data:
    sentences = line.split()
    sentences=sc(sentences)
    str1 += ' '.join(sentences)+'\n'
file.close()
file=open('test1scram.txt','w')
file.write(str1)
file.close()
print("file has been scrambled")

