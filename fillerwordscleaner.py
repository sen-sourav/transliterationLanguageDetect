words = ["ooh", "oh", "eh", "ye", "ah", "yeh"]

fin = open("koreancorpus.txt", 'r')

lines = fin.readlines()

fout = open("cleanedkoreancorpus.txt", 'w')

for l in lines:
    pd = True
    for w in words:
       if l.split().count(w) >= 2: 
           pd = False
    if pd:
        print(l)
        fout.write(l)

#[[fout.write(l) for w in words if l.split().count(w) < 2] for l in lines]
        
fout.close()

