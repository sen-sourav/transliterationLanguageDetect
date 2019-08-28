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
  fin = open("koreancorpus.txt", 'r')
  fout = open("cleanedkoreancorpus.txt", 'w')
  
  feng = open("commonengwordcontaminant.txt", "r")
  englishwords = [_.strip() for _ in feng.readlines()]
  feng.close()

  words = ["ooh", "oh", "eh", "ye", "ah", "yeh", "la"]
  t = {ord(c): " " for c in "\"!@#$%^&*()[]{};:,./<>?\|`~-=_+"}
  lines = fin.readlines()
  fin.close()
  deleteblock = False
  for l in lines:
      l = l.translate(t)
      if any(l.split().count(w) >=2 for w in words): continue
      if (not deleteblock):
  	    if any(word in l for word in englishwords) or (l.strip()=="") or (not isEnglish(l)): 
  	        continue
  	    else:
                l = re.sub(" +", " ", l)
                if (l.split() != "") and (not l.strip().isdigit()) and any(len(_)>1 for _ in l.split()): fout.write(l.strip() + "\n")
      elif ("fill in your details below or click an icon to log in" in l): 
          deleteblock = True  ##blocked deleted
      elif ("blog at wordpress.com." in l) and deleteblock:
          deleteblock = False
      else:
          continue
  fout.close()
