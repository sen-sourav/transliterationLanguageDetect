import re

# -*- coding: utf-8 -*-
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

if __name__ == '__main__':
  fin = open("banglacorpus.txt", 'r')
  fout = open("cleanedbanglacorpus.txt", 'w')
  
  feng = open("commonengwordcontaminant.txt", "r")
  englishwords = [_.strip() for _ in feng.readlines()]
  feng.close()

  words = ["ooh", "oh", "eh", "ye", "ah", "yeh", "la"]
  t = {ord(c): " " for c in "\"!@#$%^&*()[]{};:,./<>?\|`~-=_+"}
  lines = fin.readlines()
  fin.close()
  for l in lines:
      l = l.translate(t)
      if any(l.split().count(w) >=2 for w in words): continue
      elif any(word in l for word in englishwords) or (l.strip()=="") or (not isEnglish(l)): 
          continue
      else:
          l = re.sub(" +", " ", l)
          if (l.split() != "") and (not l.strip().isdigit()) and any(len(_) > 1 for _ in l.split()) : fout.write(l.strip() + "\n")
  fout.close()
