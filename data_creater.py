def wordbagmaker(corpusfilename, label):
   f = open(corpusfilename, 'r')
   lines = f.readlines()
   
   import random
   import pyphen
   worddict = []
   dic = pyphen.Pyphen(lang='it_IT')
   for l in lines:
       words = l.split()
       if (len(words) < 2): continue #only words present in sentences used, not single word sentences
       for w in words:
          if (len(w) > 1) and w.isalpha(): #words with digits not used and single letter words not used
              worddict.append(dic.inserted(w) + " : " + label)

   random.shuffle(worddict)   #shuffle the list
   return worddict





if __name__ == "__main__":

    foK = open("koreanwordbag.txt", 'w')
    [foK.write(wK+"\n") for wK in wordbagmaker("cleanedkoreancorpus.txt", "K")]
    foK.close()
    foB = open("banglawordbag.txt", 'w')
    [foB.write(wB+"\n") for wB in wordbagmaker("cleanedbanglacorpus.txt", "B")]
    foB.close()
